from models.laundry_schedule.Garmet import Garmet
from models.laundry_schedule.Load import Load

class AbstractRule():
    def process(self, garmets:list[Garmet]) -> list[Load]:
        # This method mus be overriten
        pass