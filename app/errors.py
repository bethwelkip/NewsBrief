from flask import render_template
from . import main_app
@main.app_errorhandler(404)
def four_oh_four(error):
   # return  render_template('fourohfour.html'), 404