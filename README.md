# B2-Alerting
Python script to determine if the latest file in a B2 bucket is older than 24 hours. 


## Main.py
Create a `.env` file in your local directory and add the following ENVs
```
# B2 API endpoint for buckets with sample data
export ENDPOINT='https://api.backblazeb2.com'
export KEY_ID='XXX'
export APPLICATION_KEY='XXX'
```
Execute the script and simply add your bucket name as a parameter

Example:
`./main.py my-bucket`

## Lambda Function
Build a zip file with the requirements and upload them to your function.

Add the following environment variables to your function.

- KEY_ID
- APPLICATION_KEY


#### Input
Send the bucket name to your function with no key and in quotes.

- You can create an EventBridge rule that runs every day at the same time.
    - If you use EventBridge set the input to constant and the value to your bucket name surrounded by quotes. 

#### Output
The output can then be sent to a notification service like SNS or SES

- Add a destination and be sure to set the condition to "On success"

Example:
`"my-bucket"`
