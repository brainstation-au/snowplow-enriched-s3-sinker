import base64
import json

from snowplow_analytics_sdk import event_transformer

def transform(data: str) -> str:
    tsv_record = base64.b64decode(data).decode('utf-8')
    dict_record = event_transformer.transform(tsv_record)
    return base64.b64encode(str.encode(f"{json.dumps(dict_record)}\n"))

def lambda_handler(event, context):
    print(json.dumps(event))
    output = [dict(
        recordId=r.get('recordId'),
        data=transform(r.get('data')),
        result='Ok') for r in event.get('records')]
    return dict(records=output)
