SCRIPT_DIR=$(dirname $0)
if [[ -f ${SCRIPT_DIR}/.env ]]; then
  EXTRA_OPTS=--env-file=${SCRIPT_DIR}/.env
fi

# run FastAPI app defined in app/main.py
uvicorn main:app --reload --app-dir app --port ${PORT:-8000} ${EXTRA_OPTS}
