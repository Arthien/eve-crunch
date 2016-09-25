from flask import render_template
from flask import request
from flask.views import MethodView

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
                root = etree.fromstring(r.content)
                s = []
                for child in root:
                    s.append(child.tag)
                    s.append(child.attrib)
                return str(s)
            except KeyError:
                return'Invalid Key or vCode'
        return render_template('chat.html')


class ListenHook(MethodView):
    def post(self):
        payload = request.data
        return payload