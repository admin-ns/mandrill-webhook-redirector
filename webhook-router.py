import os
from flask import Flask, redirect, request
import json

app = Flask(__name__)

@app.route("/", methods=['POST','GET', 'HEAD'])
def index():
    if request.method == 'HEAD':
        return ''
    if request.method == 'GET':
        return 'reqIest = GET'
    mandrill_event = json.loads(request.form['mandrill_events'])
    metadata = (mandrill_event[0]['msg']['metadata'])
    domain = metadata['domain']
    return redirect(domain.rstrip('/') + "/menu/autounsub/")
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)