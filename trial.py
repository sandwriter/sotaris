from problem import abstract_problem


class Trial(object):
    def __init__(self, problem):
        if not isinstance(problem, abstract_problem.AbstractProblem):
            raise ValueError("problem: {} is not AbstractProblem type".format(problem))
        self._problem = problem

    def run(self):
        print("Puzzle phrase: {}".format(self._problem.render()))
        self._problem.accept(input("Input your solution [case-sensitive]: "))
        self._problem.save()
