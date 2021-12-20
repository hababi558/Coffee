import numpy as np
import csv
import plotly.express as px

def getDataSource(data_path):
    coffee = []
    sleep = []
    
    with open(data_path) as csv_file:
        csvReader=csv.DictReader(csv_file)
        for row in csvReader:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return {'x':coffee,'y':sleep}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])
    print("correlation between coffee in ml vs sleep in hours",correlation[0,1])

def setup():
    data_path = 'Coffee.csv'
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()  