API_DIR:=api

.requirements:
	pip3 install --no-cache-dir -r requirements.txt
	touch .requirements

migrate:
	python3 ${API_DIR}/manage.py makemigrations
	python3 ${API_DIR}/manage.py migrate

run: .requirements migrate
	python3 ${API_DIR}/manage.py runserver 0.0.0.0:8000