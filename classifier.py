import numpy as np
class classifier:
    def __init__(self, output_a):
        self.output_a=output_a
    def cfi(self):
        [v_x,v_y]=self.output_a.shape
        d=np.zeros([v_x,v_y])
        for i in range(v_y):
            if self.output_a[0,i]<0.7:
                d[0,i]=0
            if self.output_a[0,i]>0.7:
                d[0,i]=1
        return  d