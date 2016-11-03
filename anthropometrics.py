EXTRA_CALORIES_LACTATING = 454


class Metabolism(object):
    # http://www.freedieting.com/calorie_needs.html

    def __init__(self, gender=0, weight=0, height=0, age=0, activity=1.2, waist_circumference=0,
                 hip_circumference=0, wrist_circumference=0):
        """
        :param gender: int (0 male, 1 female, 2 pregnant 1 tri, 3 pregnant 2 tri, 4 preg 3 tri, 5 lactating)
        :param weight: float
        :param height: float
        :param age: int
        """
        self.gender = gender
        self.weight = weight
        self.height = height
        self.age = age
        self.activity = activity
        self.waist_circumference = waist_circumference
        self.hip_circumference = hip_circumference
        self.wrist_circumference = wrist_circumference

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if 0 <= gender <= 5:
            self._gender = gender
        else:
            raise ValueError("gender must be 0 for male or 1 for female")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("age can't be a negative number")
        self._age = age

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if weight < 0:
            raise ValueError("weight can't be a negative number")
        self._weight = weight

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError("height can't be a negative number")
        self._height = height

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, activity):
        if not (1.2 <= activity <= 1.9):
            raise ValueError("activity must be a number between 1.2 and 1.9")
        self._activity = activity

    def get_bmi(self) -> float:
        return self.weight / (self.height / 100) ** 2

    def get_whr(self):
        return self.waist_circumference / self.hip_circumference

    def has_whr_risk(self):
        if self.gender == 0:  # male
            return True if self.get_whr() >= 1 else False
        else:
            return True if self.get_whr() >= 0.85 else False

    def get_complexion(self):
        # ecto meso endo 0 1 2
        complexion = self.height / self.wrist_circumference
        if self.gender == 0:  # male
            # return 0 if complexion >= 10.4 elif 10.4 > complexion > 9.6 0 else 0
            if complexion >= 10.6:
                return 0
            elif 10.4 > complexion > 9.6:
                return 1
            else:  # <= 9.6
                return 2
        else:  # female
            if complexion >= 10.9:
                return 0
            elif 10.9 > complexion > 9.9:
                return 1
            else:  # <= 9.9
                return 2

    def get_ideal_body_weight_devine(self):
        if self.gender == 0:  # male
            return (self.height - 152.4) * (0.91) + 50
        else:
            return (self.height - 152.4) * (0.91) + 45.5

    def get_ideal_body_weight_robinson(self):
        if self.gender == 0:  # male
            return (self.height - 152.4) * 0.748 + 52
        else:
            return (self.height - 152.4) * 0.669 + 49

    def get_ideal_body_weight_miller(self):
        if self.gender == 0:  # male
            return (self.height - 152.4) * 0.555 + 56.2
        else:
            return (self.height - 152.4) * 0.5354 + 53.1

    def get_ideal_body_weight_hamwi(self):
        if self.gender == 0:  # male
            return (self.height - 152.4) * 1.063 + 48.2
        else:
            return (self.height - 152.4) * 0.866 + 45.5

    def get_ideal_body_weight_lemmens(self):
        if self.gender == 0:  # male
            return 22 * ((self.height / 100) * (self.height / 100))
        else:
            return 22 * ((self.height / 100) * (self.height / 100))

    def get_ideal_body_weight_average(self):
        return (self.get_ideal_body_weight_devine() +
                self.get_ideal_body_weight_robinson() +
                self.get_ideal_body_weight_miller() +
                self.get_ideal_body_weight_hamwi() +
                self.get_ideal_body_weight_lemmens()) / 5

    def get_maximum_heart_rate_tanaka(self):
        # todo unit tests
        # todo unit tests pregnant lactating
        return 208.75 - (0.73 * self.age)

        # todo fat% pliegues
        # todo metabolismo con fat% lean mass
        # todo require() funcion con un array de las variables que se tienen que iniciar


def main():
    pass


if __name__ == "__main__":
    main()
