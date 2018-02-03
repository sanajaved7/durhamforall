install-dependencies:
	docker-compose run --rm vendors

install:
	docker-compose run --rm vendors
	docker-compose up -d --build
	make up

up:
	docker-compose up -d
	docker-compose exec web python manage.py migrate
	docker-compose exec web python manage.py loaddata site_base.json

down:
	docker-compose down
	
import-db:
	docker-compose down
	heroku pg:backups:capture
	heroku pg:backups:download -o .db/latest.dump
	pg_restore .db/latest.dump > .db/latest.sql
	docker-compose up -d
	docker-compose exec web python manage.py migrate
