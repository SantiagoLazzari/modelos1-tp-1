import argparse

class ArgParser():

    inputKey = 'input'

    def __init__(self):
        parser = argparse.ArgumentParser(description='Modelos TP')

        parser.add_argument('-i', f'--{self.inputKey}', metavar=self.inputKey, type=str,
                        help='Input file to read',
                        required=True)
        
        self.args = parser.parse_args()

    
    def inputValue(self):
        return self.args.input