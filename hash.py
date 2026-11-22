def hash_func(key, size):
    return key % size

def find(key, arr):
    return hash_func(key, len(arr))  # ищем индекс 

def add(key, arr):
    ind = hash_func(key, len(arr))
    arr[ind] = key

def delete(key, arr):
    ind = hash_func(key, len(arr))
    del arr[ind]

# ключ - значение
def insert(key, val, dct):
    ind = hash_func(key, len(dct))
    dct[ind] = val



