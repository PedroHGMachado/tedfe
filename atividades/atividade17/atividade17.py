
class PhysicValue(object):

    def __init__(self, value, uncertainty=0, unity='adm'):

        self.value = value
        self.uncertainty = uncertainty
        self.unity = unity

    def __print__(self):

        rounded_unc, ndecs = self.__round_to_significatives(self.uncertainty)
        rounded_value = round(self.value, ndecs)

        return f'({rounded_value} +- {rounded_unc}) {self.unity}'

    __repr__ = __print__


    def __round_to_significatives(self, number, algs=2):

        ten_factor = 0
        while number * (10 ** ten_factor) // 1 == 0:
            ten_factor += 1

        n_decimals = ten_factor + (algs - 1)

        return round(number, n_decimals), n_decimals



C_cal = 129.753
sigma_C_cal = 42.262
unity_C_cal = 'J/K'

c_h2o = 4.18441
sigma_c_h2o = 0.0685581
unity_c_h2o = 'J/g.K'

C_cal = PhysicValue(C_cal, sigma_C_cal, unity_C_cal)
c_h2o = PhysicValue(c_h2o, sigma_c_h2o, unity_c_h2o)