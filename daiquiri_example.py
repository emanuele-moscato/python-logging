import logging
import daiquiri
import sys

daiquiri.setup(
    level=logging.INFO,
    outputs=(
        daiquiri.output.Stream(sys.stdout),
        daiquiri.output.File(
            "./daiquiri_example.log",
            formatter=daiquiri.formatter.TEXT_FORMATTER
        )
    )
)

logger = daiquiri.getLogger(__name__)

def main():
    print("Hello humans")

    # This is meant to raise an exception
    print(a)

if __name__=='__main__':
    try:
        logger.info("Executing main routine")
        main()
    except Exception:
        logger.error("Error executing main routine", exc_info=True)
