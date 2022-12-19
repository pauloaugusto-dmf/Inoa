up:
	docker-compose up -d

up-logs:
	docker-compose up

down:
	docker-compose down

console:
	docker-compose exec django python manage.py shell

test:
	docker-compose exec django pytest

logs:
	docker-compose logs
