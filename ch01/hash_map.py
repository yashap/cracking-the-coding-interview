class HashMap(object):
  def __init__(self, *entries):
    self._buckets = [[] for _ in range(10)]
    self._MAX_BUCKET_LENGTH = 10
    for key, value in entries:
      self.put(key, value)

  def get(self, key):
    hash_code = hash(key)
    num_buckets = len(self._buckets)
    bucket = self._buckets[hash_code % num_buckets]
    for k, v in bucket:
      if k == key:
        return v
    return None    

  def put(self, key, value):
    hash_code = hash(key)
    num_buckets = len(self._buckets)
    bucket = self._buckets[hash_code % num_buckets]
    value_added = False
    for idx, (k, v) in enumerate(bucket):
      if k == key:
        bucket[idx] = (key, value)
        value_added = True
        break
    if not value_added:
      bucket.append((key, value))
    if len(bucket) > self._MAX_BUCKET_LENGTH:
      self._rebalance()

  def _rebalance():
    prev_buckets = self._buckets
    self._buckets = [[] for _ in range(len(prev_buckets) * 2)]
    for bucket in prev_buckets:
      for key, value in bucket:
        self.put(key, value)
