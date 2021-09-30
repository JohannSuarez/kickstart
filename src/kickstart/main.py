"""
Example Driver code
"""
# standard lib
import argparse

# package
from kickstart import Config
from kickstart.logger import pkg_logger as pl

# create the logger at module level
logger = pl.Logger().get_logger()


def run() -> None:
    """
    Example function to execute through poetry scripts
    """
    parser = argparse.ArgumentParser(
        prog="kickstart",
        usage="%(prog)s [options]",
        description="Example package",
        allow_abbrev=False,
    )
    parser.add_argument(
        "-r",
        "--run",
        action="store_true",
    )

    args = parser.parse_args()
    if args.run:
        logger.debug('Received -r as a command line argument')

    try:
        logger.info("APP_ENV: %s :: package name: %s@%s",
                    Config.env(), Config.package(), Config.version())
    except KeyError as error:
        logger.error(
            'Could not find %s in .env file. Please consult the README', error)
        logger.info('Testing for %s@%s', Config.package(), Config.version())
        logger.debug('Testing for %s@%s', Config.package(), Config.version())
        logger.warning('Testing for %s@%s', Config.package(), Config.version())
        logger.error('Testing for %s@%s', Config.package(), Config.version())
