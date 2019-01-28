#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv
from graph import Graph


def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('1', '3')
    graph.add_edge('1', '2')
    graph.add_edge('2', '3')
    graph.add_edge('3', '1')
    print(graph.vertices)
    print(graph.bft('0'))


if __name__ == '__main__':
    # TODO - parse argv
    main()
