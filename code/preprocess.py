from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import os
import igraph as ig

fileToWrite = '/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/preprocess/GSCC-'
fileToRead = '/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/preprocess/'
savePath = ''

def Preprocess(fileCollections):
    files = os.listdir(fileCollections)
    print(files)
    for file in files:
        print('start to process: ', file)
        G = nx.read_graphml(fileToRead + file)
        components = nx.strongly_connected_components(G)
        G_strong = nx.subgraph(G, max(components, key=len))
        nx.write_graphml(G_strong, fileToWrite+file)
        print('done with: ', file)
    print("done")

def ChooseWeek(fileCollections):
    files = os.listdir(fileCollections)
    print(files)
    nodeNumberList = []
    for file in files:
        print('start to process: ', file)
        G = nx.read_graphml(fileCollections + file)
        nodeNumberList.append(len(G.nodes))
        print('done with: ', file)
    print('-----------------------------------')
    # GSCC-2013-12-02_to_2013-12-08.graphml
    print(nodeNumberList)


bins = np.logspace(np.log10(1), np.log10(1e5), 25)

def plot_hist(degrees):
    plt.hist([deg for _, deg in degrees], bins)
    plt.xscale('log')
    plt.yscale('log')

def ReadGraph(filePath):
    G = nx.read_graphml(filePath)
    return G

def DegreeDistribution(G1, G2, G3, save):
    plt.figure(figsize=(15, 3))
    # plt.figure(figsize=(4, 4))

    plt.subplot(1, 3, 1)
    plt.title('Erdős–Rényi Distribution')
    plot_hist(G1.degree())

    plt.subplot(1, 3, 2)
    plt.title('Watts-Strogatz Distribution')
    plot_hist(G2.degree())

    plt.subplot(1, 3, 3)
    plt.title('Barabasi-Albert Distribution')
    plot_hist(G3.degree())
    # '/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/results/1_2_degreeDistribution.png'
    plt.savefig(save)

def CompareOthers(G):
    totalDegree = []
    for node in G:
        totalDegree.append(G.degree(node))
    print(round(np.mean(totalDegree))) # 6
    print(len(G.nodes)) # 165772
    ER_G = nx.gnm_random_graph(len(G.nodes), len(G.edges))
    # DegreeDistribution(ER_G, '/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/results/1_2_degreeDistribution_ER.png')
    WS_G = nx.watts_strogatz_graph(len(G.nodes), round(np.mean(totalDegree)), 0.5)
    # DegreeDistribution(WS_G, '/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/results/1_2_degreeDistribution_WS.png')
    BA_G = nx.barabasi_albert_graph(len(G.nodes), round(np.mean(totalDegree))-1)
    DegreeDistribution(ER_G, WS_G, BA_G, '/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/results/1_2/1_2_degreeDistributionCompare.png')

def Exercise_1_3(fileCollections):
    files = os.listdir(fileCollections)
    print(files)
    # with date
    wholeData = {}
    for file in files:
        print('start to process: ', file)
        G = nx.read_graphml(fileCollections+file)
        IG = ig.Graph.Read_GraphML(fileToRead + file)
        totalStrengthList = G.degree(weight='weight')
        totalDegree = []
        for node in G:
            totalDegree.append(G.degree(node))
        totalStrength = [node[1] for node in totalStrengthList]
        wholeData[file] = [len(G.nodes), len(G.edges), nx.density(G), nx.average_clustering(G), np.sum(totalDegree)/len(G.nodes), max(totalDegree), np.mean(np.sum(totalStrength)), IG.average_path_length(), IG.diameter()]
        print('done with: ', file)
    with open('/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/results/'+'Exercise_1_3.txt', 'w') as fw:
        for i in wholeData:
            fw.write(i)
            fw.write('\n')
            fw.write(str(wholeData[i]))
            fw.write('\n')
    print("done")

def setAnd(list1, list2, list3):
    print(list1)
    print(list2)
    print(list3)
    return set(list1)&set(list2)&set(list3)


if __name__ == '__main__':
    # fileCollections = '/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/preprocess/'
    # Preprocess(fileCollections)
    # ChooseWeek('/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/preprocess/')
    # DegreeDistribution(ReadGraph('/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/preprocess/GSCC-2013-12-02_to_2013-12-08.graphml'), '/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/totalDegreeDistribution.png')
    # CompareOthers(ReadGraph('/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/preprocess/GSCC-2013-12-02_to_2013-12-08.graphml'))
    # Exercise_1_3(fileCollections)
    degree = '24778	1056959	4614011	4373184	4195093	3183164	5233086	4987284	309431	5314986'
    close = '24778	4614011	4195093	5237354	5314986	5298660	1056959	5235274	4726253	4872256'
    between = '24778	4987284	5056151	4614011	1056959	4872256	4373184	4048274	4886282	4611498'
    eigen = '4987284	717202	5275726	5310061	24778	5320009	5199371	5295555	5376329	5327566'
    # print(setAnd(degree.split(), close.split(), between.split(), eigen.split()))
    eigen2 = '46606	3456919	3454412	24778	4411214	4155875	4416204	4086705	4293378	3233393'
    eigen3 = '24778	3233393	4086210	4086705	4778790	717202	4293378	3181659	4790043	4868615'
    print(setAnd(eigen.split(), eigen2.split(), eigen3.split()))


