# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"

        # food score
        foodList = newFood.asList()
        
        # if there is no food left game has ended
        if not foodList:
            return successorGameState.getScore()

        foodDistance = [manhattanDistance(newPos, food) for food in foodList]

        # increase score based on how close the food is
        if foodDistance:
            closestFoodScore = 1/float(min(foodDistance))
            furthestFoodScore = 1/float(max(foodDistance))

        # ghost score
        ghostDistance = [manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates]
        
        # decrease score based on how close the ghosts are
        closestGhostScore = 0
        if ghostDistance:
            if min(ghostDistance) == 0:
                closestGhostScore = -999
            else:
                closestGhostScore = -1/float(min(ghostDistance))

        if len(foodList) != 1:
            return successorGameState.getScore() + closestFoodScore + furthestFoodScore + closestGhostScore
        else:
            return successorGameState.getScore() + closestFoodScore + closestGhostScore


def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def minimax(self, gameState: GameState, agent: int, depth: int):

        # if game has ended or we have reached the end of the tree, return evaluation
        if (gameState.isWin() or gameState.isLose() or depth == 0):
            return (self.evaluationFunction(gameState),)

        # pacman is max player
        if agent == 0:
            maxEval = float('-inf')
            actionList = gameState.getLegalActions(agent)

            for action in actionList:
                successor = gameState.generateSuccessor(agent, action)
                successorEval = self.minimax(successor, agent + 1, depth)

                if successorEval[0] > maxEval:
                    maxEval = successorEval[0]
                    bestAction = action

            return (maxEval, bestAction)
        # ghosts are min player
        else:
            minEval = float('inf')
            actionList = gameState.getLegalActions(agent)

            if agent == gameState.getNumAgents() - 1:   # decrease number of agents because pacman is one of them
                depth -= 1
                nextAgent = 0
            else:
                nextAgent = agent + 1

            for action in actionList:
                successor = gameState.generateSuccessor(agent, action)
                successorEval = self.minimax(successor, nextAgent, depth)

                if successorEval[0] < minEval:
                    minEval = successorEval[0]
                    bestAction = action

            return (minEval, bestAction)

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        action = self.minimax(gameState, self.index, self.depth)
        return action[1]

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def alphabeta(self, gameState: GameState, agent: int, depth: int, alpha: float, beta: float):

        # if game has ended or we have reached the end of the tree, return evaluation
        if (gameState.isWin() or gameState.isLose() or depth == 0):
            return (self.evaluationFunction(gameState),)

        # pacman is max player
        if agent == 0:
            maxEval = float('-inf')
            actionList = gameState.getLegalActions(agent)

            for action in actionList:
                successor = gameState.generateSuccessor(agent, action)
                successorEval = self.alphabeta(successor, agent + 1, depth, alpha, beta)

                if successorEval[0] > maxEval:
                    maxEval = successorEval[0]
                    bestAction = action

                # alpha-beta pruning
                alpha = max(alpha, successorEval[0])
                if beta < alpha:    # no <= because of autograder
                    break

            return (maxEval, bestAction)
        # ghosts are min player
        else:
            minEval = float('inf')
            actionList = gameState.getLegalActions(agent)

            if agent == gameState.getNumAgents() - 1:   # decrease number of agents because pacman is one of them
                depth -= 1
                nextAgent = 0
            else:
                nextAgent = agent + 1

            for action in actionList:
                successor = gameState.generateSuccessor(agent, action)
                successorEval = self.alphabeta(successor, nextAgent, depth, alpha, beta)

                if successorEval[0] < minEval:
                    minEval = successorEval[0]
                    bestAction = action

                # alpha-beta pruning
                beta = min(beta, successorEval[0])
                if beta < alpha:    # no <= because of autograder
                    break

            return (minEval, bestAction)

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        
        action = self.alphabeta(gameState, self.index, self.depth, float('-inf'), float('inf'))
        return action[1]

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def expectimax(self, gameState: GameState, agent: int, depth: int):

        if (gameState.isWin() or gameState.isLose() or depth == 0):
            return (self.evaluationFunction(gameState),)

        if agent == 0:
            maxEval = float('-inf')
            actionList = gameState.getLegalActions(agent)

            for action in actionList:
                successor = gameState.generateSuccessor(agent, action)
                successorEval = self.expectimax(successor, agent + 1, depth)

                if successorEval[0] > maxEval:
                    maxEval = successorEval[0]
                    bestAction = action

            return (maxEval, bestAction)
        # ghosts are now random, so we find their average evaluation
        else:
            sumEval = 0
            actionList = gameState.getLegalActions(agent)

            if agent == gameState.getNumAgents() - 1:   # decrease number of agents because pacman is one of them
                depth -= 1
                nextAgent = 0
            else:
                nextAgent = agent + 1

            for action in actionList:
                successor = gameState.generateSuccessor(agent, action)
                successorEval = self.expectimax(successor, nextAgent, depth)

                sumEval += successorEval[0]
                bestAction = action

            minEval = sumEval / len(actionList)
            return (minEval, bestAction)

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        action = self.expectimax(gameState, self.index, self.depth)
        return action[1]

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"

    pos = currentGameState.getPacmanPosition()

    # food score
    foodList = currentGameState.getFood().asList()

    if not foodList:
        return currentGameState.getScore()

    foodDistance = [manhattanDistance(pos, food) for food in foodList]

    if foodDistance:
        closestFoodScore = 1/float(min(foodDistance) + 1)
        furthestFoodScore = 1/float(max(foodDistance) + 1)
        
        if len(foodList) == 1:
            foodScore = closestFoodScore
        else:
            foodScore = closestFoodScore + furthestFoodScore

    foodScore += 1/len(foodList)

    # ghost score
    ghostScore = 0
    ghostStates = currentGameState.getGhostStates()
    ScaredTimeSum = 0
    for ghost in ghostStates:
        ghostDistance = manhattanDistance(pos, ghost.getPosition())
        ghostScaredTime = ghost.scaredTimer
        ScaredTimeSum += ghostScaredTime

        if ghostScaredTime > 0:
            ghostScore += 1/float(ghostDistance + 1)
        else:
            ghostScore -= 1/float(ghostDistance + 1)

    # capsule score
    capsuleScore = 0
    capsuleDistance = [manhattanDistance(pos, capsule) for capsule in currentGameState.getCapsules()]
    if capsuleDistance:
        capsuleScore = (1/float(min(capsuleDistance) + 1))
        capsuleScore += 1/len(capsuleDistance)

    return currentGameState.getScore() + foodScore + ghostScore + capsuleScore

# Abbreviation
better = betterEvaluationFunction
