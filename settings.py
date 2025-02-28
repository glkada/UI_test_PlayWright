import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """
    This class represents the project level settings.
    """
        # Path of base directory
    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))

    # Default timeout
    DEFAULT_TIMEOUT: int = 10000

    # QA Link
    HOST: str = os.getenv('PLAYWRIGHT_EXP_APP_HOSTNAME')

    # QA Password
    HOST_PASSWORD: str = os.getenv("PLAYWRIGHT_EXP_APP_PASSWORD")
