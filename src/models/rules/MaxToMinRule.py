from models.rules.AbstractRule import AbstractRule
from models.laundry_schedule.Garmet import Garmet
from models.laundry_schedule.Load import Load

class MaxToMinRule(AbstractRule):
	def process(self, garmets:list[Garmet]) -> list[Load]:
		
		loads = list[Load]()
		garmets.sort(key=lambda x: x.time, reverse=True)
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

		return loads
