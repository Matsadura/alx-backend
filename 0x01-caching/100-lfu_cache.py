#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """This class LFUCache is a caching system for LFU"""

    def put(self, key, item):
        """
        Add new item while removing the least frequently
        used item, if it exceeds the MAX_ITEMS.
        If there are multiple items with the same
        frequency.
        remove the least recently used one
        """
        if key is None or item is None:
            return
        if not hasattr(self, 'frequency'):
            self.frequency = {}
        if not hasattr(self, 'usage_order'):
            self.usage_order = []

        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self.discard_lfu_item()
            self.cache_data[key] = item
            self.frequency[key] = 0
            self.usage_order.append(key)
        self.frequency[key] += 1
        self.usage_order.append(key)

    def get(self, key):
        """Get item using its key"""
        if key is None or key not in self.cache_data:
            return None
        if not hasattr(self, 'frequency'):
            self.frequency = {}
        if not hasattr(self, 'usage_order'):
            self.usage_order = []
        self.frequency[key] += 1
        self.usage_order.append(key)
        return self.cache_data[key]

    def discard_lfu_item(self):
        """Discard the least frequently used item"""
        min_freq = min(self.frequency.values())
        min_freq_keys = [
            key for key, value in self.frequency.items() if value == min_freq]
        if len(min_freq_keys) > 1:
            for key in self.usage_order:
                if key in min_freq_keys:
                    lfu_key = key
                    break
        else:
            lfu_key = min_freq_keys[0]
        del self.cache_data[lfu_key]
        del self.frequency[lfu_key]
        print("DISCARD: {}".format(lfu_key))

    def update_usage_order(self, key):
        """
        Move the accessed key to the end of
        usage order list
        """
        if key in self.update_usage_order:
            self.usage_order.remove(key)
        self.update_usage_order.append(key)
