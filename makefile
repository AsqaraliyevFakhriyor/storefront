run:
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

createsuper:
	python3 manage.py createsuperuser

shell:
	python3 manage.py shell

gitpush:
	git add .
	git commit -m "bug-fix/feature"
	git push

install:
	python3 -m venv venv
	source venv/bin/activate
	pip3 install -r requirements.txt

