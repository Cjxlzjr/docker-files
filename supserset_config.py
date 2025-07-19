import os

from werkzeug.contrib.cache import RedisCache

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': 'redis',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
    'CACHE_REDIS_URL': 'redis://redis:6379/1'}

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://superset:superset@postgres:5432/superset'
SECRET_KEY = 'thisISaSECRET_1234'

SUPERSET_UPDATE_PERMS = 0

class CeleryConfig(object):
    BROKER_URL = 'redis://redis:6379/0'
    CELERY_IMPORTS = (
        'superset.sql_lab', 
        'superset.tasks'
    )
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
    CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}


CELERY_CONFIG = CeleryConfig
RESULTS_BACKEND = RedisCache(
    host='redis',
    port=6379,
    key_prefix='superset_results'
)


import ssl
import urllib3
from urllib3.exceptions import InsecureRequestWarning

# 禁用 SSL 验证和警告
urllib3.disable_warnings(InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

# 设置 urllib 和 requests 的默认行为
import os
os.environ['PYTHONHTTPSVERIFY'] = '0'
os.environ['CURL_CA_BUNDLE'] = ''
os.environ['REQUESTS_CA_BUNDLE'] = ''

# 修改 requests 的默认 SSL 验证
try:
    import requests.adapters
    import urllib3.util.ssl_
    urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
except ImportError:
    pass