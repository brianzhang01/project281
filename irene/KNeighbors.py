import numpy as np
import time
import heapq

def partial_sort_k(lst, k, indicies_needed=False):
    if not indicies_needed:
        new_lst = [-1 * i for i in lst]
        h = new_lst[:k]
        heapq.heapify(h)
        
        for element in new_lst[k:]:
            biggest = h[0]
            if element > biggest:
                heapq.heappushpop(h, element)
        return sorted([-1*i for i in h])
    else:
#         time0 = time.time()
        new_lst = [-1 * i for i in lst]
#         time1 = time.time()
#         new_lst = rev_enumerate(new_lst)
#         time2 = time.time()
#         new_lst = list(new_lst)
#         time3 = time.time()
        h = list(rev_enumerate(new_lst[:k]))
#         time4 = time.time()
        heapq.heapify(h)
#         time5 = time.time()
        
        for element, num in rev_enumerate(new_lst[k:], start=k):
            biggest = h[0][0]
            if element > biggest:
                heapq.heappushpop(h, (element, num))
#         time6 = time.time()
        
        result = sorted([(-1 * i, num) for i,num in h])
        
#         time7 = time.time()
        
#         print '0 to 1 ', time1 - time0
#         print '1 to 2 ', time2 - time1
#         print '2 to 3 ', time3 - time2
#         print '3 to 4 ', time4 - time3
#         print '4.5 to 5 ', time5 - time4
#         print '5 to 6 ', time6 - time5
#         print '6 to 7 ', time7 - time6
        return result
        
def rev_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield elem, n
        n += 1
class KNeighbors(object):
    def __init__(self, n_neighbors=5, weights='uniform'):
        self.n_neighbors = n_neighbors
        self.weight = weights
        self.x_coords = None
        self.y_coords = None
        self.locations = None
        self.n = None
        self.dist_matrix = None
        self.counts = None
        self.infinity = 1000000000.
                
    def fit(self, locations, counts):
        self.locations = np.array(locations)
        self.x_coords = self.locations[:,0]
        self.y_coords = self.locations[:,1]
        
        # add extra dimension for transposing later
        self.x_coords = self.x_coords[None].T
        self.y_coords = self.y_coords[None].T
        
        self.n = len(locations)
        self.counts = counts
        
    def predict(self, new_sites):
        # time0 = time.time()
        new_sites = np.array(new_sites)
        # time1 = time.time()
        new_x_coords = new_sites[:,0]
        new_y_coords = new_sites[:,1]
        # time2 = time.time()
        distances_x = np.subtract(self.x_coords, np.transpose(new_x_coords))
        distances_y = np.subtract(self.y_coords, np.transpose(new_y_coords))
        distances = (distances_x ** 2 + distances_y**2) ** (0.5)
#         print distances.shape
#         print len(distances[:,5])
#         time3 = time.time()
        predictions = []
#         time4_5 = 0
#         time5_6 = 0
#         time6_7 = 0
#         smart_way = 0
#         dumb_way = 0
        for num, pt in enumerate(new_sites):
#             time4 = time.time()
#             time5 = time.time()
            
#             smart_start = time.time()
            sorted_distances = partial_sort_k(distances[:,num], self.n_neighbors, indicies_needed=True)
#             smart_end = time.time()
            
#             dumb_start = time.time()
#             sorted_distances = dumb_partial_sort_k(distances[:,num], self.n_neighbors, indicies_needed=True)
#             dumb_end = time.time()
            
            nearest_distances, nearest_indicies = zip(*sorted_distances)
            nearest_indicies = list(nearest_indicies)
            nearest_points = self.counts[nearest_indicies]
#             time6 = time.time()
            
            if self.weight == 'uniform':
                pt_predict = self.uniform_weight(nearest_points)
            elif self.weight == 'distance':
                pt_predict = self.inverse_distance_weight(nearest_points, nearest_distances)
            else:
                print 'Warning!'
#             time7 = time.time()
            
#             smart_way += smart_end - smart_start
#             dumb_way += dumb_end - dumb_start
#             time4_5 += time5 - time4
#             time5_6 += time6 - time5
#             time6_7 += time7 - time6
            predictions.append(pt_predict)
#         time4 = time.time()
#         print '1 to 2 ', time2 - time1
#         print '2 to 3 ', time3 - time2
        
#         print '4 to 5 ', time4_5
#         print '5 to 6 ', time5_6
#         print '6 to 7 ', time6_7
#         print 'dumb', dumb_way
#         print 'smart', smart_way
#         print time4 - time3
        return predictions
    
    def uniform_weight(self, counts):
        return sum(counts) / len(counts)
    
    def inverse_distance_weight(self, counts, dists):
        inv_weights = []
        for d in dists:
            try:
                inv_weights.append(1./d)
            except ZeroDivisionError:
                inv_weights.append(self.infinity)
        weights_sum = sum(inv_weights)
        inv_weights = [float(i) / weights_sum for i in inv_weights]
        return sum([c*d for c,d in zip(counts, inv_weights)])
            
    def distance_between(self, pt1, pt2):
        return math.sqrt(math.pow(pt1[0] - pt2[0],2) + math.pow(pt1[1] - pt2[1], 2))