from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import os
import igraph as ig


fileToWrite = '/coursework/'
fileToRead = '/coursework/'

def Exercise_1_1(fileCollections):
    files = os.listdir(fileCollections)
    print(files)
    # number of nodes
    nodes = []
    # number of links
    links = []
    # density
    density = []
    # Average clustering coefficient
    ACC = []
    # Average degrees (in-degree, out-degree, total degree)
    AID = []
    AOD = []
    ATD = []
    # Maximum degrees (in-degree, out-degree, total degree)
    MID = []
    MOD = []
    MTD = []
    # Average strength (in-strength, out-strength, total strength)
    AIS = []
    AOS = []
    ATS = []
    # Average path length
    APL = []
    # Diameter
    diameter = []
    for file in files:
        print('start to process: ', file)
        G = nx.read_graphml(fileCollections+file)
        IG = ig.Graph.Read_GraphML(fileToRead+file)
        # all the nodes
        nodes.append(len(G.nodes))
        # all the links
        links.append(len(G.edges))
        # density
        density.append(nx.density(G))

        inStrengthList = G.in_degree(weight='weight')
        outStrengthList = G.out_degree(weight='weight')
        totalStrengthList = G.degree(weight='weight')
        inDegree = []
        outDegree = []
        totalDegree = []
        for node in G:
            inDegree.append(G.in_degree(node))
            outDegree.append(G.out_degree(node))
            totalDegree.append(G.degree(node))
        inStrength = [node[1] for node in inStrengthList]
        outStrength = [node[1] for node in outStrengthList]
        totalStrength = [node[1] for node in totalStrengthList]
        ACC.append(nx.average_clustering(G))
        AID.append(np.sum(inDegree)/len(G.nodes))
        AOD.append(np.sum(outDegree)/len(G.nodes))
        ATD.append(np.sum(totalDegree)/len(G.nodes))
        MID.append(max(inDegree))
        MOD.append(max(outDegree))
        MTD.append(max(totalDegree))
        AIS.append(np.mean(np.sum(inStrength)))
        AOS.append(np.mean(np.sum(outStrength)))
        ATS.append(np.mean(np.sum(totalStrength)))
        apl = IG.average_path_length()
        APL.append(apl)
        damt = IG.diameter()
        diameter.append(damt)
        print('done with: ', file)

    csv_data = pd.DataFrame({
        'Number of nodes': nodes,
        'Number of links': links,
        'Density': density,
        'Average clustering coefficient': ACC,
        'Average In-Degree': AID,
        'Average Out-Degree': AOD,
        'Average Total-Degree': ATD,
        'Maximum In-Degree': MID,
        'Maximum Out-Degree': MOD,
        'Maximum Total-Degree': MTD,
        'Average In-Degree Strength': AIS,
        'Average Out-Degree Strength': AOS,
        'Average Total-Degree Strength': ATS,
        'Average path length': APL,
        'Diameter': diameter
    }).describe().T
    csv_data.to_csv(fileToWrite+'Exercise_1_1.csv')
    print("done")

if __name__ == '__main__':
    fileCollections = '/coursework/'
    Exercise_1_1(fileCollections)