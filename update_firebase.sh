#!/usr/bin/env zsh
# for manual firebase deployment

export GCP_PROJECT_ID=alzheimersai-2121
export IMAGE=gcr.io/alzheimersai-2121/alzheimersai
export CLOUD_RUN_SERVICE=alzheimersai
export CLOUD_RUN_REGION=us-central1
export CLOUDSDK_CORE_DISABLE_PROMPTS=1

nvm install node
npm i -g firebase-tools
pip3 install gdown
python3 travis_builder.py

docker build -t "${IMAGE}" ./server && \
docker push "${IMAGE}" && \
gcloud beta run deploy "${CLOUD_RUN_SERVICE}" --memory=1Gi \
    --image="${IMAGE}" \
    --platform=managed \
    --region="${CLOUD_RUN_REGION}" \
    --allow-unauthenticated;