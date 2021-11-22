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

		for x in range(10):

			x = random.randrange(len(garmets))
			y = random.randrange(len(garmets))
			oldX = garmets[x]
			oldY = garmets[y]
			garmets[x] = oldY
			garmets[y] = oldX 
			loadCollection = LoadCollection(loads=[])
			
			for garmet in garmets:
				loadCollection.addGarmetToCollectionOrAddNewLoad(garmet=garmet)
				
			totalTime = loadCollection.loadTime()
			print(totalTime)

			if totalTime < bestLoads[1]:
				bestLoads = (bestLoads[0], totalTime)
			else:
				garmets[y] = oldY
				garmets[x] = oldX 


		return bestLoads[0]
