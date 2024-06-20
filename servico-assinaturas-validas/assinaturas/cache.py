cache = {}


def add_to_cache(key, value):
    cache[key] = value


def remove_from_cache(key):
    if key in cache:
        del cache[key]


def get_from_cache(key):
    return cache.get(key)


def get_all_cache():
    return cache
