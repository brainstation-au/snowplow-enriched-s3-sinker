import base64
import json

from snowplow_analytics_sdk import event_transformer

def transform(data: str) -> str:
    tsv_record = base64.b64decode(data).decode('utf-8')
    dict_record = event_transformer.transform(tsv_record)
    return base64.b64encode(str.encode(f"{json.dumps(dict_record)}\n")).decode('utf-8')

def lambda_handler(event, context):
    output = []
    for record in event.get('records', []):
        try:
            data = transform(record.get('data'))
            output.append(dict(
                recordId=record.get('recordId'),
                data=data,
                result='Ok'
            ))
        except:
            output.append(dict(
                recordId=record.get('recordId'),
                data=record.get('data'),
                result='ProcessingFailed'
            ))
    return dict(records=output)
