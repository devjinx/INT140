from typing import Union

class Record:
    _all_keys = set()

    def __init__(self, key: int, name: str, value: Union[int, float]):
        if key < 0:
            raise ValueError("invalid")
        if key in Record._all_keys:
            raise ValueError("duplicate")
        self._key = key
        self._name = None
        self.set_name(name)
        self._value = None
        self.set_value(value)
        Record._all_keys.add(key)

    def __str__(self):
        return f"Record(key: {self._key}, name: '{self._name}', value: {self._value})"

    def __eq__(self, other): return self._key == other._key
    def __lt__(self, other): return self._key < other._key
    def __hash__(self): return hash(self._key)

    @classmethod
    def get_all_keys(cls): return cls._all_keys

    @staticmethod
    def cmp_record(r1, r2): return r1._key - r2._key

    @staticmethod
    def cmp_value(r1, r2):
        if r1._value < r2._value: return -1
        if r1._value > r2._value: return 1
        return 0

    def get_key(self): return self._key
    def get_name(self): return self._name
    def get_value(self): return self._value

    def set_name(self, name: str):
        if " " in name or name == "":
            raise ValueError(f"name='{name}' is invalid")
        self._name = name

    def set_value(self, value: Union[int, float]):
        if value < 0.0:
            raise ValueError(f"value={value} cannot be negative")
        self._value = value