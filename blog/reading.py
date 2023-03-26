import click
from notion_client import Client
from notion_client.helpers import iterate_paginated_api
from itertools import chain

from pprint import pprint


@click.command()
@click.argument('notion_token', envvar='NOTION_TOKEN')
@click.option('--database-id', default='6300c201957f499a81ebc9a097950fc8')
def main(notion_token, database_id):
    notion = Client(auth=notion_token)
    for result in iterate_paginated_api(notion.databases.query, database_id=database_id):
        for item in result:
            # TODO
            pprint(item['created_time'])
            pprint(item['properties']['Name']['title'][0]['plain_text'])
            pprint(item['properties']['URL']['url'])
