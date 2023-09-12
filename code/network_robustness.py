from __future__ import division
# Network Robustness attack
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
    plt.savefig('/Users/jiashichao/Desktop/robustness_distribution_'+Label+'.pdf')

def another_ten(deg_dist):
    newDict = dict(sorted(deg_dist.items(), key=lambda item: item[1], reverse=True))
    return [node for node in newDict]

def nx_score_eigen(G):
    print('calculating eigenvector')
    return nx.eigenvector_centrality_numpy(G, weight='qty')

def robustness_attack(orignal_graph, type_of_attack):
    updated_graph = orignal_graph.copy()
    NumberofNodes = 97739

    # original_diameter = nx.diameter(updated_graph)
    original_diameter = 290
    # nodesString = another_ten(nx_score_eigen(orignal_graph))
    nodesString = '24778	3233393	4086210	4086705	4778790	717202	4293378	3181659	4790043	4868615'
    remove_nodes = nodesString.split()
    for i in range(len(remove_nodes)):
        if remove_nodes[i] in updated_graph:
            updated_graph.remove_node(remove_nodes[i])
            components = nx.strongly_connected_components(updated_graph)
            new_graph = nx.subgraph(updated_graph, max(components, key=len))
            updated_graph = new_graph.copy()
        print(i)
        nx.write_graphml(updated_graph, fileToWrite+str(i)+'.graphml')
        IG = ig.Graph.Read_GraphML(fileToWrite+str(i)+'.graphml')

        new_diameter = IG.diameter()
        new_size = nx.number_of_nodes(updated_graph)

        updated_diameter.append(new_diameter / original_diameter)  # updated diameter
        updated_size.append(new_size / NumberofNodes)  # update size

        removed_nodes = NumberofNodes - new_size
        removed_nodelist.append(removed_nodes / NumberofNodes)


# robustness_attack(G, "random_attack")
# print(updated_diameter)
# print(updated_size)
# robustness_plot(updated_diameter, "Diameter")
# robustness_plot(updated_size, "Size")

# #Degree attack
# robustness_attack(G,"degree_attack")
# print(updated_diameter)
# print(updated_size)
# robustness_plot(updated_diameter,"Diameter")
# robustness_plot(updated_size,"Size")

#Betweenness attack
# robustness_attack(G,"betweenness_attack")
# print(updated_diameter)
# print(updated_size)
# robustness_plot(updated_diameter,"Diameter")
# robustness_plot(updated_size,"Size")

#Closeness attack
# robustness_attack(G,"closeness_attack")
# print(updated_diameter)
# print(updated_size)
# robustness_plot(updated_diameter,"Diameter")
# robustness_plot(updated_size,"Size")

#eigenvector attack
robustness_attack(G,"eigenvector_attack")
print(updated_diameter)
print(updated_size)
print(removed_nodelist)
robustness_plot(updated_diameter,"Diameter")
robustness_plot(updated_size,"Size")