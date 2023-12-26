class SimpleRandom:
    def __init__(self, seed):
        self.state = seed

    def generate(self):
        while True:
            self.state = (1103515245 * self.state + 12345) & 0x7FFFFFFF
            yield self.state
