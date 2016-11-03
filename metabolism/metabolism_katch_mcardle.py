from .basemetabolism import BaseMetabolism


class MetabolismKatchMcardle(BaseMetabolism):

    def __init__(self, gender, activity, muscle_mass):
        BaseMetabolism.__init__(self, gender=gender, activity=activity)
        # TODO calcular masa muscular quiza usar porcentaje de grasa?
        self.muscle_mass = muscle_mass

    @property
    def muscle_mass(self):
        return self._muscle_mass

    @muscle_mass.setter
    def muscle_mass(self, muscle_mass):
        if muscle_mass < 0:
            raise ValueError("muscle_mass can't be a negative number")
        self._muscle_mass = muscle_mass

    def _get_bmr_formula(self):
        return 370 + (21.6 * self.muscle_mass)
