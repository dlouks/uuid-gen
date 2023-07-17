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
export dbpassword=`value shared in 1password`
uvicorn main:app --reload
```

## Production Deploy Process
