import os
import environ

from backend.conf.common import *

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
