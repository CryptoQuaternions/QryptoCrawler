#!/usr/bin/env python3
"""
Bootstrapping script for QryptoCrawler
"""
from exchanges.binance import Binance
from datetime import datetime
import logging
import yaml

def setup_logging(path: str, level: int, console: bool=True, file: bool=True) -> None :
    # Basic logging setup
    logger = logging.getLogger()
    logger.setLevel(level)
    logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    
    # Log to file
    if file:
        fileHandler = logging.FileHandler(path)
        fileHandler.setFormatter(logFormatter)
        logger.handlers.append(fileHandler)
    
    # Log to console
    if console:
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        logger.handlers.append(consoleHandler)

if __name__ == "__main__":

    # Config loading
    with open("config.yaml", "r") as yamlfile:
        cfg = yaml.load(yamlfile, Loader=yaml.FullLoader)    
    with open("api.yaml", "r") as apifile:
        api = yaml.load(apifile, Loader=yaml.FullLoader)
    
    # Load the logging settings
    folder = cfg['logging']['folder']
    prefix = cfg['logging']['prefix']
    timeformat = cfg['logging']['timeformat']

    # Build filepath and setup logging
    logfile_name = folder + prefix + datetime.now().strftime(timeformat) + '.log'
    setup_logging(logfile_name, True, True)

    # Start of script
    logging.info('Current logfile is %s', logfile_name)    
    binance = Binance(api['binance']['key'], api['binance']['secret'])