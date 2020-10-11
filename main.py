from equations import Equation
from time import sleep


def run_balance():
    """
    Runs the chemical equation balance algorithm
    """
    print('=================================================')
    print('Insert chemical equation with element followed by the number of atoms:')
    print('Example: H2 + O2 => H2O')
    user_input = input('>>> ')
    try:
        equation = Equation(user_input)
        print('Balanced equation: ' + equation.equation_balancer())
        # sleep(3)
        # run_balance()
    except IndexError:
        print('Invalid input...')
        # sleep(3)
        # run_balance()

run_balance()