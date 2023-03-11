import networkx as nx
from InferenceMachine import InferenceMachine

#Get working for simple example. Then graph search
def order_invariance(g,source,target):
    paths = list(nx.all_simple_paths(g,source,target))
    trans = []
    
    for path in paths:
        path_trans = []
        for i in range(0,len(path)-1):
            ind_trans = InferenceMachine().infere(path[i],path[i+1])
            path_trans.append(ind_trans)
        trans.append(path_trans)

    #For now selecting path that uses higher numbers
    #Compare all paths
    for i in range(0,len(trans)):
        for j in range(i+1,len(trans)):
            if sorted(trans[i]) == sorted(trans[j]):
                p1 = paths[i]
                p2 = paths[j]

                if max(p1) > max(p2):
                    to_remove = p1[1:len(p1)-1]
                else:
                    to_remove = p2[1:len(p2)-1]
                
                for node in to_remove:
                    g.remove_node(node)
                
        
        


        



    #Properties of order invariance
        

if __name__ == '__main__':
    g = nx.DiGraph()
    g.add_node(6)
    g.add_node(18)
    g.add_node(9)
    g.add_node(3)
    g.add_edge(6,18)
    g.add_edge(18,9)
    g.add_edge(6,3)
    g.add_edge(3,9)
    order_invariance(g,6,9)