import configparser
import codecs
# Create a ConfigParser object
# Open the configuration file with UTF-8 encoding
def configRead():
    try:
        with codecs.open('config.txt', 'r', encoding='utf-8') as file:
            config = configparser.ConfigParser()
            config.read_file(file)

        # Access configuration parameters
        app_name = config.get('Credits', 'app_name')
        app_version = config.get('Credits', 'app_version')

        max_retries_fe = int(config.get('General', 'max_retries_fe'))
        max_retries_nc = int(config.get('General', 'max_retries_nc'))
    except:
        return None
    finally:
        pass
    return max_retries_fe, max_retries_nc

def ReadEndPointProData():
    try:
        with codecs.open('config.txt', 'r', encoding='utf-8') as file:
            config = configparser.ConfigParser()
            config.read_file(file)
        endPointPro = int(config.get('Endpoint', 'urlPro'))
        userPro = int(config.get('Endpoint', 'userPro'))
        passPro = int(config.get('Endpoint', 'passPro'))
    except:
        return None
    finally:
        pass
    return endPointPro, userPro, passPro

def ReadEndPointProData():
    try:
        with codecs.open('config.txt', 'r', encoding='utf-8') as file:
            config = configparser.ConfigParser()
            config.read_file(file)
        endPointPro = str(config.get('EndpointPro', 'urlPro'))
        userPro = str(config.get('EndpointPro', 'userPro'))
        passPro = str(config.get('EndpointPro', 'passPro'))
    except:
        return None
    finally:
        pass
    return endPointPro, userPro, passPro

def ReadEndPointDemoData():
    try:
        with codecs.open('config.txt', 'r', encoding='utf-8') as file:
            config = configparser.ConfigParser()
            config.read_file(file)
        endPointDemo = str(config.get('EndpointDemo', 'urlDemo'))
        userDemo = str(config.get('EndpointDemo', 'userDemo'))
        passDemo = str(config.get('EndpointDemo', 'passDemo'))
        NumeroAutorizacion=str(config.get('EndpointDemo', 'passDemo'))
    except:
        return None
    finally:
        pass
    return endPointDemo, userDemo, passDemo