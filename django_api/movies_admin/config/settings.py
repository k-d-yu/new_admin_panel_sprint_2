import os

from pathlib import Path

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = ['127.0.0.1']

LOCALE_PATHS = ['movies/locale']

INTERNAL_IPS = ['127.0.0.1']

# Application definition
include(
    'components/application_definition.py',
)

# Database
include(
    'components/database.py',
)

# Password validation
include(
    'components/password_validation.py',
)

# Internationalization
include(
    'components/internationalization.py',
)

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
