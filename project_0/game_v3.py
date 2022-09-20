import numpy as np
from numpy import random

def adaptive_predict(number: int = 1) -> int:
    """Adaptively guess the number taking into account the information about,
    more of an actual option than a hidden number or less.
       The function accepts a hidden number and returns the number of attempts.

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    limit_low = 0 # set lower limit of guessing range
    limit_high = 101 # set upper limit of guessing range
    count = 0 # set number of attempts
    while True:
        count += 1
        predict_number = int((limit_low + limit_high) / 2) # calculate average value in guessing range
        if predict_number < number: 
            limit_low = predict_number # redefining lower limit of range if hidden number are more
        if predict_number > number:
            limit_high = predict_number # redefining upper limit of range if hidden number are less
        if number == predict_number: # сompletion of the cycle, the number is guessed
            break
    return count

if __name__ == '__main__':
    adaptive_predict(number)
