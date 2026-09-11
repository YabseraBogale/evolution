import genetic
import datetime


def test_Hello_world():
    target = "Hello World!"
    guess_password(target)


def guess_password(target):
    geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime = datetime.datetime.now()

    def fnGetFitness(gene_set):
        return get_fitness(gene_set, target)

    def fnDisplay(gene_set):
        display(gene_set, target, startTime)

    optimal_fitness = len(target)
    genetic.get_best(fnGetFitness, len(target), optimal_fitness, geneSet, fnDisplay)


def display(gene_set, target, startTime):
    timediff = datetime.datetime.now() - startTime
    fitness = get_fitness(gene_set, target)
    print("{}\t{}\t{}".format(gene_set, fitness, timediff))


def get_fitness(gene_set, target):
    return sum(1 for expected, actual in zip(target, gene_set) if expected == actual)


if __name__ == "__main__":
    test_Hello_world()
