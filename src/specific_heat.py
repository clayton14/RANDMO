import sys, os

delta = '\u0394'


def main() -> float:
    while True:
        try:
            # Q = float(input(""))
            # C = float(input(""))
            # Ti = float(input(""))
            # Tf = float(input(""))
            choice = input(f"[1] Q\n[2] C \n[3] {delta}T\n[4] M\nsloving for what: ")
            choice = int(choice)
            if (choice > 4 and not isinstance(choice, int)):
                print(f"[ERROR] {choice} is not an option")
                continue
            if(choice == 1):
                C = float(input("Enter the specific heat (j/gC): "))
                M = float(input("Enter the mass (g): "))
                Ti = float(input("Enter the init temp (C): "))
                Tf = float(input("Enter the final temp (C): "))
                return M * C * (Tf - Ti)
            elif(choice == 2):
                Q = float(input("Enter the energy (j): "))
                M = float(input("Enter the mass (g): "))
                Ti = float(input("Enter the init temp (C): "))
                Tf = float(input("Enter the final temp (C): "))
                return Q / M * (Tf - Ti)
            elif(choice == 3):
                Q = float(input("Enter the energy (j): "))
                M = float(input("Enter the mass (g): "))
                C = float(input("Enter the specific heat (j/gC): "))
                return Q / (M * C)
            elif(choice == 4):
                Q = float(input("Enter the energy (j): "))
                C = float(input("Enter the specific heat (j/gC): "))
                Ti = float(input("Enter the init temp (C): "))
                Tf = float(input("Enter the final temp (C): "))
                return Q / C * (Tf - Ti)
        except ValueError as err:
            print("[ERROR] entered value must be a number")
            continue
        except ZeroDivisionError as err:
            print("[ERROR] can't devide by zero")



if __name__ == "__main__":
    answer = main()
    print(f"The answer is => {answer}")
   