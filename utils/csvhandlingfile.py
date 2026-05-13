import csv


def csvFile(filepath):
    values = []
    with open(filepath) as csv_file:
        csvformattedData = csv.reader(csv_file)
        for i in csvformattedData:
            values.append(i)
    return values
    #print(values[0]["password"])