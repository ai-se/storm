from jmoo_problem import *
from jmoo_objective import *
from jmoo_decision import *
from math import pi, cos

class c2_dtlz2(jmoo_problem):
    "C2_DTLZ2"
    def __init__(prob, numDecs=10, numObjs=2):
        super(c2_dtlz2, prob).__init__()
        prob.name = "C2_DTLZ2_" + str(numDecs) + "_" + str(numObjs)
        names = ["x"+str(i+1) for i in range(numDecs)]
        lows =  [0.0 for i in range(numDecs)]
        ups =   [1.0 for i in range(numDecs)]
        prob.decisions = [jmoo_decision(names[i], lows[i], ups[i]) for i in range(numDecs)]
        prob.objectives = [jmoo_objective("f" + str(i+1), True) for i in range(numObjs)]

    def evaluate(prob,input = None):
        if input:
            for i,decision in enumerate(prob.decisions):
                decision.value = input[i]
        k = len(prob.decisions) - len(prob.objectives) + 1
        g = 0.0

        x = []
        for i in range(0, len(prob.decisions)):
            x.append(prob.decisions[i].value)

        for i in range(len(prob.decisions) - k, len(prob.decisions)):
            g += (x[i] - 0.5)*(x[i] - 0.5)
        f = []
        for i in range(0, len(prob.objectives)):
            f.append(1.0 + g)

        for i in range(0, len(prob.objectives)):
            for j in range(0, len(prob.objectives) - (i+1)):
                f[i] *= cos(x[j]*0.5*pi);
            if not (i == 0):
                aux = len(prob.objectives) - (i+1)
                f[i] *= sin(x[aux]*0.5*pi)

        for i in range(0, len(prob.objectives)):
            prob.objectives[i].value = f[i]

        return [objective.value for objective in prob.objectives]
    def evalConstraints(prob,input = None):
        return False