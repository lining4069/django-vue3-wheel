import datetime
import os
import environ

from conf.common import *

# 设置系统日志存储路径
logger_dir = os.path.join(BASE_DIR, 'loggers')
if not os.path.exists(logger_dir):
    os.makedirs(logger_dir)

# 设置系统文件存储文件夹
appfiles_path = os.path.join(BASE_DIR, 'appfiles')
if not os.path.exists(appfiles_path):
    os.makedirs(appfiles_path)

# 设置django文件存储配置，按需设置非必需

# 从系统部署环境变量中根据APP_ENV 处理系统读取那个环境配置变量
env_filename = ".env.%s" % os.environ.get("APP_ENV", "prod")  # 默认读取prod的配置信息
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, f"env/{env_filename}"))

BACKEND_DATABASE_DB = env.str("backend_database_db")  # 数据库名称
BACKEND_DATABASE_HOST = env.str("backend_database_host")  # 数据库ip
BACKEND_DATABASE_PORT = env.str("backend_database_port")  # 端口号
BACKEND_DATABASE_USER = env.str("backend_database_user")  # 用户名
BACKEND_DATABASE_PASSWORD = env.str("backend_database_password")  # 密码

# 数据库
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": BACKEND_DATABASE_DB,
        "USER": BACKEND_DATABASE_USER,
        "PASSWORD": BACKEND_DATABASE_PASSWORD,
        "HOST": BACKEND_DATABASE_HOST,
        "PORT": BACKEND_DATABASE_PORT
    }
}

# 日志格式和存储配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        "sample": {
            "format": "%(asctime)s %(levelname)s %(message)s"
        },
        "detail": {
            "format": "%(asctime)s %(levelname)s %(message)s Exception %(exc_info)s"
        }
    },
    "filters": {},
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "detail",
        },
        "default": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "detail",
            "filename": os.path.join(logger_dir, f"{datetime.datetime.now().strftime('%Y-%m-%d')}.log"),
            "maxBytes": 1024 * 1024 * 10,
            "backupCount": 5,
            "encoding": "utf8",
        }
    },
    "loggers": {
        "django": {
            "handlers": ["default", "console"],
            "level": "INFO",
            "propagate": False,
        }
    }
}
