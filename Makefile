# Heroku app name
NAME=deploy-ml-application
# The current git commit id
COMMIT_ID=$(shell git rev-parse HEAD)

# Command 1: This creates our image from the Dokerfile
# The COMMIT_ID will be the tag of built image
# It's made this way so that we can trace any image to its Git commit
build-ml-api-heroku:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t registry.heroku.com/${NAME}/web:${COMMIT_ID} .

# Command 2: We take our built image and we push it to the Heroku registry
push-ml-api-heroku:
	docker push registry.heroku.com/${HEROKU_APP_NAME}/web:${COMMIT_ID}
