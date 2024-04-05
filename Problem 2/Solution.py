from Traversals import bfs_path
import heapq
from collections import deque
from Simulator import Simulator
import sys

class Solution:

    def __init__(self, problem, isp, graph, info):
        self.problem = problem
        self.isp = isp
        self.graph = graph
        self.info = info

    #recursively adds each possible path for a node
    def dfs_all_paths(self, graph, current_node, client, visited, path):
        visited.append(current_node)
        path_list = []
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                new_path = path.copy()
                new_path.append(neighbor)
                if neighbor == client:
                    path_list.append(new_path)
                else:
                    sub_paths = self.dfs_all_paths(graph, neighbor, client, visited, new_path)
                    path_list.extend(sub_paths)
        visited.remove(current_node)
        return path_list

    # gets longest possible path out of all clients. This length will be the stopping condition used later on
    def longest_path(self, client_paths):
        length =0
        for h, paths in client_paths.items():
            if len(paths) > length:
                length = len(paths)
        return length

    
    def output_paths(self):
        path = [] 
        visited = []
        client_paths = {}
        
        paths, bandwidths, priorities = {}, {}, {}
        paths = bfs_path(self.graph, self.isp, self.info['list_clients'])
        for client in self.info['list_clients']:
            client_paths[client] = self.dfs_all_paths(self.graph, self.isp, client, visited, path)
            
        length = self.longest_path(client_paths) 
        temp_dict = {}
        delays = {}
        for i in range(length):
            for client, paths in client_paths.items():
                try:
                    temp_dict[client]=paths[i]
                except IndexError:
                    client_paths[client] = [paths[0]]
            i = i+1
            run(self, self.graph, self.isp, self.list_clients, temp_dict, bandwidths, priorities, self.info['is_rural'])
            delays = get_delays(self, self.list_clients)
            for clients in self.info['list_clients']:
                revenue = pen_0(self, client, delays, self.info['alphas'], self.info['payments'])
                if revenue > paths.get(clients):
                    paths[clients] = revenue

        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        return (paths, bandwidths, priorities)
