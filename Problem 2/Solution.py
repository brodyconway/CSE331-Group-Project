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
                    new_paths = self.dfs_all_paths(graph, neighbor, client, visited, new_path)
                    path_list.extend(new_paths)
        visited.remove(current_node)
        return path_list



    def output_paths(self):
        path = []
        paths = {} 
        visited = []
        client_paths = {}
        for client in self.info['list_clients']:
            client_paths[client] = self.dfs_all_paths(self, self.graph, self.isp, client, visited, path)
    
    # NOW NEED TO FIND WHICH PATH IN CLIENT_PATHS HAS NO PENALTY. PATH WITH NO PENLTY GETS ADDED TO PATHS DICTIONARY BELOW. IF ALL PATHS HAVE A PENALTY FOR A NODE JUST ADD THE FIRST PATH AT INDEX 0 TO MAKE IT EASIER

        paths, bandwidths, priorities = {}, {}, {}
        # Note: You do not need to modify all of the above. For Problem 1, only the paths variable needs to be modified. If you do modify a variable you are not supposed to, you might notice different revenues outputted by the Driver locally since the autograder will ignore the variables not relevant for the problem.
        # WARNING: DO NOT MODIFY THE LINE BELOW, OR BAD THINGS WILL HAPPEN
        return (paths, bandwidths, priorities)
