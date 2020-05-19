from api.app import create_app
<<<<<<< HEAD
from api.config import DevelopmentConfig, ProductionConfig


application = create_app(
    config_object=ProductionConfig)
=======
from api.config import DevelopmentConfig


application = create_app(
    config_object=DevelopmentConfig)
>>>>>>> 0ed582465d48f8120b8ddf1b901da14d3e5c5865


if __name__ == '__main__':
    application.run()
