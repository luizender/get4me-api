API_DIR:=api

migrate:
	python3 ${API_DIR}/manage.py makemigrations
	python3 ${API_DIR}/manage.py migrate

run: migrate
	python3 ${API_DIR}/manage.py runserver 0.0.0.0:8000

clean:
	find ${API_DIR} | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
