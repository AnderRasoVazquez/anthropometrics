from .basemetabolism import BaseMetabolism
from .metabolism_common_data import MetabolismCommonData


class MetabolismMifflin(BaseMetabolism, MetabolismCommonData):

    def __init__(self, gender, activity, weight, height, age):
        BaseMetabolism.__init__(self, gender=gender, activity=activity)
        MetabolismCommonData.__init__(self, weight=weight, height=height, age=age)

    def _get_bmr_formula(self):
        if self.gender is 0:  # male
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        else:
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        return bmr
