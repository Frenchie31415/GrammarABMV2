import networkx as nx
import pylab as plt
from networkx.drawing.nx_agraph import graphviz_layout
import pygraphviz as pgv
import itertools

class PossibleProvenanceMachine:
    def __init__(self):
        self.g = None

    def get_ub(self,b):
        return 2*b
    
    def get_lb(self,a):
        if a % 3 == 0:
            return int(a/3)
        else:
            return a
        
    def get_max_depth(self,a,b):
        diff = b - a
        if diff <= 10:
            return 3 * diff
        else:
            return diff
        
    def add_node(self,number):
        if number in range(self.lb,self.ub):
            if self.g.has_node(number) == False:
                self.g.add_node(number)        

    def calc_graph(self,fr,to):
        #Assume fr < to
        a = fr
        b = to

        #If contradiction, swap vals
        if to < fr:
            a = to
            b = fr

        self.lb = self.get_lb(a)
        self.ub = self.get_ub(b)
        self.md = self.get_max_depth(a,b)
        self.g = nx.DiGraph()
        
        self.g.add_node(fr,fillcolor='green')
        self.g.add_node(to,fillcolor='red')

        self.explore_node(fr,to)

        paths = list(nx.all_simple_paths(self.g,fr,to))
        nodes_in_paths = list(set(list(itertools.chain.from_iterable(paths))))

        print(nodes_in_paths)
        nodes = list(self.g.nodes)
        
        for node in nodes:
            if node not in nodes_in_paths:
                self.g.remove_node(node)

        #A = nx.nx_agraph.to_agraph(self.g)
        #A.layout(prog='dot')
        #A.draw('test4.png')
        #print(A.to_string())

        #BFS ayclic tree search
        return None
    
    def explore_node(self,num,target):
        #Try adding
        if(self.is_valid(num,num+1)):
            self.add_node(num+1)
            self.g.add_edge(num,num+1)
            self.g[num][num+1]['weight'] = 1
            if num+1 != target: #If not final state
                self.explore_node(num+1,target)
        if(self.is_valid(num,num-1)):
            self.add_node(num-1)
            self.g.add_edge(num,num-1)
            self.g[num][num-1]['weight'] = 2
            if num-1 != target:
                self.explore_node(num-1,target)
        if(self.is_valid(num,3*num)):
            self.add_node(3*num)
            self.g.add_edge(num,3*num)
            self.g[num][3*num]['weight'] = 3
            if 3*num != target:
                self.explore_node(3*num,target)
        if((self.is_valid(num,int(num/2))) and (num % 2 == 0)):
            self.add_node(int(num/2))
            self.g.add_edge(num,int(num/2))
            self.g[num][int(num/2)]['weight'] = 4
            if int(num/2) != target:
                self.explore_node(int(num/2),target)

    def is_valid(self,fr,to):
        in_bounds = to in range(self.lb,self.ub+1)
        g_copy = self.g.copy()
        g_copy.add_edge(fr,to)
        is_dag = nx.is_directed_acyclic_graph(g_copy)
        return in_bounds and is_dag
    
    def add_one_edge(self,fr,to):
        self.g[fr][to]['weight'] = 1

    def subtract_one_edge(self,fr,to):
        self.g[fr][to]['weight'] = 2
    
    def multiply_by_three_edge(self,fr,to):
        self.g[fr][to]['weight'] = 3

    def half_edge(self,fr,to):
        self.g[fr][to]['weight'] = 4
    
    def get_graph(self):
        return self.g

if __name__ == '__main__':
    pp = PossibleProvenanceMachine()
    pp.calc_graph(3,5)
    