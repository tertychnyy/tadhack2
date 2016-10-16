"""
The flask application package.
"""
from werkzeug.wsgi import DispatcherMiddleware
from flask import Flask


bot = Flask(__name__)
application = DispatcherMiddleware(bot)

from views import *


if __name__ == "__main__":
    bot.run()


