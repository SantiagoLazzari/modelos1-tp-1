from math import perm
from models.rules.AbstractRule import AbstractRule
from models.laundry_schedule.Garmet import Garmet
from models.laundry_schedule.LoadCollection import LoadCollection
from models.laundry_schedule.Load import Load
import random

class MaxToMinRandomPermutationRule(AbstractRule):
	def process(self, garmets:list[Garmet]) -> LoadCollection:
		bestLoadCollection = None
		garmets.sort(key=lambda x: x.time, reverse=True)

		for x in range(1000):
			x = random.randrange(len(garmets))
			y = random.randrange(len(garmets))
			oldX = garmets[x]
			oldY = garmets[y]
			garmets[x] = oldY
			garmets[y] = oldX 
			loadCollection = LoadCollection(loads=[])
			
			for garmet in garmets:
				loadCollection.addGarmetToCollectionOrAddNewLoad(garmet=garmet)

			if bestLoadCollection == None:
				bestLoadCollection = loadCollection
				continue
			
			totalTime = loadCollection.loadTime()
			bestLoadCollectionTime = bestLoadCollection.loadTime()
			print(f"total time: {totalTime}, best time: {bestLoadCollectionTime}")
			
			if totalTime < bestLoadCollectionTime:
				bestLoadCollection = loadCollection
			else:
				garmets[x] = oldX
				garmets[y] = oldY

		return bestLoadCollection
