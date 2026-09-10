package algorthim

import (
	"math/rand"
	"slices"
)

func Sample[T any](src []T, k int)[]T{
	if len(src)<k{
		k=len(src)
	}
	indices:=rand.Perm(len(src))
	result:=make([]T, k)
	for i:=0;i<k;i++{
		result[i]=src[indices[i]]
	}
	return result
}

func GenerateParent[T any](length int64,geneSet[]T) []T{
	var gene []T{}
	for {
		if len(gene)>length{
			break
		} else{
			sampleSize:=math.Min(length-(len(gene)),len(geneSet))
			gene=append(gene, Sample(geneSet, sampleSize))
		}
		
	}
	return gene
}

func Mutate(parent []T,geneSet []T)[]T{
	index:=rand.Intn(len(parent))
	childGenes:=slices.Clone(parent)
	newGene:=Sample(geneSet, 2)
	if newGene[1]==childGenes[index]{
		childGenes[index]=newGene[1]
	} else{
		childGenes[index]=newGene[0]
	}
	return childGenes
}


func GetBest(target []T,getFitness func(a []T,t []T) int64,targetLen int64,optimalFitness int64,geneSet[]T,display func(a []T)) []T{
	bestParent:=GenerateParent(targetLen, geneSet)
	bestFitness:=getFitness(bestParent,target)
	if bestFitness>=optimalFitness{
		return bestParent
	}
	for{
		child:=Mutate(bestParent,geneSet)
		childFitness:=getFitness(child,target)
		if bestFitness>=childFitness {
			continue
		}
		display(child)
		if childFitness>=optimalFitness {
			return child
		}
		bestFitness:=childFitness
		bestParent:=child
	}
}

func getFitness(genes[]T,target[]T) int64{
	score:=0
	for i:=0;i<len(target);i++{
		if genes[i]==target[i]{
			score+=1
		}
	}
	return int64(score)
}
