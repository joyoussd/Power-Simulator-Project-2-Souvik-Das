# bus.py

class Bus:
    """
    Represents a bus (node) in the network.

    Required:
      - name (str)
      - nominal_kv (float)

    Attributes:
      - name
      - nominal_kv
      - bus_index (unique integer assigned automatically)
    """

    _counter = 0  # class-level counter for unique indices

    def __init__(self, name, nominal_kv):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Bus name must be a non-empty string.")
        if float(nominal_kv) <= 0:
            raise ValueError("Bus nominal_kv must be > 0.")

        self.name = name
        self.nominal_kv = float(nominal_kv)

        self.bus_index = Bus._counter
        Bus._counter += 1

    @classmethod
    def reset_counter(cls):
        cls._counter = 0