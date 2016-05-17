#!env/bin/python

"""Run the app for local development."""

import os

from mctweetface.views import app


if __name__ == '__main__':
    port = os.getenv('PORT') or 4000
    app.run(port=port, debug=True, reloader=True)
