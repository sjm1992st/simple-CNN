from __future__ import division
import numpy as np
import random
import matplotlib.pylab as plt
import math
import cnn16.bp_top as bp
class output_layer(bp.bp_layer):
    def __init__(self, input_a, output_a):
        bp.bp_layer.__init__(self, input_a, output_a)
        #self.forward_weight=forward_weight

    def diff_out_1(self, y, y_r,diff_f):
        g=diff_f*(y_r-y)
        return g