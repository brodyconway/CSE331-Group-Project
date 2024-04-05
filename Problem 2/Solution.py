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


    def dfs_all_paths(self, graph, current_node, client, visited, path):
        visited.append(current_node)
        path_list = []
        for neighbor in self.graph[current_node]:
            if neighbor not in visited:
                new_path = path + neighbor
                if neighbor == client:
                    path_list.append(new_path)
                else:
                    new_paths = self.dfs_all_paths(self,graph, neighbor, client, visited, new_path)
                    path_list.extend(new_paths)
        visited.remove(current_node)
        return path_list


    def longest_path(client_paths):
        for h, paths in client_paths.items():
            if len(paths) > length:
                length = len(paths)
        return length

    
    def output_paths(self):
        path = [] 
        visited = []
        client_paths = {}
        
        for client in self.info['list_clients']:
            client_paths[client] = self.dfs_all_paths(self, self.graph, self.isp, client, visited, path)
            
        length = longest_path(client_paths) 
        temp_dict = {}
        for i in range(length):
            for client, paths in client_paths.items():
                try:
                    temp_dict[client]=paths[i]
                except IndexError:
                    client_paths[client] = [paths[0]]
            i = i+1
            # call new function
        

        paths, bandwidths, priorities = {}, {}, {}
        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        return (paths, bandwidths, priorities)
