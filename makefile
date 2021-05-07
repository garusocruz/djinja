server:
	python app/manage.py runserver

migrations:
	python app/manage.py makemigrations

migrate:
	python app/manage.py migrate

shell:
	python app/manage.py shell

su:
	python app/manage.py createsuperuser
