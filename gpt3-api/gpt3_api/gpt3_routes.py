from flask import current_app, Flask
from markupsafe import escape

from gpt3_api import SECRET_KEY
from gpt3_api.chatbot import ChatBot

def init_app(app:Flask) -> None:

    @app.route("/prompt/<string:prompt>", methods=["GET"])
    def send_prompt(prompt: str):
        # Do some gpt stuff
        bot = ChatBot(SECRET_KEY)
        response = bot.prompt(escape(prompt))
        del bot
        return response

