class Node:
    def __init__(self,state,parent,actions,totalcost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.totalcost=totalcost
def actionsequence(graph,initialstate, goalstate):
    solution =[goalstate]
    currentparent = graph[goalstate].parent
    while currentparent != None:
        solution.append(currentparent)
        currentparent = graph[currentparent].parent
    solution.reverse()
    return solution
def BFSCost():
    initialstate = "Arad"
    goalstate = "Bucharest"
    graph={
       'Oradea' : Node('Oradea',None,['Zerind','Sibiu'],[71,151] ),
        'Zerind' : Node('Zerind',None,['Arad', 'Oradea'],[75,71 ]),
        'Arad' : Node('Arad',None,['Zerind','Timisoara','Sibiu'],[75,118,140] ),
        'Sibiu' : Node('Sibiu',None,['Fagaras','Rimnicu Vilcea','Oradea','Arad'],[99,80,151,140] ),
        'Fagaras' : Node('Fagaras',None,['Sibiu','Bucharest'],[99,211] ),
        'Bucharest' : Node('Bucharest',None,['Fagaras','Pitesti','Urziceni','Giurgiu'],[211,101,85,90] ),
        'Pitesti' : Node('Pitesti',None,['Rimnicu Vilcea','Bucharest','Craiova'],[97,101,138] ),
        'Urziceni' : Node('Urziceni',None,['Bucharest','Hirsova','Vaslui'],[85,98,142] ),
        'Hirsova' : Node('Hirsova',None,['Urziceni','Eforie'],[98,86] ),
        'Timisoara':Node('Timisoara',None,['Lugoj','Arad'],[111,118]),
        'Lugoj':Node('Lugoj',None,['Mehadia','Timisoara'],[70,111]),
        'Mehadia':Node('Mehadia',None,['Drobeta','Lugoj'],[75,70]),
        'Rimnicu Vilcea':Node('Rimnicu Vilcea',None,['Sibiu','Pitesti'],[70,111]),
        'Drobeta' : Node('Drobeta',None,['Craiova','Mehadia'],[120,75] ),
        'Craiova' : Node('Craiova',None,['Pitesti','Rimnicu Vilcea'],[138,146] ),
        'Eforie' : Node('Eforie',None,['Hirsova'],[86] ),
        'Vaslui' : Node('Vaslui',None,['Urziceni','Iasi'],[142,92] ),
        'Iasi' : Node('Iasi',None,['Vaslui','Neamt'],[92,87] ),
        'Giurgiu' : Node('Giurgiu',None,[],[]),
        'Neamt' : Node('Neamt',None,[],[] ),
        }
    frontier = [initialstate]
    explored = []
    while len(frontier) !=0:
        currentnode = frontier.pop(0)
        explored.append(currentnode)
        print(currentnode)
        for child in graph [currentnode].actions:
             if child not in frontier and child not in explored:
                  graph[child].parent = currentnode
                  if graph[child].state == goalstate:
                      return actionsequence(graph, initialstate, goalstate)
                  frontier.append(child)

solution = BFSCost()
print(solution)
        
