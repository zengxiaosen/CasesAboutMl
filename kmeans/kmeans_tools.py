# # -*- coding: utf-8 -*-
# import math
# import random
#
# class Cluster(object):
#     def __init__(self, samples):
#         if len(samples) == 0:
#             raise Exception("error: a null cluster! ")
#         # the sample dots of this cluster
#         self.samples = samples
#
#         # the dimension of cluster sample dots
#         self.n_dim = samples[0].n_dim
#
#         # judge if the dimension of the sample in this cluster is the sample or not
#         for sample in samples:
#             if sample.n_dim != self.n_dim:
#                 raise Exception("error: the dimension of sample dots is not the same")
#
#         self.centroid = self.cal_centroid()
#
#     def __repr__(self):
#         return str(self.samples)
#     def update(self, samples):
#         """
#         compute the distance between the cluster center before and the cluster now
#         """
#         old_centroid = self.centroid
#         self.samples = samples
#         self.centroid = self.cal_centroid()
#         shift = get_distance(old_centroid, self.centroid)
#         return shift
#
#     def cal_centroid(self):
#         n_samples = len(self.samples)
#         # get the coordinate of all sample dots
#         coords = [sample.coords for sample in self.samples]
#         unzipped = zip(*coords)
#         centroid_coords = [math.fsum(d_list)/n_samples for d_list in unzipped]
#         return Sample(centroid_coords)
#
# class Sample(object):
#     """
#     sample dot class
#     """
#     def __init__(self, coords):
#         self.coords = coords
#         self.n_dim = len(coords)
#
#     def __repr__(self):
#         """
#         output the information of object
#         """
#         return str(self.coords)
#
# def get_distance(a, b):
#     """
#     return the instance of sampleA and sampleB
#     """
#     if a.n_dim != b.n_dim:
#         raise Exception("error: the dimension of sample is different, can not compute")
#     acc_diff = 0.0
#     for i in range(a.n_dim):
#         square_diff = pow((a.coords[i] - b.coords[i]), 2)
#         acc_diff += square_diff
#     distance = math.sqrt(acc_diff)
#     return distance
#
# def gen_random_sample(n_dim, lower, upper):
#     """
#     output random sample
#     """
#     sample = Sample([random.uniform(lower, upper) for _ in range(n_dim)])
#     return sample
