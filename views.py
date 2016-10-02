from flask import render_template
from flask import request
from flask.views import MethodView
from flask_socketio import  emit
from xml.etree import ElementTree as etree

import requests



class ChatAPI(MethodView):
    def get(self):
        return render_template('chat.html')

    def post(self):
        if request.form:
            form = request.form
            try:
                kid = form['key']
                vcode = form['vcode']
                payload = {
                    'vCode': vcode,
                    'keyID': kid
                }
                r = requests.get('https://api.eveonline.com/account/Characters.xml.aspx', params=payload)
                tree = etree.parse(r.content)
                root = tree.getroot()

                return r.content
            except KeyError:
                return'Invalid Key or vCode'
        return render_template('chat.html')


class ListenerAPI(MethodView):
    pass

class BroadcasterAPI(MethodView):
    def get(self):
        return render_template('broadcaster.html')
