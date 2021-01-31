#!/usr/bin/env python
# coding: utf-8


class HashMap:
    """
    Entry inside HashMap
    """

    class Entry:
        def __init__(self, key, value):
            """
            An Entity that stores key-value pairs
            :param key
            :param value 
            """
            self._key = key
            self._value = value

        def get_key(self):
            #  return key
            return self._key

        def get_value(self):
            #  return value
            return self._value

        def __eq__(self, other):
            #  comparsion function
            return self._key == other.get_key()

        def set_value(self, value):
            # value setter
            self._value = value

    class ItemIterator:
        def __init__(self, hash_map, keys):
            self.hash_map = hash_map
            self.keys = keys
            self.seek = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.seek < len(self.keys):
                self.seek += 1
                return self.keys[self.seek - 1], self.hash_map.get(self.keys[self.seek - 1])
            else:
                raise StopIteration

    class ValueIterator(ItemIterator):
        def __next__(self):
            if self.seek < len(self.keys):
                self.seek += 1
                return self.hash_map.get(self.keys[self.seek - 1])
            else:
                raise StopIteration

    class KeyIterator(ItemIterator):
        def __next__(self):
            if self.seek < len(self.keys):
                self.seek += 1
                return self.keys[self.seek - 1]
            else:
                raise StopIteration

    def __init__(self, bucket_num=64):
        """
        Implementing the chaining method
        :param bucket_num: number of buckets on initialization
        """
        self.size = bucket_num
        self.hash_map = [[] for _ in range(self.size)]
        self.elem_num = 0
        self.keys_list = []
        self.LOAD_K = 0.66
        self.INCREASE = 2

    def get(self, key, default_value=None):
        #  value getter
        #  if exists - returns this value, else default_value
        ind = self._get_index(self._get_hash(key))
        for entry in self.hash_map[ind]:
            if key == entry.get_key():
                return entry.get_value()
        return default_value

    def put(self, key, value):
        #  value setter by key 
        #  if key exist replace current value
        ind = self._get_index(self._get_hash(key))
        for entry in self.hash_map[ind]:
            if entry.get_key() == key:
                entry.set_value(value)
                return None
        self.hash_map[ind].append(self.Entry(key, value))
        self.elem_num += 1
        self.keys_list.append(key)
        if self.elem_num > self.LOAD_K * self.size:
            self._resize()

    def __len__(self):
        # Returns Entry count in array
        return self.elem_num

    def _get_hash(self, key):
        #  Return the hash from the key
        #  used to put it in the bucket 
        return hash(key)

    def _get_index(self, hash_value):
        #  By hash value, return the index of the element in the array
        return hash_value % self.size

    def values(self):
        #  return an iterator of values
        return self.ValueIterator(self, self.keys_list)

    def keys(self):
        #  return an iterator of keys
        return self.KeyIterator(self, self.keys_list)

    def items(self):
        #  return an iterator of key plus value (tuples)
        return self.ItemIterator(self, self.keys_list)

    def _resize(self):
        #  hashmap resize
        self.size *= self.INCREASE
        old_elem_num = self.elem_num
        self.elem_num = 0
        self.keys_list = []
        old_data = self.hash_map
        self.hash_map = [[] for _ in range(self.size)]
        for bucket in old_data:
            for entry in bucket:
                self.put(entry.get_key(), entry.get_value())
        self.elem_num = old_elem_num

    def __str__(self):
        #  print "buckets: {}, items: {}"
        return f'buckets: {self.size}, items: {self.elem_num}'

    def __contains__(self, item):
        #  Check if there is an object (via "in")
        return item in self.keys_list
