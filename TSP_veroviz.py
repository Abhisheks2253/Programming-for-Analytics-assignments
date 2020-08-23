
import pandas as pd
import numpy as np
import csv
import random
import math
import time
import veroviz as vrv
vrv.checkVersion()


# Bounding Region: 
# [There is no bounding region defined] 
 
#Nodes selected here are the house locations of UB students in south campus

# Nodes: 
nodesArray = [ 
    {'id': 0, 'lat': 42.953791989013865, 'lon': -78.8273334503174, 'altMeters': 0.0, 'nodeName': 'Home1', 'nodeType': 'Home', 'popupText': 'Home1', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'red', 'leafletIconText': '0', 'cesiumIconType': 'pin', 'cesiumColor': 'red', 'cesiumIconText': '0', 'elevMeters': None},
    {'id': 1, 'lat': 42.95012477510882, 'lon': -78.82988691329957, 'altMeters': 0.0, 'nodeName': 'Customer1', 'nodeType': 'Customer', 'popupText': 'Customer1', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '1', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '1', 'elevMeters': None},
    {'id': 2, 'lat': 42.950870799924395, 'lon': -78.82994055747987, 'altMeters': 0.0, 'nodeName': 'Customer2', 'nodeType': 'Customer', 'popupText': 'Customer2', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '2', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '2', 'elevMeters': None},
    {'id': 3, 'lat': 42.95160896294695, 'lon': -78.8299083709717, 'altMeters': 0.0, 'nodeName': 'Customer3', 'nodeType': 'Customer', 'popupText': 'Customer3', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '3', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '3', 'elevMeters': None},
    {'id': 4, 'lat': 42.9524020856897, 'lon': -78.82976889610292, 'altMeters': 0.0, 'nodeName': 'Customer4', 'nodeType': 'Customer', 'popupText': 'Customer4', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '4', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '4', 'elevMeters': None},
    {'id': 5, 'lat': 42.9535485618855, 'lon': -78.83108854293825, 'altMeters': 0.0, 'nodeName': 'Customer5', 'nodeType': 'Customer', 'popupText': 'Customer5', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '5', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '5', 'elevMeters': None},
    {'id': 6, 'lat': 42.95441233121331, 'lon': -78.82885694503786, 'altMeters': 0.0, 'nodeName': 'Customer6', 'nodeType': 'Customer', 'popupText': 'Customer6', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '6', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '6', 'elevMeters': None},
    {'id': 7, 'lat': 42.955527360964176, 'lon': -78.8293719291687, 'altMeters': 0.0, 'nodeName': 'Customer7', 'nodeType': 'Customer', 'popupText': 'Customer7', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '7', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '7', 'elevMeters': None},
    {'id': 8, 'lat': 42.95277115912484, 'lon': -78.82729053497314, 'altMeters': 0.0, 'nodeName': 'Customer8', 'nodeType': 'Customer', 'popupText': 'Customer8', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '8', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '8', 'elevMeters': None},
    {'id': 9, 'lat': 42.95306170474017, 'lon': -78.82376074790956, 'altMeters': 0.0, 'nodeName': 'Customer9', 'nodeType': 'Customer', 'popupText': 'Customer9', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '9', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '9', 'elevMeters': None},
    {'id': 10, 'lat': 42.954702869080606, 'lon': -78.82411479949953, 'altMeters': 0.0, 'nodeName': 'Customer10', 'nodeType': 'Customer', 'popupText': 'Customer10', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '10', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '10', 'elevMeters': None},
    {'id': 11, 'lat': 42.96257827841771, 'lon': -78.81495237350465, 'altMeters': 0.0, 'nodeName': 'Customer11', 'nodeType': 'Customer', 'popupText': 'Customer11', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '11', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '11', 'elevMeters': None},
    {'id': 12, 'lat': 42.95998727793415, 'lon': -78.81593942642213, 'altMeters': 0.0, 'nodeName': 'Customer12', 'nodeType': 'Customer', 'popupText': 'Customer12', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '12', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '12', 'elevMeters': None},
    {'id': 13, 'lat': 42.95871529231204, 'lon': -78.8209390640259, 'altMeters': 0.0, 'nodeName': 'Customer13', 'nodeType': 'Customer', 'popupText': 'Customer13', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '13', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '13', 'elevMeters': None},
    {'id': 14, 'lat': 42.95772595198201, 'lon': -78.8264322280884, 'altMeters': 0.0, 'nodeName': 'Customer14', 'nodeType': 'Customer', 'popupText': 'Customer14', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '14', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '14', 'elevMeters': None},
    {'id': 15, 'lat': 42.94919812116764, 'lon': -78.82156133651735, 'altMeters': 0.0, 'nodeName': 'Customer15', 'nodeType': 'Customer', 'popupText': 'Customer15', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '15', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '15', 'elevMeters': None},
    {'id': 16, 'lat': 42.94902535363563, 'lon': -78.82477998733522, 'altMeters': 0.0, 'nodeName': 'Customer16', 'nodeType': 'Customer', 'popupText': 'Customer16', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '16', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '16', 'elevMeters': None},
    {'id': 17, 'lat': 42.9470620521607, 'lon': -78.8255524635315, 'altMeters': 0.0, 'nodeName': 'Customer17', 'nodeType': 'Customer', 'popupText': 'Customer17', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '17', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '17', 'elevMeters': None},
    {'id': 18, 'lat': 42.948177215081266, 'lon': -78.81761312484743, 'altMeters': 0.0, 'nodeName': 'Customer18', 'nodeType': 'Customer', 'popupText': 'Customer18', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '18', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '18', 'elevMeters': None},
    {'id': 19, 'lat': 42.94531858795796, 'lon': -78.81772041320802, 'altMeters': 0.0, 'nodeName': 'Customer19', 'nodeType': 'Customer', 'popupText': 'Customer19', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '19', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '19', 'elevMeters': None},
    {'id': 20, 'lat': 42.94759607636185, 'lon': -78.82166862487794, 'altMeters': 0.0, 'nodeName': 'Customer20', 'nodeType': 'Customer', 'popupText': 'Customer20', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '20', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '20', 'elevMeters': None},
    {'id': 21, 'lat': 42.95664237051177, 'lon': -78.81536006927492, 'altMeters': 0.0, 'nodeName': 'Customer21', 'nodeType': 'Customer', 'popupText': 'Customer21', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '21', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '21', 'elevMeters': None},
    {'id': 22, 'lat': 42.951773870497476, 'lon': -78.82151842117311, 'altMeters': 0.0, 'nodeName': 'Customer22', 'nodeType': 'Customer', 'popupText': 'Customer22', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '22', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '22', 'elevMeters': None},
    {'id': 23, 'lat': 42.96267249456109, 'lon': -78.82892131805421, 'altMeters': 0.0, 'nodeName': 'Customer23', 'nodeType': 'Customer', 'popupText': 'Customer23', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '23', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '23', 'elevMeters': None},
    {'id': 24, 'lat': 42.96050548675996, 'lon': -78.82604598999025, 'altMeters': 0.0, 'nodeName': 'Customer24', 'nodeType': 'Customer', 'popupText': 'Customer24', 'leafletIconPrefix': 'glyphicon', 'leafletIconType': 'info-sign', 'leafletColor': 'blue', 'leafletIconText': '24', 'cesiumIconType': 'pin', 'cesiumColor': 'blue', 'cesiumIconText': '24', 'elevMeters': None},
]
nodesDF = pd.DataFrame(nodesArray)


