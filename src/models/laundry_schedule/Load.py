from models.laundry_schedule.Garmet import Garmet


class Load():
    
    def __init__(self):
        self.garmets = list[Garmet]()

    def add(self, garmet: Garmet):
        self.garmets.append(garmet)

    def totalTime(self):
        time = 0
        for garmet in self.garmets:
            if garmet.time >= time:
                time = garmet.time

        return time

    def isCorrect(self) -> bool:
        loadGarmetIds = list(map(lambda x : x.id, self.garmets))
        loadGarmetIncompatibleIds = []

        for garmet in self.garmets:
            loadGarmetIncompatibleIds += garmet.restricitons

        for loadGarmetId in loadGarmetIds:
            if loadGarmetId in loadGarmetIncompatibleIds:
                return False

        return True
