#!/usr/bin/env python3
""" Created by Jenaide Sibolie
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class that represents an object that allows storing
    and retrieving items from dictionary
    """
    def put(self, key, item):
        """ method that adds an item in cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item


    def get(self, key):
        """
        method that retrieves an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
