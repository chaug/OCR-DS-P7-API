import os

from fastapi import FastAPI
from deta import Deta, send_email

#################################################
# Initialize the application
# port may be overridden by environment value
#################################################

PORT = int(os.environ.get('PORT', 8099))
app = FastAPI(
  port=PORT,
  title="FastAPI admin",
)

project = Deta(
  # TODO: local call with project key
)
drive = project.Drive("models")

#################################################
# Services
#################################################

from fastapi import File, UploadFile
from fastapi.responses import HTMLResponse

@app.get("/admin", response_class=HTMLResponse)
def admin_home():
    return """
    <form action="/admin/upload" enctype="multipart/form-data" method="post">
        <input name="file" type="file">
        <input type="submit">
    </form>
    """

@app.post("/admin/upload")
def upload_img(file: UploadFile = File(...)):
    name = file.filename
    f = file.file
    res = drive.put(name, f)
    return res

#################################################

if __name__ == "__main__":
  # for direct command line calls with python
  import uvicorn
  uvicorn.run(app)
