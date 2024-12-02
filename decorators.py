import logging
import time
from functools import wraps

# Configure logging
logging.basicConfig(
    filename='model_logs.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def my_logger(orig_func):
    """Decorator to log information about function calls."""
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f"Function '{orig_func.__name__}' called with args: {args}, kwargs: {kwargs}")
        result = orig_func(*args, **kwargs)
        logging.info(f"Function '{orig_func.__name__}' returned {result}")
        return result
    return wrapper

def my_timer(orig_func):
    """Decorator to measure the execution time of functions."""
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = orig_func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Function '{orig_func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper
