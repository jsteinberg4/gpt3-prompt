import json
import logging
import os

from flask import Flask

from com.jsteinberg4.api.gpt_controller import GptController

LOGGER = logging.getLogger(__name__)
#logging.basicConfig(filename=f"{__name__}.log", filemode='a+', level='DEBUG')

# Load secrets in global scope
SECRET_KEY = os.getenv("OPENAI_SECRET_KEY", None)
if SECRET_KEY is None:
    raise EnvironmentError("Missing API key in environment. Try running with `OPENAI_SECRET_KEY=<key> ...`")

def create_app(test_config = None):
    # Create and configure app
    LOGGER.info("Creating Flask app with name: %s" % __name__)
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        LOGGER.info("Configuring Flask.app from config.py")
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        LOGGER.info("Configuring Flask.app from mapping: %s" % test_config)
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    GptController.register(app)

    return app
