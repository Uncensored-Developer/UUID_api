from flask import Flask, Response
from datetime import datetime
from models import GeneratedUUID
import pytz
import uuid
import json

app = Flask(__name__)


@app.route('/')
def fetch_uuids():
    timestamp = str(datetime.now(tz=pytz.utc))
    uuid_str = str(uuid.uuid4())
    GeneratedUUID(timestamp=timestamp, uuid=uuid_str).create()
    uuids = GeneratedUUID.fetch_all()
    return Response(json.dumps(uuids), mimetype='application/json')


if __name__ == '__main__':
    app.run(port=5002)
