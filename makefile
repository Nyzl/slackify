
.PHONY: build deploy local

PORT=8080
project=customerjourney-214813/slackify
dev_project=customerjourney-214813/slackify-test
keyfile=$(PWD)/creds

build:
	gcloud builds submit \
	--tag gcr.io/${project}

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
	-v ${keyfile}:/slackify/creds:ro \
	-e GOOGLE_APPLICATION_CREDENTIALS=/slackify/creds/google.json \
	slackify
#	gcr.io/${dev_project}

pull:
	docker pull gcr.io/${dev_project}



