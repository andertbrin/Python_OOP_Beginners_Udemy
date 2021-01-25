class Sprite:

    def __init__(self, character, x, y):
        self.character = character
        self._x = x
        self._y = y

    def move_forward(self, step=5, movement="vertical"):
        if movement == "vertical":
            self._y += step
        elif movement == "horizontal":
            self._x += step
        else:
            raise ValueError("Enter a valid direction")

    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x


my_sprite = Sprite("Luigi", 50, 80)

print(my_sprite)

my_sprite.move_forward()
print(my_sprite.y)

my_sprite.move_forward(10, "horizontal")
print(my_sprite.y, my_sprite.x)

my_sprite.move_forward(step=15, movement="horizontal")
print(my_sprite.y, my_sprite.x)
