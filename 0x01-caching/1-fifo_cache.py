#!/usr/bin/env python3
""" Contains the class FIFOCache """


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Inherits from BaseCaching and is a caching system """
    def put(self, key, item):
        """ Adds the 'item' value for the key 'key' """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print(f'DISCARD: {list(self.cache_data)[0]}')
            del self.cache_data[list(self.cache_data)[0]]
 
    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
