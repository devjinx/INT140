

class Person:

    def __init__(self, pid, name, height, weight, eye=None, skin=None, hair=None):
        self._pid = pid
        self._name = name
        self.height = height
        self.set_weight(weight)
        self._eye = eye
        self._skin = skin
        self._hair = hair

    @property
    def pid(self):
        return self._pid

    @property
    def bmi(self):
        return self._weight / self._height / self._height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError
        self._height = height

    def get_weight(self):
        return self._weight

    def set_weight(self, weight):
        if weight <= 0:
            raise ValueError
        self._weight = weight

    def __repr__(self):
        return (f"Person({self._pid},'{self._name}', {self._height}, "
                f"{self._weight}, {self._eye}, {self._skin}, {self._hair})")

    def __eq__(self, other):
        return type(self) is type(other) and self._name == other._name


class PersonGroup:
    def __init__(self):
        self._group = {}  # pid, Person

    def add(self, person):
        if person.pid in self._group:
            raise ValueError
        self._group[person.pid] = person

    def remove(self, pid):
        if pid not in self._group:
            raise ValueError
        self._group.pop(pid)

    def find(self, pid):
        if pid not in self._group:
            return None
        return self._group[pid]

    def len(self):
        return len(self._group)

    def __iter__(self):
        return self._GroupIterator(list(self._group.values()))

    class _GroupIterator:
        def __init__(self, group):
            self._list = group
            self._current = 0
            self._end = len(self._list)

        def __iter__(self):
            return self

        def __next__(self):
            if self._current == self._end:
                raise StopIteration
            now = self._list[self._current]
            self._current += 1
            return now

def try_person():
    p = Person(100, "Peter", 1.80, 70)
    #q = eval(repr(p))
    #r = p
    print(p.bmi)
    print(p.height)
    p.height = 2.00
    print(p.height)
    print(p.get_weight())
    p.set_weight(50)
    print(p.get_weight())

def try_personGroup():
    g = PersonGroup()
    g.add(Person(100, "Peter", 1.8, 85, "blue", "white"))
    g.add(Person(291, "Robert", 1.64, 65, skin="yellow"))
    g.add(Person(95, "Tony", 1.52, 49, hair="blonde"))
    g.add(Person(11, "Smith", 1.73, 80, "brown"))
    print(g.len())
    print(g.find(100))
    print(g.find(99))
    g.remove(100)
    print(g.find(100))
    print(" for ------------------")
    for p in g: # iterable: list, dict, tuple, set, range
        print(p)
    print("------------------")
    print(" while -----------")
    it = iter(g)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
    print("=================")

if __name__ == "__main__":
    #try_person()
    try_personGroup()