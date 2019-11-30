import sentry_sdk
import os
from bottle import Bottle, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://dd6544ff4918444888a721566f8e583f@sentry.io/1832506",
    integrations=[BottleIntegration()]
)

app = Bottle()


@app.route('/')
def index():
    # raise RuntimeError("There is an error!")
    return


@app.route('/success')
def success():
    return


@app.route('/fail')
def fail():
    raise RuntimeError("There is an error!")

app.run(host='localhost', port=8080)
