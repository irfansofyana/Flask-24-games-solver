import solver

if __name__ == "__main__":
    x = solver.findAllSolution(solver.preProcess([3, 3, 3, 8]))
    for a in x:
        print a