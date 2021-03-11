import os

try:
    IGDB_CLIENT_ID = os.environ['IGDB_CLIENT_ID']
    IGDB_CLIENT_SECRET = os.environ['IGDB_CLIENT_SECRET']
    OAUTH_URL = os.environ['OAUTH_URL']
except KeyError:
    raise RuntimeError("Enviroment has not been initialized! Please run: source set_env.sh")
