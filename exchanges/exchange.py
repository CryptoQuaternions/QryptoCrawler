import logging

class Exchange:
    # API Clients
    __rest_client = None
    __socket_client = None

    name = None

    def __init__(self, name: str, api_key: str, api_secret: str):
        logging.debug("Creating exchange with name: %s", name)
        self.name = name
        self.__api_key = api_key
        self.__api_secret = api_secret
    
    @property
    def api_key(self) -> str:
        return self.__api_key
    
    @api_key.setter
    def api_key(self, value: str):
        logging.debug("API Key being set with value: %s", value)
        self.__api_key = value

    @property
    def api_secret(self) -> str:
        return self.__api_secret
    
    @api_secret.setter
    def api_secret(self, value: str):
        logging.debug("API Secret being set with value: %s", value)
        self.__api_secret = value

    @property
    def rest_client(self):
        return self.__rest_client
    
    @rest_client.setter
    def rest_client(self, value):
        if self.__rest_client is None:
            logging.debug("Rest client being set for %s", self.name)
            self.__rest_client = value
        else:
            logging.warning("Rest client is already set for %s  - This should not happen!", self.name)
    
    @property
    def socket_client(self):
        return self.__socket_client
    
    @socket_client.setter
    def socket_client(self, value):
        if self.__socket_client is None:
            logging.debug("Socket client being set for %s", self.name)
            self.__socket_client = value
        else:
            logging.warning("Socket client is already set for %s - This should not happen!", self.name)

    def close(self):
        logging.warning("Please implement the close function!")

    def __del__(self):
        self.close()