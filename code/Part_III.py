from __future__ import division
import pandas as pd
import numpy as np
import networkx as nx
import os
import igraph as ig

fileToWrite = '/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/results/3_2/'
fileToRead = '/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/preprocess/'

def Exercise_3_2(filePath, nodeList):
    G = nx.read_graphml(filePath)
    nodeDict = {}
    for node in nodeList:
        if node in G:
            nodeInStrength = G.in_degree(node, weight='qty')
            nodeOutStrength = G.out_degree(node, weight='qty')
            nodeTotalStrength = G.degree(node, weight='qty')
            F = (nodeOutStrength - nodeInStrength)/nodeTotalStrength
            nodeDict[node] = F
        else:
            print('not exist: ', node, ', in ', filePath)
            nodeDict[node] = None
    return nodeDict

def another_ten(deg_dist):
    newDict = dict(sorted(deg_dist.items(), key=lambda item: item[1], reverse=True)[:10])
    return newDict

def nx_score_eigen(G):
    print('calculating eigenvector')
    return nx.eigenvector_centrality_numpy(G, weight='qty')

if __name__ == '__main__':
    # with open(fileToWrite+'result.txt', 'w') as fw:
    #     list1 = '46606	3456919	3454412	24778	4411214	4155875	4416204	4086705	4293378	3233393'
    #     fw.write('2013-09-30_to_2013-10-06\n')
    #     fw.write(str(Exercise_3_2(fileToRead+'GSCC-2013-09-30_to_2013-10-06.graphml', list1.split())))
    #     fw.write('\n')
    #     # print()
    #     list2 = '24778	3233393	4086210	4086705	4778790	717202	4293378	3181659	4790043	4868615'
    #     fw.write('2013-11-04_to_2013-11-10\n')
    #     fw.write(str(Exercise_3_2(fileToRead+'GSCC-2013-11-04_to_2013-11-10.graphml', list2.split())))
    #     fw.write('\n')
    #     # print(Exercise_3_2(fileToRead+'GSCC-2013-11-25_to_2013-12-01.graphml', list2.split()))
    #     list3 = '4987284	717202	5275726	5310061	24778	5320009	5199371	5295555	5376329	5327566'
    #     fw.write('2013-11-25_to_2013-12-01\n')
    #     fw.write(str(Exercise_3_2(fileToRead+'GSCC-2013-11-25_to_2013-12-01.graphml', list3.split())))
    #     fw.write('\n')
    #     # print(Exercise_3_2(fileToRead+'GSCC-2013-11-04_to_2013-11-10.graphml', list3.split()))
    with open(fileToWrite+'result_first.txt', 'w') as fw:
        nodeString = '4987284	717202	5275726	5310061	24778	5320009	5199371	5295555	5376329	5327566'
        nodeList = nodeString.split()
        files = os.listdir(fileToRead)
        files = sorted(files)
        print(files)
        for file in files:
            # fw.write(file+'\n')
            fw.write(str(list(Exercise_3_2(fileToRead + file, nodeList).values())).replace('[', '').replace(']', ''))
            fw.write('\n')