import pandas as pd

def readData():
    file = pd.read_csv('Diabetes.csv')
    user =[]
    for i in file.index:
        col =[]
        col.append(file['Pregnancies'][i])
        col.append(file['Glucose'][i])
        col.append(file['BloodPressure'][i])
        col.append(file['SkinThickness'][i])
        col.append(file['Insulin'][i])
        col.append(file['BMI'][i])
        col.append(file['DiabetesPedigreeFunction'][i])
        col.append(file['Age'][i])
        col.append(file['Outcome'][i])
        user.append(col)
    return user
def spiltSeperlima(data):
    num = round(len(data)/5)
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    part1 = num
    part2 = (2*num)
    part3 = (3*num)
    part4 = (4*num)
    part5 = len(data)
    for i in range(part1):
        data1.append(data[i])
        data2.append(data[i + part1])
        data3.append(data[i + part2])
        data4.append(data[i + part3])
    for i in range(part5 - part4):
        data5.append(data[i + part4])
    return data1, data2, data3, data4, data5
def splitTrainTest(data):
    # Dataset 1
    training = []
    testing = []
    for i in range(614):
        training.append(data[i])
    for i in range(615, 768):
        testing.append(data[i])
    data1 = training, testing
    # Dataset 2
    training = []
    testing = []
    for i in range(461):
        training.append(data[i])
    for i in range(614, 768):
        training.append(data[i])
    for i in range(461, 614):
        testing.append(data[i])
    data2 = training, testing
    # Dataset 3
    training = []
    testing = []
    for i in range(307):
        training.append(data[i])
    for i in range(461, 768):
        training.append(data[i])
    for i in range(307, 461):
        testing.append(data[i])
    data3 = training, testing
    # Dataset 4
    training = []
    testing = []
    for i in range(154):
        training.append(data[i])
    for i in range(307, 768):
        training.append(data[i])
    for i in range(154, 307):
        testing.append(data[i])
    data4 = training, testing
    # Dataset 5
    training = []
    testing = []
    for i in range(154, 768):
        training.append(data[i])
    for i in range(154):
        testing.append(data[i])
    data5 = training, testing
    return data1, data2, data3, data4, data5
def main():
    print("Samlekom Dunya")
main()
