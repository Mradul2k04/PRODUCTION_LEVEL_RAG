from loguru import logger
import sys
from pathlib import Path

# --------------------------------------------------
# Project Root Directory
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

# Logs directory
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

# Log file path
LOG_FILE = LOG_DIR / "app.log"


# --------------------------------------------------
# Remove Default Logger
# --------------------------------------------------
logger.remove()


# --------------------------------------------------
# Console Logger
# --------------------------------------------------
# Prints logs in the terminal
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-HH:mm:ss}</green>|"
    "<level>{level}</level> |"
    "<cyan>{name}</cyan> |"
    "{message}",
    level="INFO"
)

# --------------------------------------------------
# File Logger
# --------------------------------------------------
# Saves logs into logs/app.log
logger.add(
    LOG_FILE,
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    level="DEBUG",
    enqueue=True,
)

# --------------------------------------------------
# Test Message
# --------------------------------------------------
logger.info("Logger initalized successfully")