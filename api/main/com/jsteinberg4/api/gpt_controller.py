from flask import current_app, Flask, make_response, request
from markupsafe import escape

from com.jsteinberg4.api.controller import Controller
from com.jsteinberg4.api.chatbot import ChatBot


class GptController(Controller):
    BASE_ROUTE = "/api"

    @classmethod
    def __build_path(cls, path: str) -> str:
        return f"{cls.BASE_ROUTE}/{path}"

    @classmethod
    def register(cls, app: Flask, *args, **kwargs) -> Flask:
        app.add_url_rule(cls.__build_path('/prompt'), view_func=cls._send_prompt, methods=['GET'])
        return app

    @staticmethod
    def _send_prompt():
        prompt = request.args['q']

        bot = ChatBot()
        openai_response = bot.prompt(escape(prompt))

        # Format with cors permissions
        flask_response = make_response(openai_response, 200)
        flask_response.headers['Access-Control-Allow-Origin'] = '*'
        flask_response.headers['Content-Type'] = 'application/json'

        return flask_response
