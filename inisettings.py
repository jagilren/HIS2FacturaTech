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