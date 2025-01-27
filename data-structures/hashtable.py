# An incomplete hash table implementation.
# (full implementation left for assignment)


def strhash(key):
    # ord converts a character to it's numeric representation
    #   ord("A") == 65
    #   ord("z") == 122
    # etc.
    return sum(ord(letter) for letter in key)


def set_with_linear_probe(ht_storage, key, value):
    """add a key to our hash table using linear probing algorithm"""
    capacity = len(ht_storage)
    index = strhash(key) % capacity

    # search until a space is found
    while True:
        if ht_storage[index] is None:
            # a space has been found, add and exit the loop
            ht_storage[index] = value
            break
        else:
            # move forward looking for space
            index += 1
