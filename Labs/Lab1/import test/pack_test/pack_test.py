class ExceptionB(Exception):
    def __init__(self):
        super().__init__()


class Toss:
    def tossb(self):
        return self.toss()

    def toss(self):
        raise ExceptionB()
