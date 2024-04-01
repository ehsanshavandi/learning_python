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
        print(confidence)
        offset = norm.ppf(confidence)
        print(offset)
        confidence_interval = [
            (offset * math.sqrt(variance_sum)) + expected_value_sum,
            (-offset * math.sqrt(variance_sum)) + expected_value_sum,
        ]
        print(confidence_interval)
        print("Observed : ", observed_mean)

    @classmethod
    def own_shuffle(cls, _list: list): ...
