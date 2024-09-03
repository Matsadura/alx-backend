#!/usr/bin/env python3
""" Contains the class LRUCache """
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system """
    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Adds the 'item' value for the key 'key' """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.move_to_end(key)
            least_key, _ = self.cache_data.popitem(last=False)
            print(f'DISCARD: {least_key}')

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
