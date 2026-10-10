# logger.py
import logging
from pathlib import Path


def setup_logger(app_name: str, log_filename: str = "app.log"):
    """Configures and returns a logger that outputs to both a file and the console."""

    log_dir = Path(__file__).resolve().parent.parent / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / log_filename

    logger = logging.getLogger(app_name)
    logger.setLevel(logging.DEBUG)

    # Prevent adding duplicate handlers if setup is called multiple times
    if not logger.handlers:
        # File Handler (captures DEBUG level and above)
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)

        # Console Handler (captures INFO level and above for terminal output)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Define log format
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger