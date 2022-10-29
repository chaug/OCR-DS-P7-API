import os

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


#################################################
# Services
#################################################

@app.get("/")
def hello_world():
  return {
    "message" : "Hello World!",
  }


#################################################

if __name__ == "__main__":
  # for direct command line calls with python
  import uvicorn
  uvicorn.run(app)
