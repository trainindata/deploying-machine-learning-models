NAME=samira-ml-api



build-ml-api-heroku:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t registry.heroku.com/$(NAME)/web .

push-ml-api-heroku:

	docker push registry.heroku.com/${HEROKU_APP_NAME}/web:latest