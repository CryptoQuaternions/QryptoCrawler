from binance.exceptions import BinanceAPIException, BinanceRequestException
from binance.client import Client
from .exchange import Exchange
import logging
import ccxt

class Binance(Exchange):
    def __init__(self, api_key: str, api_secret: str):
        # Call base class constructor
        super().__init__("Binance", api_key, api_secret)

        # Initialize socket client 
        logging.debug("Initializing socket client for Binance")
        try:
            self.socket_client = Client(api_key, api_secret)
            logging.info("Binance socket client for initialized successfully")
        except BinanceRequestException:
            logging.critical('Caught Binance request exception, no JSON returned')
        except BinanceAPIException as e:
            logging.critical('Caught Binance API exception! - Status code %s', e.status_code)
            logging.critical('Message: %s - Code: %s', e.message, e.status_code)

        # Initialize REST Client 
        logging.debug("Initializing REST Client for Binance")
        try:
            self.rest_client = ccxt.binance({'apiKey' : self.api_key, 'apiSecret' : self.api_secret})
            logging.info("Binance REST Client for initialized successfully")
        except BinanceRequestException:
            logging.critical('Caught Binance request exception, no JSON returned')
        except BinanceAPIException as e:
            logging.critical('Caught Binance API exception! - Status code %s', e.status_code)
            logging.critical('Message: %s - Code: %s', e.message, e.status_code)

    def download_historical_data(self):
        pass

    def close(self):
        pass