from models.laundry_schedule.Garmet import Garmet
from models.laundry_schedule.LoadCollection import LoadCollection

class AbstractRule():
	def process(self, garmets:list[Garmet]) -> LoadCollection:
		# This method mus be overriten
		pass