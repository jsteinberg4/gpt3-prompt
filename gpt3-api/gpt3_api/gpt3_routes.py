import flask
from flask import current_app, Flask, request
from markupsafe import escape

from gpt3_api import SECRET_KEY
from gpt3_api.chatbot import ChatBot

def init_app(app:Flask) -> None:
    
    @app.route("/hello")
    def hello2():
        print(request.args)
        response = flask.make_response(dict(name="Jesse Steinberg", mood='Frustrated'))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    @app.get("/prompt")
    def send_prompt():
        prompt = request.args['q']
        # Do some gpt stuff
        bot = ChatBot(SECRET_KEY)
        openai_response = bot.prompt(escape(prompt))
        flask_response =  flask.make_response(openai_response, 200)
        flask_response.headers['Access-Control-Allow-Origin'] = '*'
        flask_response.headers['Content-Type'] = 'application/json'

        return flask_response

