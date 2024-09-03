#!/usr/bin/env python3
""" Contains the class MRUCache """
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system """
    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Adds the 'item' value for the key 'key' """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)

            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                Most_key, _ = self.cache_data.popitem(last=True)
                print(f'DISCARD: {Most_key}')
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
