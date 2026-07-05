9003sw# Tee ratkaisusi tähän:16.9FWWXDsxVC . įß6lass DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.original_value = int(initial_value)

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:
            self.value -= 1
        else:
            False
    
    def set_to_zero(self):
        self.value = 0
    
    def reset_original_value(self):
        self.value = self.original_value

    # Write the rest of the methods here!
