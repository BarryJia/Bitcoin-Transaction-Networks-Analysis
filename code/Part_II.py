from __future__ import division
import pandas as pd
import numpy as np
import networkx as nx
import os
import igraph as ig


fileToWrite = '/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/pickWeek/'
fileToRead = '/Users/jiashichao/Desktop/Edinburgh/Sem1/Data-driven_Business_and_Behaviour_Analytics/ass1/pickWeek/'

def top_ten(deg_dist):
    newDict = dict(sorted(deg_dist, key=lambda item: item[1], reverse=True)[:10])
    return [node for node in newDict]
    # return [id for id, _ in sorted(deg_dist, key = lambda p: -p[1])][:10]

def another_ten(deg_dist):
    newDict = dict(sorted(deg_dist.items(), key=lambda item: item[1], reverse=True)[:10])
    return [node for node in newDict]

def score_closeness(G):
    close = G.closeness(directed=True)
    print(close)
    return close

def nx_score_closeness(G):
    print('calculating closeness')
    return nx.closeness_centrality(G)

def nx_score_betweenness(G):
    print('calculating betweenness')
    return nx.betweenness_centrality(G, k = 10000)

def nx_score_eigen(G):
    print('calculating eigenvector')
    return nx.eigenvector_centrality_numpy(G, weight='qty')

def score_betweenness(G):
    between = G.betweenness(directed=True)
    print(between)
    return between

def Exercise_2_1(fileCollections):
    files = os.listdir(fileCollections)
    print(files)
    count = 0
    for file in files:
        count += 1
        print('start to process: ', file)
        print(str(count)+'/'+str(len(files)))
        G = nx.read_graphml(fileToRead+file)
        # IG = ig.Graph.Read_GraphML(fileToRead + file)
        # closeness = {}
        # betweenness = {}
        # print(G)
        # for i in G.nodes():
        #     closeness[i] = IG.closeness(i)
        #     betweenness[i] = IG.betweenness(i)
        # print(top_ten(G.degree()))
        # print(top_ten(closeness))
        # print(top_ten(betweenness))
        data = pd.DataFrame({
            'K': top_ten(G.degree()),
            'Closeness': top_ten(nx_score_closeness(G).items()),
            'Betweenness': top_ten(nx_score_betweenness(G).items()),
            'Eigenvector': another_ten(nx_score_eigen(G))
        }).T
        data.to_csv(fileToWrite+file.replace('graphml', 'csv').replace('GSCC-', ''))


if __name__ == '__main__':
    fileCollections = fileToRead
    Exercise_2_1(fileCollections)