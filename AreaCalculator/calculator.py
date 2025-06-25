from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle
from shapes.circle import Circle
from shapes.hexagon import Hexagon
from validator import Validator
import time

def calculator():
    print("\n👋 Welcome to the Area Shape Resolver Calculator!")
    time.sleep(2)

    while True:
        print("""\033[93m
        ===============================================
        ||      Area Shape Resolver Calculator       ||
        ===============================================
        ||      1.rectangle    ||       4.circle     ||
        ||      2.square       ||       5.hexagon    ||
        ||      3.triangle     ||       6.exit       ||
        ===============================================\033[0m""")
        try:
            choice = int(input("Enter your choice : "))
            if choice < 1 or choice > 6:
                print("❌ Invalid choice. Please enter a number between 1 and 6.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
            continue

        match choice:
            case 1:
                width = Validator.get_valid_number("Enter width : ")
                height = Validator.get_valid_number("Enter height : ")
                print(Rectangle(height,width))
            case 2:
                side = Validator.get_valid_number("Enter side : ")
                print(Square(side))
            case 3:
                side_a = Validator.get_valid_number("Enter side a : ")
                side_b = Validator.get_valid_number("Enter side b : ")
                side_c = Validator.get_valid_number("Enter side c : ")
                if Validator.is_valid_triangle(side_a, side_b, side_c):
                    print(Triangle(side_a, side_b, side_c))
                else:
                    print("❌ The given sides do not form a valid triangle.")
            case 4:
                radius = Validator.get_valid_number("Enter radius : ")
                print(Circle(radius))
            case 5:
                side = Validator.get_valid_number("Enter side : ")
                print(Hexagon(side))
            case 6:
                print("Exiting calculator... 👋")
                break
if __name__ == "__main__":
    calculator()