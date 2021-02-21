import logging
class BaseLogging:
    def get_logging(self):
        fm="%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
        logging.basicConfig(level=logging.INFO,filename="./log/zmazon.log",format=fm)
        return logging


