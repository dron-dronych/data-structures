class HashTable:
    def __init__(self, m):
        self.m = m
        self.buckets = [None] * m

    def add(self, s):
        hash_val = self.calculate_hash(s)

        if self.buckets[hash_val] is None:
            self.buckets[hash_val] = []

        if s not in self.buckets[hash_val]:
            bucket = self.buckets[hash_val]
            bucket.insert(0, s)

    def delete(self, s):
        hash_val = self.calculate_hash(s)

        if s in self.buckets[hash_val]:
            drop_id = self.buckets[hash_val].index(s)
            self.buckets[hash_val].pop(drop_id)

    def find(self, s):
        hash_val = self.calculate_hash(s)

        if s in self.buckets[hash_val]:
            return s

    def check(self, i):
        return self.buckets[i]

    def calculate_hash(self, s):
        p = 1_000_000_007
        x = 263

        components = [ord(s[i]) * (x ** i) % p for i in range(len(s))]

        return sum(components) % self.m
