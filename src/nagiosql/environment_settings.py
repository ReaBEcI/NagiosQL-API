# Copyright 2012 NagiosQL-API authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

#
# configuracao para database do nagiosql
#

import sys
TESTING = len(sys.argv) == 1 or sys.argv[1] in ['test', 'jenkins']
if TESTING:
    print "Running in testing mode"

if TESTING:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'nagiosql.sql',                      # Or path to database file if using sqlite3.
#            'USER': 'nagios',                      # Not used with sqlite3.
#            'PASSWORD': 'nagiosql320',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'nagiosql',                      # Or path to database file if using sqlite3.
            'USER': 'nagios',                      # Not used with sqlite3.
            'PASSWORD': 'nagiosql320',                  # Not used with sqlite3.
            'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
            'OPTIONS': {
                "init_command": "SET storage_engine=INNODB, SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED" 
                }
        }
    }

# 
# varivel do ambiente do nagiosql 
#
NAGIOSQL = "localhost"


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(module)s] %(message)s'
        }
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {

        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': { # Stop SQL debug from logging to main logger
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.db.backends': {
             'handlers': ['console'],  # Quiet by default!
             'propagate': False,
             'level':'DEBUG',
        },
        'requests': {
            'level': 'WARN'
        },
    }
}