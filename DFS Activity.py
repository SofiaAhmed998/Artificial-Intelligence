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
def DFS():
    initialstate = 'A'
    goalstate = 'D'
    graph={
        'A':Node('A',None,['B','E','C'],None),
       'B':Node('B',None,['D','E','A'],None),
       'C':Node('C',None,['A','F','G'],None),
       'D':Node('D',None,['B','E'],None),
       'E':Node('E',None,['A','B','D'],None),
       'F':Node('F',None,['C'],None),
       'G':Node('G',None,['C'],None)}
    frontier = [initialstate]
    explored = []
    while len(frontier) !=0:
        currentnode = frontier.pop(len(frontier)-1)
        print(currentnode)
        explored.append(currentnode)
        cChild=0
        for child in graph [currentnode].actions:
             if child not in frontier and child not in explored:
                  graph[child].parent = currentnode
                  if graph[child].state == goalstate:
                      print(explored)
                      return actionsequence(graph, initialstate, goalstate)
                  cChild= cChild+1
                  frontier.append(child)
        if  cChild==0:
            del explored[len(explored)-1]
        

solution = DFS()
print(solution)


