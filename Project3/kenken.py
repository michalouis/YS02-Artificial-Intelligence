import csp
import sys

def findOperation(str):
    if '+' in str:
        return '+'
    if '-' in str:
        return '-'
    if '*' in str:
        return '*'
    if '%' in str:
        return '%'

    return ''

def getPoints(str):
    returnPoints = []
    pointsStr = str.split('|')[0]
    points = pointsStr.split(',')
    for p in points:
        coord = p.split('_')
        returnPoints.append((coord[0], coord[1]))
        
    return (returnPoints, str.split('|')[2])


class Clique:
    def __init__(self, str, dimensions):
        self.operation = findOperation(str)
        self.points, self.result = getPoints(str)

    # edo afisa tin askisi
    # def constraint(self, A, a, B, b, game):
        

class KenKen(csp.CSP):

    def __init__(self, size, lines):
        
        self.variables = list()
        self.neighbors = dict()
        self.cliques = []
        self.varCliqDict = {}

        # VARIABLES
        for i in range(1, size + 1):
            for j in range(1, size + 1):
                self.variables.append((i, j))

        # DOMAINS
        domainValues = list(range(1, size + 1))
        self.domains = dict((variable, domainValues) for variable in self.variables)

        # NEIGHBORS
        for v in self.variables:
            neighborValues = []
            coordX = v[0]
            coordY = v[1]

            for i in range(size):
                if i != coordY:
                    neighborValues.append((coordX, i))
                if i != coordX:
                    neighborValues.append((i, coordY))

            self.neighbors[v] = domainValues

        # CLIQUES
        for line in lines:
            self.cliques.append(Clique(line, size))

    # edo afisa tin askisi
    # def constraint(self, A, a, B, b):
        
        
# sto terminal: python kenken.py <diastaseis pinaka, gia paradeigma 3_3>
if __name__ == '__main__':

    file_name = '../test_cases/' + sys.argv[1] + '.txt'

    with open(file_name, 'r') as file:
        size = int(file.readline())
        lines = file.readlines()[0:]
        
    file.close()

    kenken = KenKen(size, lines)
    puzzle = csp.CSP(kenken.variables, kenken.domains, kenken.neighbors, kenken.constraint)

    print("BT algorithm")
    print()
    print(csp.backtracking_search(puzzle)) 