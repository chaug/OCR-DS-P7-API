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

