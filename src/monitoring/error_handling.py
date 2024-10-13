import logging

def log_error(error_message):
    logging.error(f'Error: {error_message}')

def handle_exception(e):
    log_error(str(e))

try:
    # Example of a risky operation
    risky_operation = 1 / 0
except Exception as e:
    handle_exception(e)
