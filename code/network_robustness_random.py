from __future__ import division
import networkx as nx
import random
import pylab as plt
import igraph as ig

fileToWrite = '/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/results/3_1/updated'
G = nx.read_graphml('/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/preprocess/GSCC-2013-11-04_to_2013-11-10.graphml')
# G = nx.fast_gnp_random_graph(500, 0.08)

updated_diameter = []
updated_size = []
removed_nodes = 0
removed_nodelist = []


def robustness_plot(updated_values, Label):
    plt.figure()
    plt.grid(True)
    plt.plot(removed_nodelist, updated_values, 'ro-')
    plt.ylabel(Label + ' of GC')
    plt.xlabel('Proportion of Nodes Removed')
    plt.title(Label + ' Distribution')
    plt.savefig('/Users/jiashichao/Desktop/robustness_distribution_'+Label+'_random.pdf')
    # plt.show()
    # plt.close()


def random_attack(orignal_graph):
    updated_graph = orignal_graph.copy()
    NumberofNodes = nx.number_of_nodes(orignal_graph)
    original_diameter = 290
    for i in range(10):
        listofNodes = updated_graph.nodes()
        IteratorNodes = 10
        RandomNodeSample = random.sample(listofNodes, IteratorNodes)  # Random 10% of Nodes randomly
        updated_graph.remove_nodes_from(RandomNodeSample)
        components = nx.strongly_connected_components(updated_graph)
        new_graph = nx.subgraph(updated_graph, max(components, key=len))

        updated_graph = new_graph.copy()
        nx.write_graphml(updated_graph, fileToWrite+str(i)+'random.graphml')
        IG = ig.Graph.Read_GraphML(fileToWrite+str(i)+'random.graphml')

        new_diameter = IG.diameter()
        new_size = nx.number_of_nodes(updated_graph)

        updated_diameter.append(new_diameter / original_diameter)  # updated diameter
        updated_size.append(new_size / NumberofNodes)  # update size

        removed_nodes = NumberofNodes - new_size
        removed_nodelist.append(removed_nodes / NumberofNodes)


random_attack(G)
print(updated_diameter)
print(updated_size)
print(removed_nodelist)
robustness_plot(updated_diameter, "Diameter")
robustness_plot(updated_size, "Size")