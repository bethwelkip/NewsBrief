# from app import app
import urllib.request, json
from .models import Source, Article
# from .models import Article
# Article = article.Article
# Source = source.Source
api_key = None
base_url = None
article_url = None
def configure_request(app):
    global api_key, base_url , article_url
    api_key = app.config['API_KEY']
    print("##################################",api_key)
    print("##################################",api_key)
    base_url = app.config['BASE_URL_SOURCES']
    print("##################################",base_url)
    article_url = app.config['BASE_URL_ARTICLES']
    print("##################################",article_url)

def get_sources():
    # configure_request(app)
    print("##################################",api_key)
    the_url = base_url.format(api_key)
    print("*************************************",the_url)
    with urllib.request.urlopen(the_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)
        result = None
        if sources_response['sources']:
            result = process_results(sources_response['sources'])
            print(type(result))
    return result

def process_results(sources_list):
    '''
    Function  that processes the results and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''

    source_results = []
    for item in sources_list:
        ide = item.get('id')
        name = item.get('name')
        description = item.get('description')
        url = item.get('url')
        category = item.get('category')
        source_results.append(Source(ide, name, description, url, category))
    return source_results

def get_articles(source):
    # configure_request(app)
    the_url = article_url.format(source,api_key)
    with urllib.request.urlopen(the_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)
        result = None
        if articles_response['articles']:
            result = process_articles(articles_response['articles'])
            print(type(result))
    return result

def process_articles(articles):
    article_results = []
    for item in articles:
        source= item.get('source[\'name\']')
        author = item.get('author')
        description = item.get('description')
        url = item.get('url')
        title = item.get('title')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')
        article_results.append(Article(source, author,title, description, url, urlToImage, publishedAt))
    return article_results

