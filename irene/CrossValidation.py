import numpy as np
from random import randrange

def shuffle(x):
    for i in xrange(len(x)-1, 0, -1):
        j = randrange(i + 1)
        x[i], x[j] = x[j], x[i]
    return x
        
def flatten_list(list_of_lists):
        return [item for sublist in list_of_lists for item in sublist]

def split_groups(lst, n):
    return [lst[i::n] for i in xrange(n)]

# k-fold cross validation
# usage: fit first, then call split_train_test(index=2) to get the different splittings of test/train data
class CrossValidation(object):
    def __init__(self, folds=5):
        self.folds = folds
    
    def flatten_list(self, list_of_lists):
        return [item for sublist in list_of_lists for item in sublist]
    
    def fit(self, locations, counts):
        self.locations = np.array(locations)
        self.counts = np.array(counts)
        self.cross_validation_data = {}
        self.n = len(locations)
        
        indicies = range(self.n)
        shuffled_indicies = shuffle(indicies)
        
        groups = np.array(split_groups(shuffled_indicies, self.folds))
        
        for fld in xrange(self.folds):
            fold_data = {}
            train_indicies = range(self.folds)
            train_indicies.remove(fld)
            test_indicies = fld
            train_set = self.flatten_list(groups[train_indicies])
            test_set = groups[test_indicies]
    
            fold_data['train'] = list(train_set)
            fold_data['test'] = test_set
            self.cross_validation_data[fld] = fold_data
        
    def split_train_test(self, index=0):
        if index >= self.folds:
            print 'Index too big'
            return
        else:
            fold_data = self.cross_validation_data[index]
            train = fold_data['train']
            test = fold_data['test']
            
            return self.locations[train], self.locations[test], self.counts[train], self.counts[test]