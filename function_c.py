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
class no_soigmoid:
    def __init__(self, input_a):
        self.input_a=input_a
    def activation(self):
        return self.input_a
    def diff_de(self):
        return self.input_a
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
class softmax:
    def __init__(self, input_a):
        self.input_a=input_a
    def cfi(self):
        [v_x,v_y]=self.output_a.shape
        d=np.zeros([v_x,v_y])
        max_=np.max(self.output_a)
        out_copy=np.exp(self.output_a-max_)
        sum_=np.sum(out_copy)
        out_copy=out_copy*1.0/sum_
        [ax,ay]=np.where(out_copy==np.max(out_copy))
        d[ax,ay]=1
        return  d
class tanh:
    def __init__(self, input_a):
        self.input_a=input_a
    def activation(self):
        s=np.tanh(self.input_a)
        return s
    def diff_de(self):
        s=1-self.activation()**2
        return s