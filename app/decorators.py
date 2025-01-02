import logging
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.INFO)

def log_file_upload(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Extract the filename from the UploadFile parameter
        file = kwargs.get('file')
        if file:
            logging.info(f"File uploaded: {file.filename}")
        return await func(*args, **kwargs)
    return wrapper
