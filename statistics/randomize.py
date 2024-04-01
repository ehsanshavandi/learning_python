import math
import random
from scipy.stats import norm


class Randomize:

    @classmethod
    def z_test_random_int(cls, alpha=0.05):
        n = 10000
        probability_repeat = 0.01
        probability_not_repeat = 0.99

        # Binomial
        expected_value = n * probability_repeat
        variance = n * probability_repeat * probability_not_repeat
        repetition = dict()
        for i in range(n):
            random_number = random.randint(1, 100)
            if random_number in repetition:
                repetition[random_number] += 1
            else:
                repetition[random_number] = 1
        # sum of binomial
        expected_value_sum = expected_value
        variance_sum = variance / 100
        # z_test
        x = 0
        for _, observed in repetition.items():
            x += observed
        observed_mean = x / 100
        z = (observed_mean - expected_value_sum) / math.sqrt(variance_sum)
        confidence = 1 - alpha / 2
        # print(confidence)
        offset = norm.ppf(confidence)
        print(offset)
        confidence_interval = [
            (offset * math.sqrt(variance_sum)) + expected_value_sum,
            (-offset * math.sqrt(variance_sum)) + expected_value_sum,
        ]
        print(confidence_interval)
        print("Observed : ", observed_mean)

    @classmethod
    def own_shuffle(cls, _list: list):
        """This algorithm works on the way that loop through on the _list and
        on each iteration use randint method to generate the index of an element
        to swap with"""
        upper_bound = len(_list) - 1
        for i in range(len(_list)):
            if i == upper_bound:
                if random.randint(1, 10) > 5:
                    swap_index = random.randint(0, upper_bound - 1)
                    _list[i], _list[swap_index] = _list[swap_index], _list[i]
            else:
                swap_index = random.randint(i + 1, upper_bound)
                _list[i], _list[swap_index] = _list[swap_index], _list[i]

    @classmethod
    def z_test_own_shuffle(cls, alpha=0.05):
        n = 120000
        orig_list = [1, 2, 3, 4, 5]
        copy_list = [1, 2, 3, 4, 5]
        probability_repeat = 1 / 120
        probability_not_repeat = 1 - probability_repeat
        # Binomial
        expected_value = n * probability_repeat
        variance = n * probability_repeat * probability_not_repeat
        repetition_count = 0
        for i in range(n):
            cls.own_shuffle(copy_list)
            if copy_list == orig_list:
                repetition_count += 1

        confidence = 1 - (alpha / 2)
        offset = norm.ppf(confidence)
        confidence_interval = [
            (offset * math.sqrt(variance)) + expected_value,
            (-offset * math.sqrt(variance)) + expected_value,
        ]
        print(confidence_interval, repetition_count)
