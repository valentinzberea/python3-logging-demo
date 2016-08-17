import logging

logger = logging.getLogger(__name__)


def test_method():
    logger.debug('DEBUG')
    logger.info('INFO')
    logger.error('ERROR')
