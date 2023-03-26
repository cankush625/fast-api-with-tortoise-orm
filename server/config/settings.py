import os

from server.config.local import LocalSettings
from server.config.production import ProductionSettings


# Create settings based on environment
if os.environ.get("IS_PRODUCTION_ENVIRONMENT", True) in ("True", "true"):
    settings = ProductionSettings()
else:
    settings = LocalSettings()
