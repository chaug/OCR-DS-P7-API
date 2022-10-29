set -e
set -x

SCRIPT_DIR=$(dirname $0)
source ${SCRIPT_DIR}/docker.env

LOCAL_ARGS="-i --rm"
PRODUCTION_ARGS="-d -e LOG_LEVEL=warning"

COMMON_ARGS="-p ${PORT}:${DOCKER_PORT} -e PORT=${DOCKER_PORT}"

# docker run ${LOCAL_ARGS}      ${COMMON_ARGS} ${DOCKER_IMAGE}
docker run ${PRODUCTION_ARGS} ${COMMON_ARGS} ${DOCKER_IMAGE}
