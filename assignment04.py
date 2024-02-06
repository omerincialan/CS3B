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
    
class Input:
    def __init__(self, owner):
        if not isinstance(owner, LogicGate):
            raise TypeError("Owner must be a LogicGate instance")
        self._owner = owner
        self._value = None  # Initially, there's no value

    @property
    def owner(self):
        return self._owner

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = bool(new_value)  # Convert new_value to boolean
        self._owner.evaluate()  # Trigger gate evaluation when input value changes

    def __str__(self):
        return str(self._value) if self._value is not None else "(no value)"

class Output:
    def __init__(self):
        self._value = None
        self._connections = []  # For extra credit

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = bool(new_value)  # Convert new_value to boolean
        # For extra credit: Update connected inputs
        for input_ in self._connections:
            input_.value = self._value

    def __str__(self):
        return str(self._value) if self._value is not None else "(no value)"

    # For extra credit: Method to connect this output to another gate's input
    def connect(self, input_):
        if not isinstance(input_, Input):
            raise TypeError("Can only connect to an Input instance")
        if input_ not in self._connections:
            self._connections.append(input_)
            input_.value = self._value  # Update the input value immediately if this output has a value

