from flask import render_template

from app import app
from .request import get_sources

# home page
@app.route('/')
def index():

     '''
    View root page function that returns the index page and its data
    '''

     title = "Your One Stop News Site"
     sources = get_sources()
     #news sources array here, passed then for-looped
     return render_template('index.html', title = title, sources = sources)

    