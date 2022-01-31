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
                print(f"The answer is => {M * C * (Tf - Ti)} J")
                continue
            elif(choice == 2):
                Q = float(input("Enter the energy (j): "))
                M = float(input("Enter the mass (g): "))
                Ti = float(input("Enter the init temp (C): "))
                Tf = float(input("Enter the final temp (C): "))
                print( f"The answer is => {Q / M * (Tf - Ti)} J/gC")
                continue
            elif(choice == 3):
                Q = float(input("Enter the energy (j): "))
                M = float(input("Enter the mass (g): "))
                C = float(input("Enter the specific heat (j/gC): "))
                print(f"The answer is => {Q / (M * C)} C")
                continue
            elif(choice == 4):
                Q = float(input("Enter the energy (j): "))
                C = float(input("Enter the specific heat (j/gC): "))
                Ti = float(input("Enter the init temp (C): "))
                Tf = float(input("Enter the final temp (C): "))
                print(f"The answer is => {Q / C * (Tf - Ti)} g")
                continue
        except ValueError as err:
            print("[ERROR] entered value must be a number")
            continue
        except ZeroDivisionError as err:
            print("[ERROR] can't devide by zero")
            continue
        except KeyboardInterrupt as err:
            print("\n[EXIT]")
            break


if __name__ == "__main__":
    main()
   