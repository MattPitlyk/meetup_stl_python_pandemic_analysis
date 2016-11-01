# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:11:40 2015

@author: Matt
"""

import itertools
#import random
import networkx as nx
#import time

g = nx.read_graphml('pandemic.graphml.txt')

# dicts from city names to numbers, and from numbers to city names.
city_names_to_num = {tup[1]['label']:tup[0] for tup in g.nodes(data=True)}
city_num_to_names = {tup[0]:tup[1]['label'] for tup in g.nodes(data=True)}



def get_longest_shortest_paths(graph):
    """Get longest shortest paths in a graph.
    These are the paths with length equal to the diameter - 1.
    If there are multiple shortest paths between a pair of cities, this will
    only return one.
    """
    shortest = nx.shortest_path(graph)
    flat_shortest = [shortest[source][target] for source in shortest for target in shortest[source]]
    longest = max([len(path) for path in flat_shortest])
    return [s for s in flat_shortest if len(s) == longest]
    

    



def get_diameter(graph, stations):
    """Add edges between the stations and calculate the diameter."""
    
    # Make a copy of the graph because we're going to add edges.
    h = graph.copy()
    #print(stations)
    # Take the list of stations and add edges between them.
    for c in itertools.combinations(stations, 2):
        if c[0] in h and c[1] in h:
            h.add_edge(c[0], c[1])
        else:
            print('missing nodes' + c[0] + ' ' + c[1])
    return (nx.diameter(h), stations, len(h.edges()))
    
    
    
    
#def city_combinations(graph, cities, stations, depth, func, results):
#    """Creates combinations of stations with length equal to depth and calls func."""
#    
#    # Loop through cities.
#    for c1 in cities:
#
#        # Make copy of stations.        
#        stations2 = stations[:]
#        
#        # Make copy of cities and remove c1.
#        cities2 = cities[:]
#        stations2.append(c1)
#        cities2.remove(c1)
#        
#        # Remove neighbors of c1.
#        for c in nx.neighbors(graph, c1):   
#            try:
#                cities2.remove(c)
#            except:
#                pass
#    
#        # Check for max depth.
#        if len(stations2) == depth:
#            #print('stations2 ' + str(stations2))
#            # Reached the max depth (number of stations), so call function.
#            results.append(func(graph, stations2))
#        else:
#            # Go deeper -- add more stations to the list.
#            city_combinations(graph, cities2, stations2, depth, func, results)      
#    
    
    
#def all_stations_combos(graph, station_num=6, starting_stations=['6']):
#    """Finds diamters for graphs with all combos of station_num stations added.
#    
#    Removes neighbors after choosing each station to reduce the number
#    of combonations to try.
#    """
#    results = []
#    # Make copy of cities.    
#    cities = graph.nodes()[:]
#    stations = starting_stations[:]
#    for c in stations:
#        cities.remove(c)    
#    
#    city_combinations(graph, cities, stations, station_num, get_diameter, results)
#    return results
#    
    
    
#start = time.time()    
#res = all_stations_combos(g)
#end = time.time()
#print(end - start)

    #end = time.time()
    #total_time = end - start
    #print(total_time / 60.0)
    #print(min([tup[0] for tup in results]))
    #return results



#def add_stations(graph, cities, names=False):
#    """Adds edges to graph between each pair of cities.
#    
#    Graph and list of cities (numbers as strings or names) to place stations in.    
#    """
#    if names:
#        cities = [city_names_to_num[c] for c in cities]
#    for c in itertools.combinations(cities, 2):
#        graph.add_edge(c[0], c[1])
        
        
#    
#def all_stations_combos(graph, station_num=5, starting_stations=['6']):
#    """Finds diamters for graphs with all combos of station_num stations added.
#    
#    Removes neighbors after choosing each station to reduce the number
#    of combonations to try.
#    """
#    
#    #start = time.time()
#    results = []
#    
#    # Make copy of cities.    
#    cities1 = graph.nodes()[:]
#    stations1 = starting_stations[:]
#    for c in stations1:
#        cities1.remove(c)    
#    
#    # Loop through cities.
#    for c1 in cities1:
#
#        # Make copy of stations.        
#        stations2 = stations1[:]
#        
#        # Make copy of cities and remove c1.
#        cities2 = cities1[:]
#        stations2.append(c1)
#        cities2.remove(c1)
#        
#        # Remove neighbors of c1.
#        for c in nx.neighbors(graph, c1):   
#            try:
#                cities2.remove(c)
#            except:
#                pass
#            
#        # Loop through remaining cities.        
#        for c2 in cities2:
#            
#            # Make copy of stations.
#            stations3 = stations2[:]
#            
#            # make copy of cities and remove c2.
#            cities3 = cities2[:]
#            stations3.append(c2)
#            cities3.remove(c2)
#            
#            # Remove neightbors of c2.
#            for c in nx.neighbors(graph, c2):
#                try:
#                    cities3.remove(c)
#                except:
#                    pass
#                
#            # Make a copy of the graph because we're going to add edges.
#            h = graph.copy()
#            
#            # Take the list of cities and add edges between them.
#            print(stations3)
#            for c in itertools.combinations(stations3, 2):
#                if c[0] in h and c[1] in h:
#                    h.add_edge(c[0], c[1])
#                else:
#                    print('missing nodes' + c[0] + ' ' + c[1])
#            results.append((nx.diameter(h), stations3, len(h.edges())))
#    return results
#    
#

#def sim_stations(graph, station_num=2, iterations=1000):
#    """Simulate random placements of station_num stations and calculates the diameter.
#    Keeps a station at Atlanta which is not counted in station_num.
#    """
#    
#    # Get the list of nodes in the graph. These are integers stored as strings.
#    #nums = list(graph.nodes())
#    #nums.remove('6')
#    results = []
#    
#    start = time.time()
#    
#    for i in xrange(iterations):
#        
#        # Make a copy of the graph because we're going to add edges.
#        h = graph.copy()
#        
#        # Get the list of nodes in the graph. These are integers stored as strings.
#        nums = list(graph.nodes())
#        
#        # Remove Atlanta.
#        nums.remove('6')
#        cities = ['6']
#        
#        #random.shuffle(nums)
#        #cities = nums[:station_num - 1] + ['6']
#        #cities = [str(n) for n in cities]
#    
#        for n in xrange(station_num):
#            
#            # Shuffle remaining cities.
#            random.shuffle(nums)
#            
#            # Remove a city and add it to the list.
#            cities.append(nums.pop(0))
#            
#            # Remove all of it's neighbors.
#            for j in nx.neighbors(h, str(cities[-1])):
#                if j in nums:            
#                    nums.remove(j)
#                    
#        # Take the list of cities and add edges between them.
#        for c in itertools.combinations(cities, 2):
#            if c[0] in h and c[1] in h:
#                h.add_edge(c[0], c[1])
#            else:
#                print('missing nodes')
#        results.append((nx.diameter(h), cities, len(h.edges())))
#        
#    end = time.time()
#    total_time = end - start
#    print(total_time / 60.0)
#    print(min([tup[0] for tup in results]))
#    return results    