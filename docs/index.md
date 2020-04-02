## docker-lambda
  - [lambci/docker-lambda](https://github.com/lambci/docker-lambda)

### Run as a API server

```
docker run --rm \
  --name d-lambda \
  -p 9001:9001 \
  --net=minio-lambda-net \
  -e AWS_ACCESS_KEY_ID=minioadmin \
  -e AWS_SECRET_ACCESS_KEY=minioadmin \
  -e DOCKER_LAMBDA_STAY_OPEN=1 \
  -v "$PWD":/var/task \
  lambci/lambda:nodejs10.x \
  index.handler
```

```
$ curl -X POST -d '{}' http://localhost:9001/2015-03-31/functions/myfunction/invocations
```
