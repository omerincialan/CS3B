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

class NotGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input = Input(self)  # NotGate has a single input

    @property
    def input(self):
        return self._input

    def evaluate(self):
        if self._input.value is not None:  # Ensure the input value is set
            self._output.value = not self._input.value  # Invert the input value for the output
class AndGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input0 = Input(self)  # First input for the AND gate
        self._input1 = Input(self)  # Second input for the AND gate

    @property
    def input0(self):
        return self._input0

    @property
    def input1(self):
        return self._input1

    def evaluate(self):
        # Check if both inputs are set
        if self._input0.value is not None and self._input1.value is not None:
            # AND logic: output is True if both inputs are True, False otherwise
            self._output.value = self._input0.value and self._input1.value

