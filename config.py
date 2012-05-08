# -*- coding: utf-8 -*-
"""
Configs for default spider
"""

MAX_THREADS = 3
USE_CACHE = True
SAVE_TO_DB = USE_CACHE
CACHE_DB = 'default_project'


def default_spider_params():
    params = {
        'thread_number': MAX_THREADS,
        'network_try_limit': 20,
        'task_try_limit': 20,
    }
    if USE_CACHE:
        params.update({
            'thread_number': 3,
            'use_cache': USE_CACHE,
            'cache_db': CACHE_DB,
            'debug_error': True,
        })
    return params
