up:
	docker compose up -d

down:
	docker compose down

build:
	docker compose up -d --build

bash:
	docker exec -it uploadfiles-backend-1 bash

makemigrations:
	docker exec -it uploadfiles-backend-1 python manage.py makemigrations

migrate:
	docker exec -it uploadfiles-backend-1 python manage.py migrate

celery logs:
	docker logs -f uploadfiles-celery-1

logs:
	docker logs -f uploadfiles-backend-1

test:
	docker exec -it uploadfiles-backend-1 python manage.py test

createsuperuser:
	docker exec -it uploadfiles-backend-1 python manage.py createsuperuser