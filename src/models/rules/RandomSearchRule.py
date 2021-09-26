from models.rules.AbstractRule import AbstractRule
from models.laundry_schedule.Garmet import Garmet
from models.laundry_schedule.Load import Load
import random

class RandomSearchRule(AbstractRule):
    def process(self, garmets:list[Garmet]) -> list[Load]:
        
        bestLoads = (list[Load](), 100)

        for x in range(1000000):
            loads = list[Load]()
            randomShuffle = random.shuffle(garmets)
            
            for garmet in garmets:
                couldAddToLoad = False
                for load in loads:
                    if load.canAdd(garmet=garmet):
                        couldAddToLoad = True
                        load.add(garmet)
                        break
                
                if not couldAddToLoad:
                    newLoad = Load()
                    newLoad.add(garmet=garmet)
                    loads.append(newLoad)
            
            totalTime = 0 
            for load in loads:
                totalTime += load.totalTime()
            
            if totalTime < bestLoads[1]:
                bestLoads = (loads, totalTime)


        return bestLoads[0]
