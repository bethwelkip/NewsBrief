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
