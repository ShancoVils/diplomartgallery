from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = ['127.0.0.1','0.0.0.0']
DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR/'db.sqlite3',
    }
}