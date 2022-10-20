from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


@lru_cache(maxsize=None)
def permutation(no_days, possible_absent):
    """used recursion with time complexity N*M
    where N=no_days and M=possible_absent"""

    if max_absent == possible_absent:
        return 0

    if no_days == 0:
        return 1

    return permutation(no_days - 1, 0) + permutation(no_days - 1, possible_absent + 1)


if __name__ == "__main__":
    no_of_days = int(input())
    max_absent = 4  # consecutive classes miss in days

    no_of_class_to_attend = permutation(
        no_of_days, 0
    )  # The number of ways to attend classes over N days.

    prob_missing_gradation = permutation(
        no_of_days - 1, 1
    )  # The probability that you will miss your graduation ceremony.

    print(f"for {no_of_days} days: {prob_missing_gradation}/{no_of_class_to_attend}")
