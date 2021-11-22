from models.laundry_schedule.Load import Load
from models.laundry_schedule.LoadCollection import LoadCollection

class LoadsOutput():
	def showOutputVerbose(self, loadCollection:LoadCollection):
		loadCount = 1
		totalTime = 0
		for load in loadCollection.loads:
			print(f"Load {loadCount} has garmets {list(map(lambda x : x.id, load.garmets))} and its total time is {load.totalTime()}")
			loadCount += 1
			totalTime += load.totalTime()
			print(f"Load is correct {load.isLoadCompatible()}")

		print(f"total time is {totalTime}")

	def showOutput(self, loadCollection:LoadCollection):
		loadCount = 1
		for load in loadCollection.loads:
			for garmet in load.garmets:
				print(f"{garmet.id} {loadCount}")
			loadCount += 1
