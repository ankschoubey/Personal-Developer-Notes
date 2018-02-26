import logging
import os

# prints log to stdout and also saves to specified log file
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def directory_maker(path): # makes directory if path does not exists
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_logger(module_path, file_name = 'execution.log'):
    module_path = module_path.split('/')

    name = module_path[-1]
    current_directory = '/'.join(module_path[:-1])

    directory =  current_directory+'/Logs/'
    directory_maker(directory)
    print(current_directory+'execution.log')
    logging.basicConfig(filename = directory+'execution.log', format = LOG_FORMAT, level=logging.DEBUG)

    logger = logging.getLogger(name)
    return logger


logger = get_logger(__file__)
logger.info("This is information.")
# logger.error("This is Error!")
# logger.debug("This is debug...")
