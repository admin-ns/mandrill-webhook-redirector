from flask import Flask, redirect, request
import json

app = Flask(__name__)

@app.route("/", methods=['POST', 'HEAD'])
def index():
    if request.method == 'HEAD':
        return ''
    mandrill_event = json.loads(request.form['mandrill_events'])
    metadata = (mandrill_event[0]['msg']['metadata'])
    domain = metadata['domain']
    return redirect(domain.rstrip('/') + "/menu/autounsub/")
if __name__ == "__main__":
    app.run()
