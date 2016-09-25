import requests
import json
import redis
import threading
from flask import Flask

from models import Killmail

from views import ChatAPI


app = Flask(__name__)


# TODO Switch to pyres worker
class Listener(threading.Thread):
    def __init__(self, channels):
        threading.Thread.__init__(self)
        self.redis = redis.Redis()
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe(channels)

    # TODO assign each listener a set of rules and slack details
    def run(self):
        for item in self.pubsub.listen():
            pass


class Poller(threading.Thread):
    def __init__(self, channel):
        threading.Thread.__init__(self)
        self.redis = redis.Redis()
        self.channel = channel

    def poll(self):
        while True:
            r = requests.get('https://redisq.zkillboard.com/listen.php')
            print(json.loads(r.text))
            a = Killmail(json.loads(r.text))
            self.redis.publish(self.channel, a)

    def run(self):
        self.poll()


def main():
    # TODO assign listeners from POSTGRES
    app.add_url_rule('/chat', view_func=ChatAPI.as_view('chat'))
    app.add_url_rule('/listener', view_func=ChatAPI.as_view('chat'))
    app.run(debug=True, port=5000)
    # c1 = Listener(['kills'])
    # c1.start()

    # poller = Poller('kills')
    # poller.start()


main()
