from abc import ABC, abstractmethod


EXTRA_CALORIES_LACTATING = 454


class BaseMetabolism(ABC):

    def __init__(self, gender, activity):
        self.gender = gender
        self.activity = activity

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if 0 <= gender <= 5:
            self._gender = gender
        else:
            raise ValueError("gender must be 0 for male or 1-5 for female")

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, activity):
        if not (1.2 <= activity <= 1.9):
            raise ValueError("activity must be a number between 1.2 and 1.9")
        self._activity = activity

    @abstractmethod
    def _get_bmr_formula(self):
        pass

    def get_bmr(self) -> float:
        bmr = self._get_bmr_formula()

        if 2 <= self.gender <= 4:  # female pregnant
            trimester = self._get_trimester_based_on_gender()
            bmr += self.get_extra_calorie_needs_during_pregnancy(trimester)
        elif self.gender is 5:  # lactating
            # TODO si se ha ganado todo el peso necesario durante el embarazo reducir un 15% el total
            bmr += EXTRA_CALORIES_LACTATING

        return bmr

    def _get_trimester_based_on_gender(self):
        return self.gender - 1

    @staticmethod
    def get_extra_calorie_needs_during_pregnancy(trimester) -> int:
        # TODO trimester 1-3 raise valueerror si no es ninguno de esos
        if trimester is 1:
            return 85
        elif trimester is 2:
            return 285
        else:  # trimester is 3
            return 475

    def get_tmr(self):
        return self.get_bmr() * self.activity

