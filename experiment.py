import random

from problem import anagram_problem_factory
import trial


class Experiment(object):
    def __init__(self, user_id, is_perfectionist, num_trial, problem_type, store):
        self._user_id = user_id
        self._is_perfectionist = is_perfectionist
        self._num_trial = num_trial
        if problem_type != "anagram":
            raise ValueError("invalid problem type: {}".format(problem_type))
        self._problem_type = problem_type
        self._store = store

    def run(self):
        if self._problem_type == "anagram":
            factory = anagram_problem_factory.AnagramProblemFactory(self._store)

        for i in range(self._num_trial):
            problem = factory.generate(self._user_id, self._is_perfectionist, random.randint(1, 4))
            t = trial.Trial(problem)
            t.run()
