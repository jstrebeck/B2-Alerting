#!/usr/bin/env python3
from b2sdk.v2 import *
from dotenv import load_dotenv
from datetime import datetime, timedelta, date
import os

def lambda_handler(event, context):   
    info = InMemoryAccountInfo()
    b2_api = B2Api(info)
    application_key_id = os.environ['KEY_ID']
    application_key = os.environ['APPLICATION_KEY']
    b2_api.authorize_account("production", application_key_id, application_key)

    bucket_name = event

    bucket = b2_api.get_bucket_by_name(bucket_name)

    for file_version, folder_name in bucket.ls(latest_only=True):

        timestamp = file_version.upload_timestamp // 1000

    dt_obj = datetime.fromtimestamp(timestamp)

    if datetime.now().date() - timedelta(hours = 24) > dt_obj.date():
        return "❌The last backup was over 24 hours ago"
        

    else:
        exit(1)