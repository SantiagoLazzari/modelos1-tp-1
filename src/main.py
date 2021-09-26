from models.args.ArgParser import ArgParser
from models.laundry_schedule.LaundryScheduleFactory import LaundryScheduleFactory
from models.rules.IterativeRule import IterativeRule
from models.rules.MaxToMinRule import MaxToMinRule
from models.output.LoadsOutput import LoadsOutput


def main():
    argParser = ArgParser()
    laundryScheduleFactory = LaundryScheduleFactory()
    laudrySchedule = laundryScheduleFactory.getFrom(inputFile=argParser.inputValue())
    rule = MaxToMinRule()
    loads = laudrySchedule.loadsWithRule(rule=rule)
    output = LoadsOutput()
    output.showOutput(loads=loads)

if __name__ == '__main__':
    main()