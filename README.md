# weather-alerts-crud
Weather alerts api for handling receivers

# Installation
`npm install serverless`
`npm install serverless-requirements-plugin serverless-dotenv-plugin`
`pip install -r requirements.txt`

# Testing
export all Enviroment Variables using:
`export $(xargs < .env)`

To run all the tests use:
`pytest`

To run a specific test, use:
`pytest tests/<filename> -v`
Add `-v` for verbose mode

# Deploy
`sls deploy -s prod`
