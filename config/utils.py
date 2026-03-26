import os
import logging
from datetime import datetime
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    value = os.getenv(key, default)
    if value is None:
        logger.warning(f"Environment variable '{key}' not found and no default provided.")
    return value

def validate_config(config: Dict[str, Any], required_keys: list) -> bool:
    missing_keys = [key for key in required_keys if key not in config]
    if missing_keys:
        logger.error(f"Missing required configuration keys: {', '.join(missing_keys)}")
        return False
    return True

def format_timestamp(timestamp: datetime) -> str:
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")

def ensure_directory_exists(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)
        logger.info(f"Created directory: {path}")

def sanitize_input(input_str: str) -> str:
    return input_str.strip().replace("\n", "").replace("\r", "")