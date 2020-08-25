import argparse
import json
import yaml
from elastic_workplace_search import Client


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', help='source name',
                        choices={'employees','issues','trello','bikes'})
    parser.add_argument('-p', '--purge', action='store_true',
                        help='purge all data for the source')
    return parser.parse_args()

def get_config(filename='config.yaml'):
    with open(filename) as f:
        return yaml.safe_load(f)

def get_data(filename):
    with open(filename) as f:
        return [json.loads(line) for line in f]

def upload_data():
    data = get_data(source['file'])
    client.documents.index_documents(key, data)

def purge_data():
    data = get_data(source['file'])
    ids = [str(i) for i in range(1,len(data)+1)]
    client.documents.delete_documents(key, ids)

args = parse_args()
config = get_config()
deployment =config['deployment']
source = get_config()[args.source]
key = source['key']
base_url = deployment['endpoint'] + '/api/ws/v1'
client = Client(deployment['access_token'], base_url=base_url)
if args.purge:
    purge_data()
else:
    upload_data()



