from app import app
import urllib.request, json
from .sourcemodel import source
Source = source.Source
api_key = app.config['API_KEY']
base_url = app.config['BASE_URL_SOURCES']

def get_sources():
    the_url = base_url.format(api_key)

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
        name = item.get('name')
        description = item.get('description')
        url = item.get('url')
        category = item.get('category')
        source_results.append(Source(name, description, url, category))
    return source_results