class Cache:
    cache = None

    def get_singleton_cache(self):
        if not Cache.cache:
            Cache.cache = {}
        return Cache.cache

    def add_to_cache(self, key, value):
        self.get_singleton_cache()[key] = value

    def remove_from_cache(self, key):
        if key in self.get_singleton_cache():
            self.get_singleton_cache().pop(key)

    def get_from_cache(self, key):
        return self.get_singleton_cache().get(key)
