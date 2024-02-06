class LogicGate:
    def __init__(self, name):
        self._name = name
        self._output = None  # Will be initialized in child classes

    @property
    def name(self):
        return self._name

    @property
    def output(self):
        return self._output

    def __str__(self):
        # Implement a way to represent the gate's status as a string
        pass

    def evaluate(self):
        # This method will be overridden by child classes to implement specific gate logic
        pass

