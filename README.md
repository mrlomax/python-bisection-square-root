# Python Bisection Square Root Calculator

This is a Python script I wrote to find the square root of a number using the bisection method, a numerical method for approximating solutions to mathematical problems.



## What I Learned

This project was a practical exercise in implementing a numerical method to solve a common mathematical problem. My learning focused on:

- **Numerical Methods:** Gaining an understanding of how the bisection method works by repeatedly dividing a search interval in half to find a progressively better approximation of a solution.
- **Algorithmic Thinking:** Translating the mathematical concept into concrete programming logic, including setting initial bounds, iterating, and checking for convergence within a set tolerance.
- **Handling Edge Cases:** Implementing specific conditional checks for invalid inputs (negative numbers) and special cases (0 and 1) to ensure the function is robust.

## Features

- Calculates the square root of any non-negative number.
- Uses the bisection method for an efficient, iterative approximation.
- Allows customization of tolerance and maximum iterations.
- Includes full type hinting and docstrings for clarity.

## Requirements

This script uses only Python's standard library, so no external packages are needed. All you need is **Python 3.x** installed.

## Usage

To run the script with the built-in examples, save the code as `bisection.py` and execute it from your terminal:

```sh
python bisection.py
```

This will run the `main()` function and produce the following output:

```
--- Bisection Method Square Root Examples ---
The square root of 16 is approximately 4.0
The square root of 64 is approximately 8.0
The square root of 25 is approximately 5.0
The square root of 2 is approximately 1.4142135381698608
The square root of 98765 is approximately 314.2689916499641
The square root of 0.25 is approximately 0.5
The square root of 0 is 0
The square root of 1 is 1
```

## Code Overview

- **`square_root_bisection`**: The core function that takes a number and other parameters, performs the bisection algorithm, and prints the result.
- **`main`**: The execution block that runs several test cases through the calculation function.

## Technologies Used

- **Language:** Python 3
- **Key Concepts:** Numerical Methods, Algorithms, Type Hinting, Docstrings
