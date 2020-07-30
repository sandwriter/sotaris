from collections import defaultdict
import random

from problem import anagram_problem

DICT_PATH = "/usr/share/dict/words"


class AnagramProblemFactory(object):

    def __init__(self, store):
        self._store = store

        with open(DICT_PATH) as f:
            self._candidates = f.read().splitlines()
        self._preprocess(self._candidates)

    def _preprocess(self, candidates):
        solution_map = defaultdict(list)
        for word in candidates:
            canonical_word = ''.join(sorted(word))
            solution_map[canonical_word].append(word)
        self._solution_map = solution_map

    def generate(self, user_id, is_perfectionist, difficulty):
        filter_fn = self.get_filter_fn(difficulty)
        entry = random.choice(list(filter(filter_fn, self._solution_map.items())))
        phrase = self.shuffle_str(entry[0])
        return anagram_problem.AnagramProblem(
            phrase, entry[1],
            {"difficulty": difficulty, "user_id": user_id, "is_perfectionist": is_perfectionist},
            self._store
        )

    @staticmethod
    def shuffle_str(s):
        s_list = list(s)
        random.shuffle(s_list)
        return ''.join(s_list)

    @staticmethod
    def get_filter_fn(difficulty):
        return lambda entry: (difficulty - 1) * 3 <= len(entry[0]) < difficulty * 3

    def nearest_unsolvable(self, phrase):
        def next_char(c):
            return chr(ord(c) + 1)

        def is_valid_alphabet(c):
            return 'A' <= c <= 'z'

        phrase_chars = list(phrase)
        for index in range(len(phrase)):
            new_char = next_char(phrase_chars[index])
            if is_valid_alphabet(new_char):
                new_phrase = ''.join(sorted(phrase[:index] + [new_char] + phrase[index + 1]))
                if new_phrase not in self._solution_map:
                    return new_phrase
        return ''
