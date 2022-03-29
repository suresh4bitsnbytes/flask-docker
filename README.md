
# flask-docker

Dockerize a flask app with gunicorn and nginx.

  

### Dockerize flask app

```sh

docker build -t <tag-name>  api/
docker run -it -p 5000:5000 --name <container-name> <image-name/id>
```

### To access the api
```sh
curl http://localhost:5000/users
```
