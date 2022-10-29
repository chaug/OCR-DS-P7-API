set -e
set -x

SCRIPT_DIR=$(dirname $0)
source ${SCRIPT_DIR}/docker.env

ROOT_DIR=${SCRIPT_DIR}/..

docker build -t ${DOCKER_IMAGE} ${ROOT_DIR}
