from flask import render_template

from app import app
from .request import get_sources
from .request import get_articles

# home page
@app.route('/')
def index():

     '''
    View root page function that returns the index page and its data
    '''

     title = "Your Everyday News Bank"
     sources = get_sources()
     #news sources array here, passed then for-looped
     return render_template('index.html', title = title, sources = sources)


#articles
@app.route('/articles/<names>')
def articles(names):
     '''
     View root page function that returns the index page and its data
     '''
     name = names 
     print("here")
     articles = get_articles(names)
     return render_template('articles.html', name = names, articles = articles)