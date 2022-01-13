# import turtle
# tokral = turtle.Turtle()
# tokral.shape("turtle")
# tokral.color("red")
# tokral.shapesize(5, 5, 12)
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
pokemon = PrettyTable()
pokemon.align = "l"

pokemon.field_names = ["Pokemon name", "Type", "HP"]
pokemon.add_rows(
    [
        ["Pikachu", "Electric", 35],
        ["Squirtle", "Water", 44],
        ["Charmander", "Fire", 39]

    ]
)
print(pokemon.get_string(start=0, end=2))


