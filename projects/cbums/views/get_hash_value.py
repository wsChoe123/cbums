import hashlib

# hash function : key-streching & solting algorithm
# bycrypt 라이브러리 사용 시 필요 없음.
def get_hash_value(value):
    data = hashlib.sha256()
    solt = "asiefak!@#!E@Q#4kjsdfiaekfaleif"
    data.update((str)(value).encode('utf-8'))
    data.update((str)(solt).encode('utf-8'))
    temp_value = (str)(data.hexdigest())
    for count in range(1000000):
        temp_hash = hashlib.sha256()
        temp_hash.update((temp_value).encode('utf-8'))
        temp_value = (str)(temp_hash.hexdigest())
    return temp_value