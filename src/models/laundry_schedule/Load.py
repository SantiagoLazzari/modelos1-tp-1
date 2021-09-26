from models.laundry_schedule.Garmet import Garmet


class Load():
    garmets = list[Garmet]()

    def add(self, garmet: Garmet):
        self.garmets.append(garmet)

    def totalTime(self):
        time = 0
        for garmet in self.garmets:
            if garmet.time >= time:
                time = garmet.time

        return time
