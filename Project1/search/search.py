# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from util import PriorityQueue
from util import Queue
from util import Stack
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    """
        > path contains List to store final sequence of directions 
        > explored contains states we have already visited
        > toBeExplored contains states that have been placed 
        in the Queue and are waiting to be explored
    """
    path = []           # list to store sequence of directions 
    explored = []       # list with states we have already visited
    frontier = Stack()
    frontier.push((problem.getStartState(), path))
    while True:
        if frontier.isEmpty():
            return []

        node = (frontier.pop())     # node = (state, path)
        if problem.isGoalState(node[0]):
            return node[1]

        explored.append(node[0])
        successors = problem.getSuccessors(node[0])
        for child, direction, cost in successors:
            if child not in explored:
                childPath = node[1].copy()
                childPath.append(direction)
                frontier.push((child, childPath))

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""

    """
        > path contains List to store final sequence of directions 
        > explored contains states we have already visited
        > toBeExplored contains states that have been placed 
        in the Queue and are waiting to be explored
    """
    path = []           # list to store sequence of directions 
    explored = []       # list with states we have already visited
    toBeExplored = []   # list with states that have been placed in
                        # the Queue and are waiting to be explored
    frontier = Queue()
    frontier.push((problem.getStartState(), path))
    while True:
        if frontier.isEmpty():
            return []

        node = (frontier.pop())     # node = (state, path)
        if problem.isGoalState(node[0]):
            return node[1]

        explored.append(node[0])
        successors = problem.getSuccessors(node[0])
        for child, direction, cost in successors:
            if child not in explored and child not in toBeExplored:
                toBeExplored.append(child)
                childPath = node[1].copy()
                childPath.append(direction)
                frontier.push((child, childPath))

        # removes state we just visited from toBeExplored list
        toBeExplored.pop(0)

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""

    """
        > path contains List to store final sequence of directions 
        > explored contains states we have already visited
        > toBeExplored contains states that have been placed 
        in the Queue and are waiting to be explored
    """
    path = []           # list to store sequence of directions 
    explored = []       # list with states we have already visited
    toBeExplored = []   # list with states that have been placed in
                        # the Queue and are waiting to be explored
    frontier = PriorityQueue()
    frontier.push((problem.getStartState(), path, 0), 0)
    while True:
        if frontier.isEmpty():
            return []

        while True:
            node = (frontier.pop())
            if node[0] not in explored:
                break

        if problem.isGoalState(node[0]):
            return node[1]

        explored.append(node[0])

        successors = problem.getSuccessors(node[0])
        for child, path, cost in successors:
            successorPath = node[1].copy()
            successorPath.append(path)
            successorPathCost = node[2]
            successorPathCost += cost
            if child not in explored and child not in toBeExplored:
                toBeExplored.append(child)
                frontier.push((child, successorPath, successorPathCost), successorPathCost)
            elif child in toBeExplored:
                frontier.push((child, successorPath, successorPathCost), successorPathCost)

        if len(toBeExplored) != 0:
            toBeExplored.pop(0)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    frontier = PriorityQueue()
    path = []
    node = (problem.getStartState(), path, 0, 0)
    frontier.push(node, node[3])
    explored = []
    toBeExplored = []
    while True:
        if frontier.isEmpty():
            return []

        while node[0] in explored:
            node = (frontier.pop())

        if problem.isGoalState(node[0]):
            return node[1]
        explored.append(node[0])

        possibleSuccessors = problem.getSuccessors(node[0])
        for successor in possibleSuccessors:
            if successor[0] not in explored and successor[0] not in toBeExplored:
                toBeExplored.append(successor[0])
                successorPath = node[1].copy()
                successorPath.append(successor[1])
                successorPathCost = node[2]
                successorPathCost += successor[2]
                heuristicValue = heuristic(successor[0], problem)
                successorAstarCost = successorPathCost + heuristicValue
                successorNode = (successor[0], successorPath, successorPathCost, successorAstarCost)
                frontier.push(successorNode, successorNode[3])
            elif successor[0] in toBeExplored:
                successorPath = node[1].copy()
                successorPath.append(successor[1])
                successorPathCost = node[2]
                successorPathCost += successor[2]
                heuristicValue = heuristic(successor[0], problem)
                successorAstarCost = successorPathCost + heuristicValue
                successorNode = (successor[0], successorPath, successorPathCost, successorAstarCost)
                frontier.push(successorNode, successorNode[3])
        if len(toBeExplored) != 0:
            toBeExplored.pop(0)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
