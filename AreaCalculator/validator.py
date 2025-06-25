class Validator:
    @staticmethod
    def is_valid_triangle(a, b, c):
        return (
                a + b > c and
                a + c > b and
                b + c > a
        )
    @staticmethod
    def get_valid_number():
        while True:
            try:
                inpt=float(input())
                if inpt>0:
                    return inpt
                else:
                    print("❌ Invalid input. Please enter a positive number.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")