class calculadora:
    def __init__(self, value_1, value_2, operator):
        self.value_1 = value_1
        self.value_2 = value_2
        self.operator = operator

    def make_operations(self):
        if self.operator == "+":
            return self.value_1 + self.value_2
        elif self.operator == "-":
            return self.value_1 - self.value_2
        elif self.operator == "*":
            return self.value_1 * self.value_2
        elif self.operator == "/":
            return self.value_1 / self.value_2

def main():
    while True:
        value_1 = int(input("Introduce el valor 1: "))
        value_2 = int(input("Introduce el valor 2: "))
        print("If you want to exit you need to input a blank operator: ")
        operator = (input("Introduce el operador: "))

        if operator == "":
            break

        clc = calculadora(value_1=value_1, value_2=value_2, operator=operator)
        print(clc.make_operations())






if __name__ == "__main__":
    main()