class Source:
    '''
    defines sources of news
    '''
    sources = []
    def __init__(self,id, name, description,url, category = ""):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category


class Article:
    '''
    defines an articles' properties
    '''
    sources = []
    def __init__(self,source, author,title, description, url, urlToImage, publishedAt):
        self.source = source
        self.author = author
        self.url = url
        self.title = title
        self.description = description
        self.image = urlToImage
        self.date = publishedAt