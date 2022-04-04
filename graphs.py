# implementation of graphs with Adjacency Matrix, Adjacency List, and OOP


class Graphs():
    def __init__(self):
        pass

    def adjLst(self, length):
        # user inputs number of nodes in their graph
        # for that number of nodes the user is asked if they are linked to any other nodes
        # this is used to create an adjacency matrix which is returned
        graph = []
        counter = 0
        for node in range(length):
            nodeList = []
            counter += 1
            counter2 = 0
            while counter2 < length: 
                while True:
                    answer = input("is node " + str(node) + " connected to node " + str(counter2)+ "? (y/n)")
                    if answer == "y":
                        nodeList.append([1])
                        break
                    if answer == "n":
                        nodeList.append([0])
                        break
                    else:
                        print("incorrect input, try again")
                counter2 += 1
            graph.append(nodeList)
        return graph

graphs = Graphs
print(graphs.adjLst(0, 5))

