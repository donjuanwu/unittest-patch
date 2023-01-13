"""
Reading temperature from random()
Reference: Homework 1

References:
    Adding existing local project to github
    - https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github
"""

import random


def read_temperature():
    """
    simulates a temperature sensor by returning random temperature values
    :return: -10 - 110 F
    """
    return random.randint(-10, 110)
