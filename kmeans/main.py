# # -*- coding: utf-8 -*-
# import random
# from kmeans_tools import Cluster, get_distance, gen_random_sample
# import matplotlib.pyplot as plt
# from matplotlib import colors as mcolors
#
# def kmeans(samples, k, cutoff):
#     init_samples = random.sample(samples, k)
#     clusters = [Cluster([samples]) for sample in init_samples]
#
#     n_loop = 0
#     while True:
#         lists = [[] for _ in clusters]
#         n_loop += 1
#         for sample in samples:
#             smallest_distance = get_distance(sample, clusters[0].centroid)
#             cluster_index = 0
#
#             for i in range(k - 1):
#                 distance = get_distance(sample, clusters[i+1].centroid)
#                 if distance < smallest_distance:
#                     smallest_distance = distance
#                     clusters_index = i+1
#
#             lists[cluster_index].append(sample)
#         biggest_shift = 0.0
#
#         for i in range(k):
#             shift = clusters[i].update(lists[i])
#             biggest_shift = max(biggest_shift, shift)
#
#         if biggest_shift < cutoff:
#             print ("after the {} iterator , cluster is stable ".format(n_loop))
#             break
#     return clusters
#
# def run_main():
#     n_samples = 1000
#     n_feat = 2
#     lower = 0
#     upper = 200
#     n_cluster = 5
#     samples = [gen_random_sample(n_feat, lower, upper) for _ in range(n_samples)]
#
#     cutoff = 0.2
#     clusters = kmeans(samples, n_cluster, cutoff)
#     for i, c in enumerate(clusters):
#         for sample in c.samples:
#             print ('cluster--{}, sample dot--{}'.format(i, sample))
#
#     plt.subplot()
#     color_names = list(mcolors.cnames)
#     for i, c in enumerate(clusters):
#         x = []
#         y = []
#         random.choice
#         color = [color_names[i]] * len(c.samples)
#         for sample in c.samples:
#             x.append(sample.coords[0])
#             y.append(sample.coords[1])
#         plt.scatter(x, y, c=color)
#     plt.show()
#
# if __name__ == '__main__':
#     run_main()
#
