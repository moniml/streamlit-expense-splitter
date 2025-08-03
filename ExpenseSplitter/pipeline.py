class Pipeline:
    def __init__(self):
        self.steps = []

    def add_step(self, func):
        self.steps.append(func)

    def run(self, data):
        for step in self.steps:
            data = step(data)
        return data
