from .basemetabolism import BaseMetabolism
from .metabolism_common_data import MetabolismCommonData


class MetabolismHarris(BaseMetabolism, MetabolismCommonData):

    def __init__(self, gender, activity, weight, height, age):
        BaseMetabolism.__init__(self, gender=gender, activity=activity)
        MetabolismCommonData.__init__(self, weight=weight, height=height, age=age)

    def _get_bmr_formula(self):
        if self.gender is 0:  # male
            bmr = (66.5 + (13.75 * self.weight) + (5.003 * self.height) - (6.775 * self.age))
        else:
            bmr = (655.1 + (9.563 * self.weight) + (1.85 * self.height) - (4.676 * self.age))
        return bmr
