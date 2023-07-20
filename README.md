# uuid-gen
Generates UUIDs on the fly 

## Summary
This application creates an endpoint that generates a uuid. When deployed locally, the user can run the following command to generate a uuid

```
curl localhost:8000/api/generate/v1
```

## Running locally
Do the following to run locally

```
export DB_PASSWORD=`value shared in 1password`
uvicorn main:app --reload
```

## Production Deploy Process
Build the docker image locally
```
docker build -t uuid-gen .
```

Authenticate with ECR
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 194956116872.dkr.ecr.us-east-1.amazonaws.com
```
Get the image id
```
docker images
```

Tag the image
```
docker tag <image_id> 194956116872.dkr.ecr.us-east-1.amazonaws.com/dlouksinfracandidate:latest
```

Push the image to ECR
```
docker push 194956116872.dkr.ecr.us-east-1.amazonaws.com/dlouksinfracandidate:latest
```