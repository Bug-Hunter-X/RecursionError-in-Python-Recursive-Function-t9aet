# RecursionError in Python

This repository demonstrates a common but often overlooked error in Python: the `RecursionError`. This error occurs when a recursive function calls itself too many times, exceeding the maximum recursion depth set by Python's interpreter.

## The Bug

The `bug.py` file contains a simple recursive function to calculate Fibonacci numbers.  While correct for small inputs, it will fail for larger numbers, causing a `RecursionError`.

## The Solution

The `bugSolution.py` file demonstrates how to fix the RecursionError by using dynamic programming (memoization) to store already calculated values, preventing redundant recursive calls. This avoids exceeding the recursion depth.