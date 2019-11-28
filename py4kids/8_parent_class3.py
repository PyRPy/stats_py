class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalk(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print("breathing")
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding young')

class Giraffes(Mammals):
    def __init__(self, spots):
        self.giraffe_spots = spots
    def find_food(self):
        self.move()
        print("I've found food!")
    def eat_leaves_from_trees(self):
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()

ozwald = Giraffes(100)
gertrude = Giraffes(150)

print(ozwald.giraffe_spots)
print(gertrude.giraffe_spots)














