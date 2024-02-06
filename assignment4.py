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

