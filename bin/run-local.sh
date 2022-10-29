# run FastAPI app defined in src/main.py
uvicorn main:app --reload --app-dir src --port ${PORT:-8000}
