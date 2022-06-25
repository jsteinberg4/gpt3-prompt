import json
import logging
import os

from flask import Flask

LOGGER = logging.getLogger(__name__)
#logging.basicConfig(filename=f"{__name__}.log", filemode='a+', level='DEBUG')

# Load secrets in global scope
if os.path.exists("api.properties") and os.path.isfile("api.properties"):
        with open("api.properties") as file:
            for line in file.readlines():
                exec(line)
else:
    raise OSError("File does not exist: api.properties")

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

    from gpt3_api.gpt3_routes import init_app
    init_app(app)
    exec("LOGGER.info('Loaded SECRET_KEY=%s' % SECRET_KEY)")

    return app
