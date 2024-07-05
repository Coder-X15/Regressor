import sys
import csv
import statistics
import math
# a command line tool to generate a regression line for the data in a given .csv file using Ordinary Least Squares (OLS) method

'''class FileError(Exception):
    def __init__(self, stmt):
        self.stmt = stmt'''
    
class RegressionLineGenerator:
    
    def __init__(self, filepath):
        ''' Constructor. The data processing also takes place here '''
        self.file = csv.reader(open(filepath, 'r', newline="")) # getting the iterator for the file
        self.x = []
        self.y = []
        self.m = self.c = 0

        # by default we're gonna take float to use with the process
        self.headers = next(self.file)
        try:
            while True:
                row = next(self.file)
                self.x += [float(row[0])]
                self.y += [float(row[1])]
        except:
            pass
        
    def build_line(self):
        ''' Finding the (optimal) coefficients m and c of the line y = mx + c '''
        x_mean = statistics.mean(self.x)
        y_mean = statistics.mean(self.y)

        num = math.fsum([(self.x[i]- x_mean)*(self.y[i]-y_mean) for i in range(len(self.x))])
        denom = math.fsum([(self.x[i]- x_mean)**2 for i in range(len(self.x))])

        self.m = num/denom
        self.c = y_mean - x_mean*self.m

    def analyse(self):
        ''' Prints the MSE and R^2 score of the line'''
        def predict(x : list):
            y = [self.m * i + self.c for i in x]
            return y
        y_pred = predict(self.x)

        SSR = math.fsum([(self.y[i]- y_pred[i])**2 for i in range(len(self.y))]) # sum of squared residues
        SST = math.fsum([(self.y[i]- statistics.mean(self.y))**2 for i in range(len(self.y))]) # sum of squared 
        R2 = 1 - (SSR/SST)
        MSE = (1/2*len(self.x))*SSR
        print("====ANALYSIS====")
        print(f"1. Coefficients (y=mx+c):m={self.m}, c={self.c}")
        print(f"2. MSE:{MSE}")
        print(f"3. R2:{R2}")

file = sys.argv[1]
line = RegressionLineGenerator(file)
line.build_line()
line.analyse()
