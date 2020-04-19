from q5_b_weightedgraphclass import WeightedGraph
from random import randint

def createRandomCompleteWeightedGraph(n):
  graph = WeightedGraph()
  node_vals = [str(num) for num in range(n)]
  # create nodes
  for val in node_vals:
    graph.addNode(val)
  # create all edges, with random weight
  limit = n
  for a in graph.nodes():
    for b in [n for n in graph.nodes() if n is not a]:
      graph.addWeightedEdge(a, b,randint(0, limit))
  return graph

if __name__ == '__main__':
  n = 10
  graph = createRandomCompleteWeightedGraph(n)
  print(graph)