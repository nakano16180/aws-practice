# aws_practice

## Test

```
$ docker run --rm -v "$PWD":/var/task lambci/lambda:python3.7 function_setup.lambda_handler
```

## Run as a API server

```
$ docker run --rm \
  --name d-lambda \
  --net=minio-lambda-net \
  -p 9001:9001 \
  -e AWS_ACCESS_KEY_ID=minioadmin \
  -e AWS_SECRET_ACCESS_KEY=minioadmin \
  -e DOCKER_LAMBDA_STAY_OPEN=1 \
  -v "$PWD":/var/task \
  lambci/lambda:python3.7 \
  function.lambda_handler
```


```
$ curl -X POST -d '{}' http://localhost:9001/2015-03-31/functions/myfunction/invocations
```