import logging

# Possible logging levels: DEBUG, INFO, ERROR, CRITICAL
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Possible modes correspond to the opening modes for files: 'w' (write), 'a'
# (append)
handler = logging.FileHandler("./logging_example.log", mode='w')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)
logger.addHandler(handler)




def main():
    logger.info("Executing main routine")

    # This should raise an exception
    print(a)

if __name__=='__main__':
    try:
        main()
    except Exception:
        logger.error("Error executing main routine", exc_info=True)
