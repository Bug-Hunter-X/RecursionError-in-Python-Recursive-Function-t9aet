def function_with_uncommon_error(n):
    if n == 0:
        return 0  # This is fine
    elif n == 1:
        return 1  # This is also fine
    else:
        return function_with_uncommon_error(n-1) + function_with_uncommon_error(n-2) #This line will cause RecursionError for large n