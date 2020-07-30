import json
from problem import abstract_problem


class AnagramProblem(abstract_problem.AbstractProblem):
    def __init__(self, phrase, potential_solutions, meta, store):
        self._phrase = phrase
        self._potential_solutions = potential_solutions
        self._meta = meta
        self._solution = None
        self._accept = False
        self._store = store

    def render(self):
        return self._phrase

    def accept(self, solution):
        self._solution = solution
        self._accept = solution in self._potential_solutions or (not self._potential_solutions and solution == "N/A")
        return self._accept

    def save(self):
        self._store.save(self)

    def __str__(self):
        return json.dumps({
            "difficulty": self._meta.get("difficulty"),
            "is_perfectionist": self._meta.get("is_perfectionist"),
            "phrase": self._phrase,
            "potential_solutions": self._potential_solutions,
            "solution": self._solution,
            "accept": self._accept
        })
