release: python manage.py migrate
web: python manage.py collectstatic --noinput; python manage.py compress; gunicorn durhamforall.wsgi --log-file -
