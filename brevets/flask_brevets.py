"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import logging

import arrow  # Replacement for datetime, based on moment.js
import flask
from flask import request

import acp_times  # brevet time calculations
import config


app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('brevets.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404

@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from km, using rules
    described at https://rusa.org/pages/acp-brevet-control-times-calculator.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)

    app.logger.debug(f"request.args: {request.args}")
    app.logger.debug(f"km={km}")

    #########
    # my changes
    #########
    brevet_dist = request.args.get('brevet_dist', 0, type=int)
    begin_date = request.args.get('begin_date', "", type=str)
    begin_time = request.args.get('begin_time', "", type=str)
    starting_time = arrow.get(begin_date + " " + begin_time, 'YYYY-MM-DD HH:mm')

    # Calculate open and close times and convert them to ISO 8601 format
    open_time = acp_times.open_time(km, brevet_dist, starting_time)
    close_time = acp_times.close_time(km, brevet_dist, starting_time)

    result = {"open": arrow.get(open_time).format('ddd M/D H:mm'), "close": arrow.get(close_time).format('ddd M/D H:mm')}       
  

    return flask.jsonify(result=result)

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    app.logger.info(f"Opening for global access on port {CONFIG.PORT}")
    app.run(port=CONFIG.PORT, host="0.0.0.0", debug=True)
