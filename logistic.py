import numpy as np
class logistic:
    def __init__(self, input_a):
        self.input_a=input_a
    def activation(self):
        s=1.0/(1+np.exp(-1*self.input_a))
        return s
    def diff_de(self):
        s=(1-self.activation())*self.activation()
        return s