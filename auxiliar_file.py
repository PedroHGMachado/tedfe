import matplotlib.pyplot as plt
import numpy as np


class PhysicalMeasure(object):

    def __init__(self, value, uncertainty, physical_unity, n_signf=2):

        if uncertainty > 10*value:
            raise ValueError('Valor Incerto!')

        self.value = value
        self.uncertainty = uncertainty
        self.unity = physical_unity

        self.__get_repr()


    def __repr__(self):
        return self.value_repr


    def __str__(self):
        return self.value_repr


    def __get_repr(self, algs=2):

        value = self.value
        uncertainty = self.uncertainty

        ten_factor = 0

        dir = (1 if uncertainty <= 1 else -1)

        powered_unc = int(uncertainty * (10 ** ten_factor) // 1)
        while len(str(powered_unc)) != algs:
            ten_factor += dir
            powered_unc = int(uncertainty * (10 ** ten_factor) // 1)


        powered_val = round(value * (10 ** ten_factor))
        powered_unc = round(uncertainty * (10 ** ten_factor))

        value_repr = powered_val * (10 ** -ten_factor)


        if ten_factor >= 0:
            self.value_repr = f'{value_repr:.{ten_factor}f}({powered_unc}) {self.unity}'
        else:
            if ten_factor < -1:
                self.value_repr = f'{powered_val}({powered_unc})x10^{-ten_factor} {self.unity}'
            else:
                self.value_repr = f'{powered_val}({powered_unc})x10 {self.unity}'

