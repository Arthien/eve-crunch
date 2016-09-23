from flask import render_template
from flask import request
from flask.views import MethodView

class ChatAPI(MethodView):
    def get(self):
        return render_template('chat.html')

    def post(self):
        if request.form:
            form = request.form
            try:
                kid = form['key']
                vcode = form['vcode']
            except KeyError:
                return'Invalid Key or vCode'
            return 
        return render_template('chat.html')