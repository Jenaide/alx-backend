#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class that represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
    remova process
    """
    def __init__(self):
        """
        initializing cache
        """
        super().__init__()
        self.cache_data = []

    def put(self, key, item):
        """
        method that adds an item to cache
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                x_key, _ = self.cache_data.popitem(True)
                print("DISCARD: ", x_key)

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        method that retrieves an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
