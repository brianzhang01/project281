import math
from scipy.stats import poisson

def poisson_likelihood(kneigh, locations, counts):
    predictions = kneigh.predict(locations) 
    results = []
    for p,c in zip(predictions, counts):
        try:
            log_likelihood = -math.log(poisson(p).pmf(c))
        # handle k >>> 0 cases
        except ValueError:
            log_likelihood = p - c*math.log(p) + c*math.log(c) - c + math.log(math.sqrt(2 * math.pi * c))
        results.append(log_likelihood)
    return (sum(results) / float(len(results)))

# poisson baseline
def poisson_baseline(baseline, counts):
    results = []
    for c in counts:
        try:
            log_likelihood = -math.log(poisson(baseline).pmf(c))
        # handle k >> 0 cases
        except ValueError:
            log_likelihood = baseline - c*math.log(baseline) + c*math.log(c) - c + math.log(math.sqrt(2 * math.pi * c))
        results.append(log_likelihood)
    return (sum(results) / float(len(results)))

def perfect_guessing(counts):
    results = [-math.log(poisson(c).pmf(c)) for c in counts]
    return (sum(results) / float(len(results)))