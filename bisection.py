def square_root_bisection(square_target, tolerance= 1e-7, max_iterations= 100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        pass

def main ():
    pass

if __name__ == '__main__':
    pass