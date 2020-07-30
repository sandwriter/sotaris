class AbstractProblem(object):
    def render(self):
        raise NotImplementedError()

    def accept(self, solution):
        raise NotImplementedError()

    def save(self):
        raise NotImplementedError()
