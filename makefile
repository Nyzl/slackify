
.PHONY: build deploy local

PORT=8080
project=slackify-main
dev_project=slackify-dev
keyfile=/Users/Ian/Documents/GitHub/slackify-data/creds/cj_data.json # need to remove this reference

build:
	gcloud builds submit \
	--region=europe-west1 \
	--tag europe-west1-docker.pkg.dev/slackify-main/slackify/test-image:tag1

deploy:
	gcloud run deploy \
	--platform managed \
	--image gcr.io/${project} \
	--memory 500M

dev-build:
	gcloud builds submit \
	--tag gcr.io/${dev_project}

dev-deploy:
	gcloud run deploy \
	--platform managed \
	--image gcr.io/${dev_project} \
	--memory 500M \
	--update-env-vars bq_dataset=slackify_test

local:
	PORT=8080 && docker run \
	-p 9090:${PORT} \
	-e PORT=${PORT} \
	-e K_SERVICE=dev \
	-e K_CONFIGURATION=dev \
	-e K_REVISION=dev-00001 \
	-v ${keyfile}:/slackify/creds/cj_data.json:ro \
	-e GOOGLE_APPLICATION_CREDENTIALS=/slackify/creds/cj_data.json \
	gcr.io/${dev_project}

pull:
	docker pull gcr.io/${dev_project}