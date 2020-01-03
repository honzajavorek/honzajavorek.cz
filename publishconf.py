import os
import sys
from operator import itemgetter

import requests

sys.path.append(os.curdir)
from pelicanconf import *


DELETE_OUTPUT_DIRECTORY = True
LOAD_CONTENT_CACHE = False
GOOGLE_ANALYTICS = 'UA-1316071-6'


def get_deployment_url():
    sha = os.getenv('NOW_GITHUB_COMMIT_SHA')
    org = os.getenv('NOW_GITHUB_COMMIT_ORG', 'honzajavorek')
    repo = os.getenv('NOW_GITHUB_COMMIT_REPO', 'honzajavorek.cz')

    res = requests.get(f'https://api.github.com/repos/{org}/{repo}/deployments',
                       params=dict(sha=sha))
    res.raise_for_status()
    deployment = sorted(res.json(), key=itemgetter('created_at'), reverse=True)[0]

    res = requests.get(deployment['statuses_url'])
    res.raise_for_status()
    status = sorted(res.json(), key=itemgetter('created_at'), reverse=True)[0]

    return status['target_url']

SITEURL = get_deployment_url() if os.getenv('NOW_GITHUB_COMMIT_SHA') else 'https://honzajavorek.cz'
