"""Create a hashtable."""


class Hash(object):
    """Create a hashtable. Its functions are as follows.
    get(key) - should return the value stored with the given key.
    set(key, val) - should store the given val using the given key.
    _hash(key) - should hash the key provided.
    """

    def __init__(self, size):
        """Instantiates hashtable instance."""
        self._size = size
        self._hashtable = [[] for n in range(size)]

    def _additive_hash(self, key):
        """Hash the key provided using the additive method."""
        hash_total = sum([ord(k) for k in key])
        return hash_total % self._size

    def _fnv_hash(self, key):
        """Hash the key provided using a modified fnv/xor method."""
        hash_total = 2166136261
        for k in key:
            hash_total = (hash_total * 16777619) ^ ord(k)
        return hash_total % self._size

    def set(self, key, value, _hash):
        """Store the given value using the given key."""
        if type(key) is not str:
            raise TypeError("Hash tables can only accept strings.")
        key_hash = self._hash(key)
        bucket = self._hashtable[key_hash]
        if bucket:
            for tup in bucket:
                if tup[0] == key:
                    bucket.remove(tup)
        self._hashtable[key_hash].append((key, value))

    def get(self, key, _hash):
        """Return the value stored with the given key."""
        key_hash = self._hash(key)
        bucket = self._hashtable[key_hash]
        for tup in bucket:
            if tup[0] == key:
                return tup[1]
