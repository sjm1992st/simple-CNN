import numpy as np
class relu:
    def __init__(self, input_a):
        self.input_a=input_a
    def activation(self):
        [r_x,r_y]=self.input_a
        s=np.zeros([r_x,r_y])
        for i in range(r_x):
            for j in range(r_y):
                if self.input_a[i,j]<0:
                    s[i,j]=0
                if self.input_a[i,j]>0:
                    s[i,j]=self.input_a[i,j]
        return s
    def diff_de(self):
        [r_x,r_y]=self.input_a
        s=np.zeros([r_x,r_y])
        for i in range(r_x):
            for j in range(r_y):
                if self.input_a[i,j]<0:
                    s[i,j]=0
                if self.input_a[i,j]>0:
                    s[i,j]=1
        return s