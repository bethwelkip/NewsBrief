class Source:
    '''
    defines sources of news
    '''
    sources = []
    def __init__(self,name, description,url, category):
        self.name = name
        self.description = description
        self.url = url
        self.category = category
