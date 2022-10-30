import os
from pathlib import Path

from fastapi import FastAPI

#################################################
# Initialize the application
# port may be overridden by environment value
#################################################

PORT = int(os.environ.get('PORT', 8000))
app = FastAPI(
  port=PORT,
  title="FastAPI demo",
)

APP_DIR = Path(__file__).parent
LOCAL_MODEL = APP_DIR / 'models' / 'default.joblib'

#################################################
# Services
#################################################

@app.get("/")
async def hello_world():
  return {
    "message" : "Hello World!",
  }

@app.get("/echo/{message}")
async def echo(message: str):
  return {
    "message" : message,
  }

@app.get("/local_model")
async def test_local_model():
  if not LOCAL_MODEL.exists():
    return []
    with LOCAL_MODEL.open() as stream:
      return stream.read().split('\n')


#################################################
# Deta specifics services
#################################################

HAS_DETA = False
try:
  from deta import Deta
  HAS_DETA = True
except ModuleNotFoundError as exc:
  pass
try:
  project = Deta()
except AssertionError as exc:
  HAS_DETA = False

if HAS_DETA:
  drive = project.Drive("models")

  @app.get("/models")
  async def list_models():
    return drive.list()

  @app.get("/model_size")
  async def test_model():
      model = drive.get("default.joblib")
      return len(model.read())


#################################################

if __name__ == "__main__":
  # for direct command line calls with python
  import uvicorn
  uvicorn.run(app)
