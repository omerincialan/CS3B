class Input:
    def __init__(self, owner):
        self._owner = owner  # Using a leading underscore for the private attribute
        self._value = None   # Initially, the input value is undefined

    @property
    def owner(self):
        return self._owner

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = bool(new_value)  # Convert the new value to a boolean
        # Trigger the owner gate's evaluation method, if the owner is set
        if self._owner is not None:
            self._owner.evaluate()

class Output:
    def __init__(self):
        self._value = None  # Initially, the output value is undefined
        self._connections = []  # For extra credit: List to hold connected inputs

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = bool(new_value)  # Convert the new value to a boolean
        # For extra credit: Propagate the new value to connected inputs
        for input in self._connections:
            input.value = self._value

    # For extra credit: Method to connect this output to an input
    def connect(self, input_):
        if input_ not in self._connections:
            self._connections.append(input_)
            # Immediately update the connected input's value to match this output's value
            if self._value is not None:
                input_.value = self._value
class LogicGate:
    def __init__(self, name):
        self._name = name
        self._output = Output()  # Every gate has an output

    @property
    def name(self):
        return self._name

    @property
    def output(self):
        return self._output

    def evaluate(self):
        pass  # This method will be overridden by subclasses to implement specific logic

