class Piglet:
    years = 0

    def pig_years(self):
        return self.years * 18


piggy = Piglet()  # instance of class Piglet

print(piggy.pig_years())
piggy.years=2

print(piggy.pig_years())


piggy.years=5

print(piggy.pig_years())
