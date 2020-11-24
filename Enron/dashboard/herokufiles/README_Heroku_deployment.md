# To deploy to Heroku follow these steps

## Required files
## - dashboard.py
## - requirements.txt
## - Procfile
## - setup.sh


## Intialize git
cd ./dashboard
git init

heroku login
heroku create
git add .
git commit -m 'deployment'
git push heroku master

## Check if app was successfully deployed
heroku ps:scale web=1
