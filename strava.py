# Inspired a lot by:
# https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86


import os
import json
from pathlib import Path
import time

import requests


STRAVA_TOKENS_PATH = Path(__file__).parent / '.strava'
STRAVA_CLIENT_ID = os.environ['STRAVA_CLIENT_ID']
STRAVA_CLIENT_SECRET = os.environ['STRAVA_CLIENT_SECRET']
ACTIVITIES_PER_PAGE = 200


def get_access_token():
    try:
        strava_tokens = json.loads(STRAVA_TOKENS_PATH.read_text())
    except FileNotFoundError:
        print("Open the following link and copy the 'code' from URL after redirect:")
        print(f"\nhttps://www.strava.com/oauth/authorize?client_id={STRAVA_CLIENT_ID}&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:read_all,activity:read_all\n")
        strava_code = input('Code: ')
        response = requests.post(url='https://www.strava.com/oauth/token',
                                 data=dict(client_id=STRAVA_CLIENT_ID,
                                           client_secret=STRAVA_CLIENT_SECRET,
                                           code=strava_code,
                                           grant_type='authorization_code'))
        response.raise_for_status()
        strava_tokens = response.json()
        STRAVA_TOKENS_PATH.write_text(json.dumps(strava_tokens))

    if strava_tokens['expires_at'] < time.time():
        response = requests.post(url='https://www.strava.com/oauth/token',
                                 data=dict(client_id=STRAVA_CLIENT_ID,
                                           client_secret=STRAVA_CLIENT_SECRET,
                                           code=strava_tokens['refresh_token'],
                                           grant_type='refresh_token'))
        response.raise_for_status()
        strava_tokens = response.json()
        STRAVA_TOKENS_PATH.write_text(json.dumps(strava_tokens))

    return strava_tokens['access_token']


if __name__ == '__main__':
    access_token = get_access_token()
    activities = []
    page = 1
    while True:
        response = requests.get('https://www.strava.com/api/v3/activities', params=dict(access_token=access_token,
                                                                                        page=page,
                                                                                        per_page=ACTIVITIES_PER_PAGE))
        response.raise_for_status()
        batch = response.json()
        activities.extend(batch)
        if len(batch) < ACTIVITIES_PER_PAGE:
            break
        else:
            page += 1
    print(activities)


# total_elevation_gain
# type == 'Walk', 'Run', 'Hike',
# distance
# elapsed_time
