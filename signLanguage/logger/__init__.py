import logging
import os
from datetime import datetime
from from_root import from_root

# Generate the log file name with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


# # Create the log directory path
# log_dir = os.path.join(from_root(), 'log')

# # Ensure the log directory exists
# os.makedirs(log_dir, exist_ok=True)
# log_path = log
# Create the full log file path
LOG_FILE_PATH = os.path.join("log", LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
