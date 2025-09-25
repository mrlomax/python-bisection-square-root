def square_root_bisection(
        square_target: float, 
        tolerance: float = 1e-7, 
        max_iterations: int = 100
) -> float | None:
    """Calculates and prints the square root using the bisection method. 

    This function finds an approximate square root and prints the result to the console.

    Args:
        square_target (float): The number to find the square root of. Must be non-negative.
        tolerance (float): The desired accuracy of the result. Defaults to 1e-7.
        max_iterations (int): The maximum number of iterations. Defaults to 100. 

    Returns:
        float | None: The calculated root, or None if the method fails to converge.

    Raises:
        ValueError: If the square_target is a negative number.
    """
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers.")
    elif square_target == 1:
        print(f"The square root of {square_target} is 1")
        return 1.0
    elif square_target == 0:
        print(f"The square root of {square_target} is 0")
        return 0.0
    
    low = 0.0
    high = max(1.0, square_target)
    root = None

    for _ in range(max_iterations):
        mid = (low + high) / 2
        square_mid = mid ** 2

        if abs(square_mid - square_target) < tolerance:
            root = mid
            break
        elif square_mid < square_target:
            low = mid
        else:
            high = mid
    
    if root is None:
        print(f'Failed to converge for {square_target} within {max_iterations} iterations.')
    else:
        print(f'The square root of {square_target} is approximately {root}')

    return root

def main ():
    """Runs several examples of the square root calculation."""
    print("--- Bisection Method Square Root Examples ---")

    targets_to_test = [16, 64, 25, 2, 98765, 0.25, 0, 1]
    
    for n in targets_to_test:
        square_root_bisection(n)

if __name__ == '__main__':
   main()