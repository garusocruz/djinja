from .settings import *  # noqa
import warnings

warnings.filterwarnings("ignore")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"
    }
}
