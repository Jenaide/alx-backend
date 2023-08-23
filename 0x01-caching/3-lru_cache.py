#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    class object that allows storing and retrieving items
    from dictionary with LRU removel process
    """
    def __init__(self):
        """
        initializing cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        method that adds an item to cache
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                cache_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", cache_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        method that retrieves an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
