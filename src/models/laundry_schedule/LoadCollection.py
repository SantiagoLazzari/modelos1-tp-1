from models.laundry_schedule.Load import Load
from models.laundry_schedule.Garmet import Garmet

class LoadCollection():
	def __init__(self, loads: list[Load]):
		self.loads = loads
		self.garmets = []


	def loadTime(self):
		totalTime = 0 
		for load in self.loads:
			totalTime += load.totalTime()
		return totalTime

	def canAddGarmetToCollection(self, garmet: Garmet):
		for load in self.loads:
			if load.canAdd(garmet=garmet):
				return True
		return False

	def addGarmetToCollectionOrAddNewLoad(self, garmet: Garmet):
		couldAddToLoad = False
		for load in self.loads:
			if load.canAdd(garmet=garmet):
				couldAddToLoad = True
				load.add(garmet)
				break
		
		if not couldAddToLoad:
			newLoad = Load()
			newLoad.add(garmet=garmet)
			self.loads.append(newLoad)
		
		self.garmets.append(garmet)
