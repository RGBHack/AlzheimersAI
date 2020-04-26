:: run this to update firebase w out having to type stuff
@echo off
call cd server
call gcloud builds submit --tag gcr.io/alzheimersai-2121/alzheimersai
call gcloud beta run deploy --image gcr.io/alzheimersai-2121/alzheimersai
call cd ..