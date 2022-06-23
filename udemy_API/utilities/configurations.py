import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read(r'udemy_API\utilities\properties.ini')
    return config