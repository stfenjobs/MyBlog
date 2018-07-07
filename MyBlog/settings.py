"""
Django settings for MyBlog project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

from celery.schedules import crontab

# 这里使用gettext_lazy代替gettext，是为了防止循环引入
# from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))  # 这里需要把项目根目录下的apps设置为包搜索目录
sys.path.append(os.path.join(BASE_DIR, 'apps', 'agent', 'robot'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!w5xi_5(*j!1blz^&(_jrsjui@x)q44lfmn3-zz&m7@ja7zsmo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'guardian',
    'bloguser',
    'django_filters',
    'rest_framework',
    'social_django',
    'haystack',
    'elasticstack2',
    'whooshstack',
    'captcha',
    'kindeditor',
    'mdeditor',
    'mptt',
    'pure_pagination',
    'blog',
    'comment',
    'oper',
    'agent',
    'import_export'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware', #这里不做国际化与本地化支持
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'blog.context_processors.post_extra'
            ],
        },
    },
]

WSGI_APPLICATION = 'MyBlog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'myblog',
            'HOST': '127.0.0.1',
            'PASSWORD': 'Jennei0122?',
            'USER': 'root',
        }
    }

AUTHENTICATION_BACKENDS = (
    'bloguser.backends.UserBackend.UserBackend',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.weibo.WeiboOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

AUTH_USER_MODEL = 'bloguser.UserProfile'

SOCIAL_AUTH_PIPELINE = (
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    'social_core.pipeline.social_auth.social_details',

    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    'social_core.pipeline.social_auth.social_uid',

    # Verifies that the current auth process is valid within the current
    # project, this is where emails and domains whitelists are applied (if
    # defined).
    'social_core.pipeline.social_auth.auth_allowed',

    # Checks if the current social-account is already associated in the site.
    'social_core.pipeline.social_auth.social_user',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    'social_core.pipeline.user.get_username',

    # Send a validation email to the user to verify its email address.
    # Disabled by default.
    # 'social_core.pipeline.mail.mail_validation',

    # Associates the current social details with another user account with
    # a similar email address. Disabled by default.
    # 'social_core.pipeline.social_auth.associate_by_email',

    # Create a user account if we haven't found one yet.
    'social_core.pipeline.user.create_user',

    # 设置用户的头像等
    'bloguser.pipline.save_bloguser_extra_profile',

    # Create the record that associates the social account with the user.
    'social_core.pipeline.social_auth.associate_user',

    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
    'social_core.pipeline.social_auth.load_extra_data',

    # Update the user record with any changed info from the auth service.
    'social_core.pipeline.user.user_details',
)

#线上回调地址 http://example.com/social/complete/github
SOCIAL_AUTH_GITHUB_KEY = '39e547f05b01a85f217f'
SOCIAL_AUTH_GITHUB_SECRET = '71be9131fb2461555c8ebfcd08783833ab0d02ad'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
REGISTER_REDIRECT_URL = '/'  # 自定义
LOGIN_URL = '/account/login/'

EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '303288346@qq.com'
EMAIL_HOST_PASSWORD = 'qjisygavtvktbggi'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = '303288346@qq.com'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_SUBJECT_PREFIX = '[MyBlog]'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6  # 密码长度最少要是6位
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True  # 这里不做国际化与本地化翻译

USE_L10N = True

USE_TZ = False  # 这里使用本地时区

# LANGUAGES = [
#     ('en', _('English')),
#     ('ja', _('Japanese')),
#     ('zh-hans', _('Simplified Chinese')),
#     ('zh-hant', _('Traditional Chinese')),
# ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static/")]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

SITE_ID = 1

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        "KEY_PREFIX": "MYBLOG"
    }
}

# see https://django-haystack.readthedocs.io/en/v2.8.1/tutorial.html#configuration
# 这里改用elasticsearch搜索引擎，Whoosh实测性能较低。
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'elasticstack2.backends.ConfigurableElasticSearchEngine',
        # 'whooshstack.backends.WhooshEngine'
        'URL': 'http://127.0.0.1:9200/',  # 'PATH': os.path.join(BASE_DIR, 'apps/whooshstack/whoosh_index'),
        'INDEX_NAME': 'haystack',
        'INCLUDE_SPELLING': True,
        'DEFAULT_ANALYZER': 'ik',  # ES自定义设置 see http://elasticstack.readthedocs.io/en/latest/mappings.html#chaning-the-default-analyzer
        'DEFAULT_NGRAM_SEARCH_ANALYZER': 'ik_smart', # ES自定义设置
        'DEFAULT_NGRAM_INDEX_ANALYZER': 'ik'        # ES自定义设置
    },
}
# 'haystack.signals.RealtimeSignalProcessor' 在博文保存，删除时自动更新索引
HAYSTACK_SIGNAL_PROCESSOR = 'blog.signals.PostSignalProcessor'  # 在博文状态发生变化时更新索引

# 博文分页形式设置 1 2... 3 4 5 6 7 ... 8 9
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 5,
    'MARGIN_PAGES_DISPLAYED': 2,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_TIMEZONE = TIME_ZONE
CELERY_ENABLE_UTC = USE_TZ
# 这里写1保持celery工作线程只有一个， why?
# The Twisted reactor cannot be restarted, so once one spider finishes running
# and crawler stops the reactor implicitly, that worker is useless.
# 所以为了实现重启reactor,可以换成每次重新启动一个worker来实现。
# see https://stackoverflow.com/questions/22116493/run-a-scrapy-spider-in-a-celery-task
CELERYD_MAX_TASKS_PER_CHILD = 1
CELERY_BEAT_SCHEDULE = {
    "sync-cache-unread-to-db": {
        'task': 'oper.tasks.sync_n_unread',
        'schedule': 60.0
    },
    "post-crawler": {
        'task': 'agent.tasks.post_crawler',
        'schedule': crontab(minute=0, hour=0)  # 每天凌晨十二点执行
    }
}
CELERY_BEAT_MAX_LOOP_INTERVAL = 1
# CELERY_WORKER_HIJACK_ROOT_LOGGER = False
# there was a bug in django-celery-beat may be caused periodic tasks be run in microseconds.
# CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'standard': {
            'format': '%(asctime)s %(levelname)s [%(name)s: %(lineno)s] -- %(message)s'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'task': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'standard'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'oper.tasks': {
            'handlers': ['console', 'task'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

ADMINS = [('Jennei', 'jennei@hotmail.com'), ('RenKang', 'rk19931211@hotmail.com'), ('Nico', '303288346@qq.com')]
