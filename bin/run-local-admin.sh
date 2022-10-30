SCRIPT_DIR=$(dirname $0)
if [[ -f ${SCRIPT_DIR}/.env ]]; then
  EXTRA_OPTS=--env-file=${SCRIPT_DIR}/.env
fi

# run FastAPI app defined in admin/main.py
uvicorn main:app --reload --app-dir admin --port ${PORT:-8099} ${EXTRA_OPTS}
