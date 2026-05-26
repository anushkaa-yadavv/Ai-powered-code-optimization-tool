import hashlib


class CacheManager:

    _cache = {}

    @staticmethod
    def hash(code):
        return hashlib.md5(code.encode()).hexdigest()

    @classmethod
    def get(cls, key):
        return cls._cache.get(key)

    @classmethod
    def set(cls, key, value):
        cls._cache[key] = value