import random


def _generate_parent(length, geneSet):
    genes = []
    while len(geneSet) < length:
        sampleSize = min(length - len(geneSet), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    return "".join(genes)


def _mutate(parent, geneSet):
    index = random.randrange(0, len(parent))
    childgenes = list(parent)
    newgene, alternative = random.sample(geneSet, 2)
    childgenes[index] = alternative if newgene == childgenes[index] else newgene
    return childgenes


def get_best(get_fitness, target_length, optimal_fitness, geneSet, display):
    random.seed()
    bestParent = _generate_parent(target_length, geneSet)
    best_fitness = get_fitness(bestParent)
    display(bestParent)
    if best_fitness >= optimal_fitness:
        return bestParent
    while True:
        childgene = _mutate(bestParent, geneSet)
        child_fitness = get_fitness(childgene)
        if child_fitness <= best_fitness:
            continue
        display(childgene)
        if child_fitness >= optimal_fitness:
            return childgene
        bestParent = childgene
        best_fitness = child_fitness
