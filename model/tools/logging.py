
import logging
import sys

class Logger:
    logging.baseicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)s %(levelname)5s %(message)s',
        encoding="UTF-8",
        handlers=[

            logging.streamhandler(sys.stdout),
        ]
    )
    @classmethod
    def info(cls, message):
        logging.info(message)


    @classmethod
    def error(cls, message):
        logging.error(message)
