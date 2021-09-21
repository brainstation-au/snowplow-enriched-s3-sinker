import base64
import json
import os

from snowplow_tsv_to_json.main import lambda_handler

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def test_handler():
    with open(os.path.join(__location__, 'event.json'), 'r') as event_file_handle, \
        open(os.path.join(__location__, 'transformed.txt'), 'r') as transformed_file_handle:
        lambda_response = lambda_handler(json.loads(event_file_handle.read()), None)
        for record in lambda_response.get('records'):
            encoded_data = record.get('data')
            data = base64.b64decode(encoded_data).decode('utf-8')
            assert data == transformed_file_handle.readline()
