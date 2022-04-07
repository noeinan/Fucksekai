init python:
    class WeightedRandom(object):
        def __init__(self, list_of_values_and_weights):
            """
            expects a list of [ (value, weight), (value, weight),...]
            """
            self.the_list = list_of_values_and_weights
            self.the_sum = sum([ v[1] for v in list_of_values_and_weights])

        def pick(self):
            """
            return a random value taking into account the weights
            """
            import random
            r = random.uniform(0, self.the_sum)
            s = 0.0
            for k, w in self.the_list:
                s += w
                if r < s: return k
            return k
