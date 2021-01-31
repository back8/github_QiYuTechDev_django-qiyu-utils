"""
使用方式:

在配置文件中:
```python
from django_qiyu_utils.settings import *
```
"""

import inspect
import os

from .env import EnvHelper

# 只需要导出有用的变量
#
# Django 项目导出的配置项
#
__all__ = [
    "DEBUG",
    "SECRET_KEY",
    "ALLOWED_HOSTS",
    "LANGUAGE_CODE",
    "TIME_ZONE",
    "MEDIA_URL",
    "STATIC_URL",
    "STATIC_ROOT",
    "STATICFILES_DIRS",
]

# 安全警告: 请不要在线上环境打开 DEBUG
DEBUG = False  # 防御性编程 默认不打开 DEBUG
# 只有设置了 DJANGO_DEV|DJANGO_TEST 环境变量, 才打开 DEBUG
if EnvHelper.in_dev() or EnvHelper.in_test():
    DEBUG = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
#
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY", "wr*dd-zawlb)xpzw!hi-jbkene_^sb7oqs4_(e7Tz8yklz49_v"
)

#
# 允许访问的 HOSTS 列表
ALLOWED_HOSTS = ["*"]
# 多个域名使用 ';' 分隔
hosts = os.getenv("DJANGO_ALLOWED_HOSTS", None)
if isinstance(hosts, str) and hosts != "":
    ALLOWED_HOSTS = hosts.split(";")
##########################################################

LANGUAGE_CODE = os.getenv("DJANGO_LANGUAGE_CODE", "zh-Hans")

TIME_ZONE = os.getenv("DJANGO_TIME_ZONE", "Asia/Shanghai")

MEDIA_URL = os.getenv("DJANGO_MEDIA_URL", "/media/")

STATIC_URL = os.getenv("DJANGO_STATIC_URL", "/static/")

#################################################################################
# this is ugly hack
frame = inspect.currentframe()
BASE_DIR = os.path.join(os.path.dirname(inspect.getfile(frame.f_back)), "..", "..")

STATIC_ROOT = None
STATICFILES_DIRS = None

MEDIA_ROOT = os.path.join(BASE_DIR, "..", "media")

if DEBUG:
    STATICFILES_DIRS = [
        os.path.normpath(os.path.join(BASE_DIR, "..", "static")),
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "..", "static")
#################################################################################
