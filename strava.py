# Inspired a lot by:
# https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86


import sys
import os
import json
from pathlib import Path
import time
from datetime import date
import math

import requests


STRAVA_TOKENS_PATH = Path(__file__).parent / '.strava'
STRAVA_CLIENT_ID = os.environ['STRAVA_CLIENT_ID']
STRAVA_CLIENT_SECRET = os.environ['STRAVA_CLIENT_SECRET']
ACTIVITIES_PER_PAGE = 200
ACTIVITY_TYPES = {
    'run': 'běhal',
    'walk': 'se procházel',
    'hike': 'chodil po túrách',
}


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


def get_activities(access_token):
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
    return activities


def filter_by_dates(activities, start_date, end_date):
    for activity in activities:
        activity_date = date.fromisoformat(activity['start_date_local'][:10])
        if activity_date >= start_date and activity_date <= end_date:
            yield activity


def calc_stats(activities):
    stats = {}
    for activity in activities:
        key = activity['type'].lower()
        stats.setdefault(key, dict(count=0, time=0, distance=0))
        stats[key]['count'] += 1
        stats[key]['time'] += (activity['elapsed_time'] / 60 / 60)  # h
        stats[key]['distance'] += (activity['distance'] / 1000)  # km
    for substats in stats.values():
        substats['time'] = math.ceil(substats['time'])
        substats['distance'] = math.ceil(substats['distance'])

    ordering = list(ACTIVITY_TYPES.keys())
    stats = dict(sorted(stats.items(), key=lambda item: ordering.index(item[0])))
    return stats


def stats_to_text(start_date, end_date, stats):
    parts = [
        f"{substats['count']}⨉ {ACTIVITY_TYPES[activity_type]} ({substats['distance']} km, {substats['time']} hodin)"
        for activity_type, substats in stats.items()
    ]

    total_days = (end_date - start_date).days + 1
    total_distance = sum(int(substats['distance']) for substats in stats.values())
    total_time = sum(int(substats['time']) for substats in stats.values())

    text = f"Během {total_days} dní od {start_date.day}.{start_date.month}. do {end_date.day}.{end_date.month}. "
    text += f"jsem {', '.join(parts)}."
    text += f" Celkem jsem se hýbal {total_time} hodin a zdolal při tom {total_distance} kilometrů."
    return text


if __name__ == '__main__':
    activities = get_activities(get_access_token())
    try:
        start_date = date.fromisoformat(sys.argv[1])
    except IndexError:
        start_date = input('Start date: ').strip()
    try:
        end_date = date.fromisoformat(sys.argv[2])
    except IndexError:
        end_date = input('End date (defaults to today): ').strip() or date.today()
    stats = calc_stats(filter_by_dates(activities, start_date, end_date))
    print(stats)
    print(stats_to_text(start_date, end_date, stats))
