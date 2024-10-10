import logging
from datetime import datetime

class DailyMessageLogger:
  """
  A class for logging messages and function calls with daily log files.
  """

  def __init__(self, log_dir="logs"):
    """
    Initializes the logger with a log directory.
    """
    self.log_dir = log_dir
    self.get_logger()

  def get_logger(self):
    """
    Creates or retrieves a logger for the current date.
    """
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = f"{self.log_dir}/{today}.log"
    handler = logging.FileHandler(log_file, mode="a")  # Append to existing file
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    self.logger = logging.getLogger(today)
    self.logger.addHandler(handler)
    self.logger.setLevel(logging.INFO)  # Adjust logging level as needed

  def log_message(self, message, level=logging.INFO):
    """
    Logs a message with the specified level.
    """
    self.logger.log(level, message)

  def log_function_entry(self, function_name):
    """
    Logs the entry of a function.
    """
    self.log_message(f"Entering function: {function_name}", logging.DEBUG)

  def log_function_exit(self, function_name):
    """
    Logs the exit of a function.
    """
    self.log_message(f"Exiting function: {function_name}", logging.DEBUG)

# Example usage
logger = DailyMessageLogger()
logger.log_message("Project started")