# nodesDF

# To create a view of the nodes selected 
# vrv.createLeaflet(nodes = nodesDF, boundingRegion=None)


# 2. Get time and distance matrices
costDict = [timeSec, distMeters] = vrv.getTimeDist2D(nodes = nodesDF,
                                          routeType = 'euclidean2D',
                                          speedMPS = vrv.convertSpeed(25, 'miles', 'hr', 'meters', 'second'))


# vrv.convertSpeed?
# costDict
# This dictionary that we get has both time and distance in it; timeSec and distMeters


# Optional, just to view the data in a table:
# costDF = vrv.convertMatricesDictionaryToDataframe(distMeters)

# costDF.to_csv('distance_matrix.csv')


# Nearest neighbour tsp function as discussed in class

def solve_tsp_nn(startNode, costDict, nodesDF): 
    """
    This function computes a "nearest neighbor" solution to a TSP.
    
    Inputs
    ------
    startNode: Integer, indicating the node where the salesperson begins (and ends) the route
    
    costDict: VeRoViz time or distance dictionary.
    
    nodesDF: VeRoViz nodes dataframe
    
    Returns
    -------
    An ordered list of nodeIDs specifying a TSP route.
    """
    
    # Solve the TSP with a "nearest neighbor" heuristic
    nn_route = []

    # Start our route by visiting the startNode
    nn_route.append(startNode)

    # Initialize a list of unvisited nodes
    unvisitedNodes = list(nodesDF[nodesDF['id'] != startNode]['id'])

    # Let i represent our "current" location:
    i = startNode

    while len(unvisitedNodes) > 0:
        # Initialize minTime to a huge value
        minTime = float('inf')

        # Find the nearest unvisited node to our current node:
        for j in unvisitedNodes:
            if (costDict[i,j] < minTime):
                nextNode = j
                minTime = costDict[i,j]

        # Update our salesperson's location
        i = nextNode

        # Append nextNode to our route:
        nn_route.append(nextNode)

        # Remove nextNode from our list of unvisitedNodes:
        unvisitedNodes.remove(nextNode)

    nn_route.append(startNode)

    return nn_route

