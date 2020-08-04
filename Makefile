# The current git commit id
# COMMIT_ID=$(shell git rev-parse HEAD)

# Command 1: This creates our image from the Dokerfile
# The COMMIT_ID will be the tag of built image
# It's made this way so that we can trace any image to its Git commit
build-ml-api-heroku:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t registry.heroku.com/${APP_NAME}/web .

# Command 2: We take our built image and we push it to the Heroku registry
push-ml-api-heroku:
	docker push registry.heroku.com/${APP_NAME}/web:latest

build-ml-api-aws:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t $(APP_NAME):latest .

push-ml-api-aws:
	docker push ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/$(APP_NAME):latest

tag-ml-api:
	docker tag $(APP_NAME):$(COMMIT_ID) ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/$(APP_NAME):latest
