# coding: utf-8

from collections import defaultdict


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Graph:
    def __init__(self):
        self.edge = defaultdict(list)

    def __getitem__(self, k):
        return self.edge[k]

    def add_edge(self, from_node, to_node):
        self.edge[from_node].append(to_node)

    def remove_edge(self, from_node, to_node):
        self.edge[from_node].remove(to_node)
