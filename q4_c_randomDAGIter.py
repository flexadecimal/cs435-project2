from q4_b_directedgraphclass import DAG
from random import random, randrange

def createRandomDAGIter(n):
  graph = DAG()
  node_vals = [str(num) for num in range(n)]
  # create nodes
  for val in node_vals:
    graph.addNode(val)
  # for DAG - using the property that the adjacency matrix of a DAG is lower
  # triangular - i.e DAG has edge A->B if A < B.
  enum_nodes = sorted(list(enumerate(graph.nodes())))
  for a_idx, a in enum_nodes:
    for b_idx, b in enum_nodes:
      if random() > 0.5 and a_idx < b_idx:
        graph.addDirectedEdge(a, b)
  return graph


if __name__ == '__main__':
  n = 10
  graph = createRandomDAGIter(n)
  print(graph)