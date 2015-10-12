import os, sys, inspect
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe()))[0], "../../..")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

from jmoo_core import *

def readpf(problem):
    filename = "./Testing/PF/" + problem.name.split("_")[0] + "(" + str(len(problem.objectives)) + ")-PF.txt"
    return [[float(num) for num in line.split()] for line in open(filename, "r").readlines()]

from Techniques.IGD_Calculation import IGD
algorithms = [jmoo_NSGAIII_New()]
problems = [dtlz1(7, 3)]
os.chdir("../../..")  # Since the this file is nested so the working directory has to be changed

# Wrap the tests in the jmoo core framework
tests = jmoo_test(problems, algorithms)
IGD_Results = []
for problem in tests.problems:
    for algorithm in tests.algorithms:
        for repeat in xrange(repeats):
            initialPopulation(problem, MU)
            statBox = jmoo_evo(problem, algorithm, repeat)
            resulting_pf = [[f for f in individual.fitness.fitness] for individual in statBox.box[-1].population]
            IGD_Results.append(IGD(resulting_pf, readpf(problem)))
            print
            print IGD(resulting_pf, readpf(problem))
        IGD_Results = sorted(IGD_Results)
        print "Problem Name: ", problem.name
        print "Algorithm Name: ", algorithm.name
        print "- Generated New Population"
        print "- Ran the algorithm for ", repeats
        print "- The SBX crossover and mutation parameters are correct"
        print "Best: ", IGD_Results[0]
        print "Worst: ", IGD_Results[-1]
        print "Median: ", IGD_Results[int(len(IGD_Results)/2)]


