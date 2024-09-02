import os

from dynaconf import Dynaconf

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


settings = Dynaconf(
    envvar_prefix="PARK",
    root_path=CURRENT_DIR,
    base_dir=CURRENT_DIR,
    settings_files=["settings.toml", ".secrets.toml"],
)
