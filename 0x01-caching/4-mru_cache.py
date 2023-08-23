#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    class that represents an object tht allows for storing and retrieving
    of items from a dictionary with MRU removel process
    """
    def __init__(self):
        """
        Initializing cache
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
                mru_keys, _ = self.cache_data.popitem(False)
                print("DISCARD: ", mru_keys)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key]= item

    def get(self, key):
        """
        method that retrieves an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
