import os
import sys
from operator import itemgetter
import logging

import requests

sys.path.append(os.curdir)
from pelicanconf import *


logger = logging.getLogger(__name__)


DELETE_OUTPUT_DIRECTORY = True
GOOGLE_ANALYTICS = 'UA-1316071-6'


NOW_GITHUB_COMMIT_SHA = os.getenv('NOW_GITHUB_COMMIT_SHA')
logger.info('NOW_GITHUB_COMMIT_SHA=%s', NOW_GITHUB_COMMIT_SHA)

NOW_GITHUB_COMMIT_REF = os.getenv('NOW_GITHUB_COMMIT_REF')
logger.info('NOW_GITHUB_COMMIT_REF=%s', NOW_GITHUB_COMMIT_REF)


def get_deployment_url(sha):
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


if NOW_GITHUB_COMMIT_SHA and NOW_GITHUB_COMMIT_REF != 'master':
    SITEURL = get_deployment_url(NOW_GITHUB_COMMIT_SHA)
else:
    SITEURL = 'https://honzajavorek.cz'
logger.info('SITEURL=%s', SITEURL)
