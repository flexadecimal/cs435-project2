from q5_b_weightedgraphclass import WeightedGraph
from q5_c_randomweightedgraph import createRandomCompleteWeightedGraph
from q5_d_linkedlist import createLinkedList
from sys import maxsize as maxint
# to be consistent and use adjacency list, i will use dijkstras variant that uses minheap
from heapq import heappop as pop, heappush as push, heapify

class TreadmillMazeSolver:
  def __init__(self, graph):
    self.graph = graph
  def dijkstras(self, start):
    num_nodes = len(self.graph.nodes())
    distance = {node:maxint for node in self.graph.nodes()}
    distance[start] = 0
    # add all nodes to heap ordered by distance
    heap = []
    for node, dist in distance.items():
      push(heap, (dist, node))
    while len(heap) > 0:
      min_dist_node = pop(heap)[1]
      # go through all adjacent nodes
      for adj, weight in self.graph.adjacent(min_dist_node):
        edge_in_heap = (distance[adj], adj) in heap
        new_dist_lessthan_current = weight + distance[min_dist_node] < distance[adj];
        has_valid_distance = distance[min_dist_node] != maxint
        if edge_in_heap and has_valid_distance and new_dist_lessthan_current: 
          new_dist = weight + distance[min_dist_node]
          # update heap and distance
          node_idx = heap.index((distance[adj], adj))
          heap[node_idx] = (new_dist, adj)
          heapify(heap)
          distance[adj] = new_dist
    # before returning, convert maxint to None's for easy reading
    for node, dist in distance.items():
      if dist == maxint:
        distance[node] = None
    return distance
  def astar(self, start, end):
    # count variable used for local distance
    count = 0
    # distance so far: 
    def g(n):
      return count
    # distance to end: end-n, e.g. 9 - 2 = 7
    def h(n):
      return int(end.val) - int(n.val)
    # initialize distances
    distances = {node:(g(node), h(node)) for node in self.graph.nodes()}
    finalized = {node:False for node in self.graph.nodes()}
    cursor = start
    while cursor is not end:
      finalized[cursor] = True
      # update neighbors' distances
      for adj, weight in self.graph.adjacent(cursor):
        if distances[adj][0] <= distances[cursor][0]:
          distances[adj] = (distances[cursor][0] + weight, h(adj))
      # cursor is now new min of un-finalized nodes with key g+h
      not_finalized = [n for n in self.graph.nodes() if not finalized[n]]
      cursor = min(not_finalized, key=lambda n: distances[n][0] + distances[n][1])
      # increment count, used for g local heuristic
      count += 1
    return distances[end][0]
    
if __name__ == '__main__':
  n = 10000
  maze = createRandomCompleteWeightedGraph(n)
  start = maze.nodes()[0]
  end = maze.nodes()[n-1]
  solver = TreadmillMazeSolver(maze)
  print(maze, end='\n\n')
  print("Dijkstra's algorithm paths from {}:".format(start))
  print(solver.dijkstras(start), end="\n\n")
  print("A* search from {} to {}: end g-value {}".format(start, end, solver.astar(start, end)))