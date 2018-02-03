# Durham for All website

### Dependencies

* Docker (It is also possible to use heroku cli to run a local version of the site, but most of the local dev tooling is set up around docker)
* Heroku-cli

### To run the site locally

1. First run `make install` -- this will build the docker container for the site, load in initial fixtures and run any pending migrations.
2. On subsequent runs, you can just do `make up`, since the container does not need to be built.
3. To stop the site, run `make down`. Database state will not persist once you've run `make down`. If you need persistent database state, set up a volume mapping in docker-compose.yml by uncommenting the line in `docker-compose.yml`.

### Fixtures

The JSON code in `fixtures/site_base.json` loads a basic set of pages into the site and creates an admin user with username/password `admin`/`admin`. It also sets up password auth for the site, with password `durhamforall`.

Fixtures load automatically when `make install` is called, or they can be loaded manually via `docker-compose exec web python manage.py loadddata site_base.json`.

### Deployment process
New code branches merged into `master` on this repository are automatically deployed via heroku. Heroku runs `python manage.py migrate` on new deployments, other release tasks can be run manually via `heroku run ___`.
