from models.args.ArgParser import ArgParser
from models.laundry_schedule.LaundryScheduleFactory import LaundryScheduleFactory
from models.rules.IterativeRule import IterativeRule
from models.rules.MaxToMinRule import MaxToMinRule
from models.rules.RandomSearchRule import RandomSearchRule
from models.rules.MaxToMinRandomPermutationRule import MaxToMinRandomPermutationRule
from models.rules.MaxToMinWithRestrictionsRule import MaxToMinWithRestrictionsRule

from models.output.LoadsOutput import LoadsOutput




def main():
	# Dependency Inject
	argParser = ArgParser()
	laundryScheduleFactory = LaundryScheduleFactory()
	output = LoadsOutput()

	# Rules
	# rule = MaxToMinRandomPermutationRule()
	# rule = MaxToMinRule()
	rule = RandomSearchRule()

	# Schedule
	laudrySchedule = laundryScheduleFactory.getFrom(inputFile=argParser.inputValue(), rule=rule)

	# Output
	output.showOutputVerbose(loadCollection=laudrySchedule.loadCollection)
	# output.showOutput(loads=loads)


if __name__ == '__main__':
    main()