nn_route = solve_tsp_nn(0, distMeters, nodesDF)


# myArcs = vrv.createArcsFromNodeSeq(nodeSeq = nn_route, nodes = nodesDF)
# myArcs


# View our nodes and bounding region: (No bounding region specified here)
# vrv.createLeaflet(nodes = nodesDF, arcs = myArcs)



#tsp_cost function will return the total cost of our route, in this example
#we have timeSec and distMeters as the costs metrics

def tsp_cost(route, costDict):
    cost = 0
    
    i = route[0]
    for j in route[1:]:
        cost += costDict[i,j]
        i = j
        
    cost += costDict[i, route[0]]
    
    return cost

# tsp_cost(solve_tsp_nn(0, distMeters, nodesDF), distMeters) 


def tsp_neighbor(route):
    # You should document this function to explain what's happening
    
    a = random.randint(0,len(nn_route)-3)
    b = random.randint(a+1, len(nn_route)-2)
    
    newRoute = []
    newRoute.extend(route[0:a])
    
    subtour = route[a:b+1]
    subtour.reverse()
    newRoute.extend(subtour)
    
    newRoute.extend(route[b+1:len(route)-1])
    
    newRoute.append(newRoute[0])
    
    return newRoute


# tsp_cost(solve_tsp_nn(0, distMeters, nodesDF), distMeters)


# Get the code runtime -- This will give the total runtime
def get_runtime():
    start_time = time.time()
#     main()
    runtime = time.time() - start_time
    return runtime   

# Simulated Annealing 

def solveTSP_SA(nodesDF, costDict, timeLimit):
    #Initialization
    t0 = 10000
    i = 100
    delta = 1
    T_final = 1000
    cutofftime = timeLimit
    
    X_0 = solve_tsp_nn(0, distMeters, nodesDF)
    X_cur = X_0
    Z_cur = tsp_cost(X_cur, distMeters)
    T_cur = t0
    X_best = X_cur
    Z_best = Z_cur
    
    #Phase 2 and 3 - Simulated Annealing
    for i in range(i):        
        X_count = tsp_neighbor(X_cur)
        if(tsp_cost(X_count,distMeters) <= Z_cur):
            X_cur = X_count
            Z_cur = tsp_cost(X_count,distMeters)
        else:
            del_C = Z_cur - tsp_cost(X_count,distMeters)
            if(random.randint(0,1) <= math.exp(del_C/T_cur)):
                X_cur = X_count
                Z_cur = tsp_cost(X_count,distMeters)
        if(tsp_cost(X_cur,distMeters) < Z_best):
            Z_best = tsp_cost(X_cur,distMeters)
            X_best = X_cur
        T_cur = T_cur - delta
        if((T_cur < T_final) or (get_runtime() < cutofftime)):
            break
    
    #Create assignments DF
    assignmentsDF = vrv.createAssignmentsFromNodeSeq2D(
        nodeSeq          = X_best,
        nodes            = nodesDF,
        serviceTimeSec   = 20.0,
        odID             = 1,
        objectID         = 'UB truck',
        modelFile        = 'veroviz/models/car_blue.gltf',
        modelScale       = 100,
        modelMinPxSize   = 75,
        startTimeSec     = 65.0,
        expDurationArgs  = None,
        routeType        = 'fastest',
        speedMPS         = None,
        leafletColor     = 'blue',
        leafletWeight    = 3,
        leafletStyle     = 'dashed',
        leafletOpacity   = 0.8,
        useArrows        = True,
        cesiumColor      = 'blue',
        cesiumWeight     = 3,
        cesiumStyle      = 'solid',
        cesiumOpacity    = 0.8,
        dataProvider     = 'ORS-online',
        dataProviderArgs = {'APIkey' : "5b3ce3597851110001cf6248974295e9c364418fa4e3a941dc7560e5"})
    vrv.createLeaflet(nodes=nodesDF, arcs=assignmentsDF)
    return assignmentsDF
#     return Z_best

# solveTSP_SA(nodesDF, distMeters, 20)


# assignmentDF = solveTSP_SA(nodesDF, distMeters, 20)

# vrv.createLeaflet(nodes=nodesDF, arcs=assignmentDF)
