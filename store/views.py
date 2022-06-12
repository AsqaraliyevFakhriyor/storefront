from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.db.models import Count
from django.shortcuts import get_object_or_404

from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(queryset, many=True, context={'request': request}) # we used many=True so that serializers iterates queryset
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =  ProductSerializer(data=request.data)

        # if serializer.is_valid():
        #     serializer.validated_data 
        #     return Response(serializer.data)
        # else:
        #     Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        serializer.save()  
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', "PUT", 'Delete'])
def product_detail(request,id):

    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializer(product)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)


    product = get_object_or_404(Product, pk=id)
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data) # it will automatically call update as we sending existing obj
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        if product.orderitem_set.count() > 0:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def collection_list(request):
    if request.method == 'GET':
        queryset = Collection.objects.annotate(product_count=Count("products")).all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view()
def collection_detail(request, pk):
    return Response("Ok")