class InMemoryStore(object):
    def __init__(self):
        self._data = []

    def save(self, problem):
        self._data.append(problem)

    def dump(self):
        return ', '.join(map(lambda problem: str(problem), self._data))
