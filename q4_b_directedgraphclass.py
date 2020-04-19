from pprint import pformat
from q3_a_graphclass import Graph

class DAG(Graph):
  def addDirectedEdge(self, first, second):
    self.node_adj_dict[first].add(second)
  def removeDirectedEdge(self, first, second):
    self.node_adj_dict[first].remove(second)

# for testing
if __name__ == '__main__':
  pass