
from models.laundry_schedule.LaundrySchedule import LaundrySchedule
from models.laundry_schedule.Garmet import Garmet
from models.rules.AbstractRule import AbstractRule

class LaundryScheduleFactory():
	def getFrom(self, inputFile:str, rule: AbstractRule) -> LaundrySchedule:
		with open(inputFile) as fp:
			lines = fp.readlines()

			restrictions = {}
			times = {}
			garmets = []

			for line in lines:
				line = line.replace('\n', "")
				line = line.replace('\t', " ")
				splittedLine = line.split(' ')

				lineType = splittedLine[0]
				if 'c' in lineType:
					continue
				
				if 'p' in lineType:
					continue

				if 'e' in lineType:
					firstGarmet = splittedLine[1]
					seccondGarmet = splittedLine[2]

					if firstGarmet in restrictions:
						restrictions[firstGarmet].append(seccondGarmet)
					else: 
						restrictions[firstGarmet] = [seccondGarmet]

				if 'n' in lineType:
					
					garmet = splittedLine[1]
					time = int(splittedLine[2])
					times[garmet] = time
			
			for garmet in times:
				restricion = []
				if garmet in restrictions:
					restriction = restrictions[garmet]
				garmets.append(Garmet(id=garmet, restrictions=restriction, time=times[garmet]))

			return LaundrySchedule(garmets=garmets, rule=rule)