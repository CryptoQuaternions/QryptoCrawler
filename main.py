from datetime import datetime
import logging
import yaml

if __name__ == "__main__":

    # Config loading
    with open("config.yaml", "r") as yamlfile:
        cfg = yaml.load(yamlfile, Loader=yaml.FullLoader)

    # Load the logging settings
    folder = cfg['logging']['folder']
    prefix = cfg['logging']['prefix']
    timeformat = cfg['logging']['timeformat']

    # Logging setup
    logfile_name = folder + prefix + datetime.now().strftime(timeformat) + '.log'
    logging.basicConfig(filename=logfile_name, level=logging.DEBUG)