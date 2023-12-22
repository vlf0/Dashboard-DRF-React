import environ

# Get root dir of the project
root = environ.Path(__file__) - 3
env = environ.Env()
# Reading .env file
environ.Env.read_env()


DATABASES = {'default': env.db('DB_LITE_URL')}
