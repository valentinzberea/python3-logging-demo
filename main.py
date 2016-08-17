import logging.config
import yaml

from log_tests import test_method


if __name__ == '__main__':

    logging_config = yaml.load(open('logging.yml', 'r'))
    logging.config.dictConfig(logging_config)

    test_method()
