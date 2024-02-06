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
class NotGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input = Input(self)  # Create an Input instance owned by this gate
        self._output = Output()  # Initialize the output

    @property
    def input(self):
        return self._input

    def evaluate(self):
        if self._input.value is not None:  # Check if the input has a value
            self._output.value = not self._input.value  # Set the output to the opposite of the input value

    def __str__(self):
        return f"Gate '{self.name}': input={self._input}, output={self._output}"
class AndGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input0 = Input(self)  # First input
        self._input1 = Input(self)  # Second input
        self._output = Output()

    @property
    def input0(self):
        return self._input0

    @property
    def input1(self):
        return self._input1

    def evaluate(self):
        if self._input0.value is not None and self._input1.value is not None:
            # Perform AND operation and set the output
            self._output.value = self._input0.value and self._input1.value

    def __str__(self):
        return f"Gate '{self.name}': input0={self._input0}, input1={self._input1}, output={self._output}"
class OrGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input0 = Input(self)
        self._input1 = Input(self)
        self._output = Output()

    def evaluate(self):
        if self._input0.value is not None and self._input1.value is not None:
            self._output.value = self._input0.value or self._input1.value

class XorGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)
        self._input0 = Input(self)
        self._input1 = Input(self)
        self._output = Output()

    def evaluate(self):
        if self._input0.value is not None and self._input1.value is not None:
            self._output.value = self._input0.value != self._input1.value

