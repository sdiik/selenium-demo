from dotenv import load_dotenv
import os

load_dotenv()

#testrail_config.py
TESTRAIL_URL = os.getenv('TESTRAIL_URL')
TESTRAIL_EMAIL = os.getenv('TESTRAIL_EMAIL')
TESTRAIL_API_KEY = os.getenv('TESTRAIL_API_KEY')
TESTRAIL_PROJECT_ID = os.getenv('TESTRAIL_PROJECT_ID', "1")
TESTRAIL_RUN_ID = os.getenv('TESTRAIL_RUN_ID', "17")

