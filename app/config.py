class Config:
    '''
    General configuration parent class
    '''
    BASE_URL = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'
    BASE_URL_SOURCES = 'https://newsapi.org/v2/sources?apiKey={}'


class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    DEBUG = True