from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60 
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY", cast=str, 
				default="8267343f61522a153a2e21b3c509f0ee81e6c2e7783465f245742fbfc38df342")
