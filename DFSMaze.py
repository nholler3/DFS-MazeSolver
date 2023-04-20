from pyMaze import maze,agent,COLOR;

dfsPath={}
def DFS(m):
    start=(m.rows,m.cols)
    explored=[start] #stack holding the explored nodes
    potentialpaths=[start] #stacking holding the nodes we want to explore

    while len(potentialpaths)>0: #while there are still paths to explore
        currCell=potentialpaths.pop() #current cell is popped from the potential paths 
        if currCell == (1,1): #if the current cell is the goal then break 
            break
        for d in 'ESNW': #explore in each direction 
            if m.maze_map[currCell][d]==True: #checking all directions and if d in whatever direction is true
                if d=='E': #if the direction is east the child cell is set equal to the node to the right
                    childCell=(currCell[0],currCell[1]+1) 
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1, currCell[1])
                elif d=='W':
                    childCell=(currCell[0], currCell[1]-1)
                if childCell in explored: #if we have visited the child node continue on
                    continue 
                #otherwise append the child node to both explored and potential paths
                explored.append(childCell)
                potentialpaths.append(childCell)
                dfsPath[childCell]=currCell #all paths taken in reverse from goal to start 
    fwdPath={} #reverse the order of dfsPath to get the correct forward path
    cell=(1,1)#set cell = to the goal
    while cell!=start: #while cell is not = to start work down dfs path and push the curreuntil you get to start 
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return fwdPath


#create maze
m=maze(5,5)
m.CreateMaze()
path=DFS(m)
a=agent(m,footprints=True)#makes the path taken by DFS visible
m.tracePath({a:path}) #we want the agent to follow path 

m.run()