
.PHONY: build deploy local

PORT=8080
name=slackify
project=slackify-main
dev_project=slackify-dev

build:
	gcloud builds submit \
	--region=europe-west1 \
	--tag europe-west1-docker.pkg.dev/${project}/${name}/test-image:tag1

deploy:
	gcloud run deploy ${name} \
	--platform=managed \
	--region=europe-west2 \
	--allow-unauthenticated \
	--env-vars-file=.env.yaml \
	--image=europe-west1-docker.pkg.dev/${project}/${name}/test-image:tag1 \
	--memory=500M

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
	gcr.io/${dev_project}

pull:
	docker pull gcr.io/${dev_project}