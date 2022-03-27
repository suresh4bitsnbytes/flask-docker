# flask-docker
Dockerize a flask app with gunicorn and nginx.

### Start gunicorn server
```bash
cd api
gunicorn -w 3 -t 30 -b :5000 --reload wsgi:app
'''
