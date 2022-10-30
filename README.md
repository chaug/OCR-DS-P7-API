# OCR-DS-P7-API

## Dependencies

Skeleton to build and deploy an API based on:
* [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/) to develop the services
* [REST Client for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) to test the API


## Get started

### Initial setup

```bash
pip install -r requirements.txt
```

### Launch the API locally

```bash
uvicorn main:app --reload --app-dir src
# or a direct python call (without reload option)
python src/main.py
# or the wrapper script
./bin/run-local.sh
```

### Check API

The basic provided URL are:
* http://localhost:8000/docs swagger UI: automatic powerful inventory of services
* http://localhost:8000/openapi.json swagger definition
* http://localhost:8000/ default route: here it simply exposes an "Hello World!"

```bash
curl http://localhost:8000/
{"message":"Hello World!"}
```

You can also check services with the `humao.rest-client` VSC plugin:
* [./tests/api/local-basics.rest](./tests/api/local-basics.rest)
* [./tests/api/services.rest](./tests/api/services.rest)

For the second test file, you need to copy `./test/api/.env.sample` file as `./test/api/.env` and change the contained values to your setup.
See the [plugin documentation](https://github.com/Huachao/vscode-restclient) and [dotenv's one](https://github.com/motdotla/dotenv) for more information


## Deployment targets

### With docker

You can build an image and run a container from it, to expose your services under port 80:
```bash
DOCKER_IMAGE=my-fastapi

# build image
docker build -t ${DOCKER_IMAGE} .

# run image for local test (interactive and auto remove at stop time)
docker run -i --rm -p 80:80 ${DOCKER_IMAGE}

# run image as a daemon
docker run -d -p 80:80 ${DOCKER_IMAGE}
```


### With Heroku 

TODO


### With deta.sh

[Official documentation](https://fastapi.tiangolo.com/deployment/deta/)

Install the CLI and login:
```bash
# with powershell (Windows)
iwr https://get.deta.dev/cli.ps1 -useb | iex
# with bash (Linux, macOS)
curl -fsSL https://get.deta.dev/cli.sh | sh

deta version
# deta v1.3.3-beta x86_64-windows

deta login
```

Create a project (from the UI)

Create deta micro (runtime unit):
```bash
cd app
cp ../requirements.txt .
deta new --project OCR-DS-P7-API-deta --name fastapi
```

You should then have a returned endpoint. You can test its swagger:
* https://xxxxxx.deta.dev/docs
