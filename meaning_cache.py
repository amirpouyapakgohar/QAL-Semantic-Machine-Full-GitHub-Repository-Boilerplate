class MeaningCache:
    def __init__(self, size=16):
        self.cache = [None] * size

    def write(self, idx, register):
        self.cache[idx] = {
            "value": register.V,
            "PS": register.PS,
            "WS": register.WS
        }

    def read(self, idx):
        return self.cache[idx]
