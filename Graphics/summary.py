def get_data_from_archive(problems, algorithms, Configurations, function):
    from PerformanceMeasures.DataFrame import ProblemFrame
    problem_dict = {}
    for problem in problems:
        data = ProblemFrame(problem, algorithms)
        reference_point = data.get_reference_point(Configurations["Universal"]["No_of_Generations"])
        generation_dict = {}
        for generation in xrange(Configurations["Universal"]["No_of_Generations"]):
            population = data.get_frontier_values(generation)
            evaluations = data.get_evaluation_values(generation)
            algorithm_dict = {}
            for algorithm in algorithms:
                repeat_dict = {}
                for repeat in xrange(Configurations["Universal"]["Repeats"]):
                    candidates = [pop.objectives for pop in population[algorithm.name][repeat]]
                    repeat_dict[str(repeat)] = {}
                    if len(candidates) > 0:
                        repeat_dict[str(repeat)]["HyperVolume"] = function(reference_point, candidates)
                        repeat_dict[str(repeat)]["Evaluations"] = evaluations[algorithm.name][repeat]
                    else:
                        repeat_dict[str(repeat)]["HyperVolume"] = None
                        repeat_dict[str(repeat)]["Evaluations"] = None

                algorithm_dict[algorithm.name] = repeat_dict
            generation_dict[str(generation)] = algorithm_dict
        problem_dict[problem.name] = generation_dict
    return problem_dict


def generate_summary(problems, algorithms, list_hypervolume_scores, list_spread_scores,base_line, baseline, Configurations, tag="Comparisions"):
    for measure_name, list_xx_scores in zip(["HyperVolume", "Spread"], [list_hypervolume_scores, list_spread_scores]):
        # concatenating the dictionaries
        x_scores = list_xx_scores[0]
        for x_score in list_xx_scores: x_scores.update(x_score)
        x_dpoints = []
        import pdb
        pdb.set_trace()
        for problem in problems:
            from PerformanceMeasures.DataFrame import ProblemFrame
            data = ProblemFrame(problem, algorithms)
            population = data.get_frontier_values(Configurations["Universal"]["No_of_Generations"])
            for objective_number in xrange(len(problem.objectives)):
                for algorithm in algorithms:
                    for repeat in xrange(Configurations["Universal"]["Repeats"]):
                        candidates = [pop.objectives for pop in population[algorithm.name][repeat]]
