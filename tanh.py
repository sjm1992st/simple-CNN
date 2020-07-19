import numpy as np
class tanh:
    def __init__(self, input_a):
        self.input_a=input_a
    def activation(self):
        s=np.tanh(self.input_a)
        return s
    def diff_de(self):
        s=1-self.activation()**2
        return s