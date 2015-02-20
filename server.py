import os
from flask import Flask
from radio import RadioScanner

app = Flask(__name__)
radio_scanner = RadioScanner()


@app.route('/broadcast')
def broadcast():
    radio_scanner.scan()
    return "OK"


app.debug = True
app.run(host='0.0.0.0', port=int(os.environ['PORT']))
