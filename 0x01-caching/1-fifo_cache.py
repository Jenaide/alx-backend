#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from base_caching import BaseCaching
from collections import OrderedDict



class FIFOCache(BaseCaching):
    """
    class that reps an object that allows storing
    and retrieving of items from a dictionary.
    """
    def __init__(self):
        """
        Initializing cache
        """
        super().__init__()
        self.cache_data = OrderdDict()

    def put(self, key, item):
        """
        method that adds an item in cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) => BaseCaching.MAX_ITEMS:
            disc_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", disc_key)


    def get(self, key):
        """
        method that retrieves an item by key
        """
        return self.cache_data.get(key, None)
