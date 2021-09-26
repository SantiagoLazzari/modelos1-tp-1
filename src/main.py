from models.args.ArgParser import ArgParser
from models.laundry_schedule.LaundryScheduleFactory import LaundryScheduleFactory


def main():
    argParser = ArgParser()
    laundryScheduleFactory = LaundryScheduleFactory()
    laudrySchedule = laundryScheduleFactory.getFrom(inputFile=argParser.inputValue())
    
    

    

if __name__ == '__main__':
    main()