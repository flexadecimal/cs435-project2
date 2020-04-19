from pprint import pformat
from q3_a_graphclass import Graph

# now use tuple of (dest, weight) to represent edges
class WeightedGraph(Graph):
  def addWeightedEdge(self, first, second, weight):
    self.node_adj_dict[first].add((second, weight))
  def removeWeightedEdge(self, first, second):
    self.node_adj_dict[first].remove((second, weight))

# for testing
if __name__ == '__main__':
  pass