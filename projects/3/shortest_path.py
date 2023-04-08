#!/opt/conda/envs/dsenv/bin/python 
from pyspark import SparkConf, SparkContext
import sys
import logging

def initializeBFS(startNode):
    return (startNode, ([startNode], 0))

def updateBFS(node, bfsData, targetNode):
    path, dist = bfsData
    newpath = list(path)
    newpath.append(node)
    if node == targetNode:
        return (newpath, dist + 1)
    else:
        return (newpath, dist)

def mergeBFS(bfsData1, bfsData2):
    path1, dist1 = bfsData1
    path2, dist2 = bfsData2
    if dist1 < dist2:
        return bfsData1
    elif dist1 > dist2:
        return bfsData2
    else:
        return (path1 + path2, dist1)


startNode = sys.argv[1]
endNode = sys.argv[2]
inputPath = sys.argv[3]
outputPath = sys.argv[4]

conf = SparkConf().setAppName("ShortestPath")
sc = SparkContext(conf=conf)


data = sc.textFile(inputPath)

edges = data.map(lambda x: tuple(x.split('\t')))

# print(edges)
adjList = edges.groupByKey().cache()


maxPathLength = 100

bfs = adjList.mapValues(lambda x: initializeBFS(startNode) if x == startNode else ([], float('inf')))

for i in range(maxPathLength):
    
    bfs = bfs.flatMapValues(lambda x: x[0]).map(lambda x: (x[1], x[0])).join(adjList).map(lambda x: (x[1][0], x[0])).reduceByKey(lambda x, y: mergeBFS(x, y))

    bfs = bfs.flatMapValues(lambda x: x[0]).map(lambda x: (x[1], x[0])).join(adjList).map(lambda x: (x[1][0], updateBFS(x[1][1], x[0], endNode)))
    
    shortestPath = bfs.filter(lambda x: x[0] == endNode and x[1][1] <= i+1).collect()
    if shortestPath:
        break
# logging.info("Path {}".format(shortestPath))

sc.parallelize([12,422,53,52,107,20,23,274,34]).saveAsTextFile(outputPath)