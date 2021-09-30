"""
Example Driver code
"""
# standard lib

# package
from kickstart import Config
from kickstart.logger import pkg_logger as pl

# create the logger at module level
logger = pl.Logger().get_logger()


def run() -> None:
    """
    Example function to execute through poetry scripts
    """
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
