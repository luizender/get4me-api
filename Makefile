API_DIR:=api

makemigrations:
	python3 ${API_DIR}/manage.py makemigrations

migrate:
	python3 ${API_DIR}/manage.py migrate

run: migrate
	python3 ${API_DIR}/manage.py runserver 0.0.0.0:8000