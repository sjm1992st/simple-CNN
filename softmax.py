import numpy as np
class softmax:
    def __init__(self, input_a):
        self.input_a=input_a
    def cfi(self):
        [v_x,v_y]=self.output_a.shape
        d=np.zeros([v_x,v_y])
        for i in range(v_x):
            max_=np.max([self.output_a[i,]])
            out_copy=np.exp([self.output_a[i,]]-max_)
            sum_=np.sum(out_copy)
            out_copy=out_copy*1.0/sum_
            [ax,ay]=np.where(out_copy==np.max(out_copy))
            d[i,ay]=1
        return  d