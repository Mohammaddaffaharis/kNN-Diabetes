import pandas as pd
from math import sqrt

#melakukan read data Diabetes.csv dan memmasukkan kedalam array user
def readData():
    file = preProcess(pd.read_csv('Diabetes.csv'))
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
#melakukan preprocessing data (mengubah data yang bernilai nol dengan mean kolom)
def preProcess(file):
    meanPregnancies = file['Pregnancies'].mean(skipna=True)
    file['Pregnancies'] = file.Pregnancies.mask(file.Pregnancies == 0, meanPregnancies)
    meanGlucose = file['Glucose'].mean(skipna=True)
    file['Glucose'] = file.Glucose.mask(file.Glucose == 0, meanGlucose)
    meanBloodPress = file['BloodPressure'].mean(skipna=True)
    file['BloodPressure'] = file.BloodPressure.mask(file.BloodPressure == 0, meanBloodPress)
    meanSkinThickness = file['SkinThickness'].mean(skipna=True)
    file['SkinThickness'] = file.SkinThickness.mask(file.SkinThickness == 0, meanSkinThickness)
    meanInsulin = file['Insulin'].mean(skipna=True)
    file['Insulin'] = file.Insulin.mask(file.Insulin == 0, meanInsulin)
    meanBMI = file['BMI'].mean(skipna=True)
    file['BMI'] = file.BMI.mask(file.BMI == 0, meanBMI)
    meanDPF = file['DiabetesPedigreeFunction'].mean(skipna=True)
    file['DiabetesPedigreeFunction'] = file.DiabetesPedigreeFunction.mask(file.DiabetesPedigreeFunction == 0, meanDPF)
    meanAge = file['Age'].mean(skipna=True)
    file['Age'] = file.Age.mask(file.Age == 0, meanAge)
    return file
#memecah data menjadi 2 bagian yaitu data training(80%) dan data testing(20%)
def splitTrainTest(data):
    # Dataset 1
    training = []
    testing = []
    for i in range(614):
        training.append(data[i])
    for i in range(614, 768):
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
#fungsi yang digunakan untuk menghitung jarak antara dua baris data
def euclidian(baris1, baris2):
    jarak = 0
    for i in range(len(baris1) - 1):
        jarak = jarak + ((baris1[i] - baris2[i]) ** 2)
    return sqrt(jarak)
#pencarian k data training terdekat dari suatu baris data test
def getNeighbors(train, testRow, neighborsNum):
    distance = []
    for i in train:
        x = euclidian(testRow,i)
        distance.append([i,x])
    distance.sort(key=lambda tup: tup[1])
    neighbors = []
    for j in range(neighborsNum):
        neighbors.append(distance[j][0])
    return neighbors
#prediksi nilai outcome baru dari sebuah data test
def getClass(neighbors):
    kelas1 = 0
    kelas0 = 0
    for i in range(len(neighbors)):
        if (neighbors[i][8] == 1):
            kelas1 = kelas1 + 1
        elif (neighbors[i][8] == 0):
            kelas0 = kelas0 + 1
    if (kelas0 > kelas1):
        return 0
    elif (kelas0 < kelas1):
        return 1
#menghitung nilai akurasi antara nilai outcome asli dan nilai outcome prediksi
def getAccuracyDataset(real, predicted):
    true = 0
    for i in range(len(real)):
        if real[i] == predicted[i]:
            true = true + 1
    return (true/float(len(real))) *100
#Main function untuk proses kNN
def getNewOutput(dataSet, k, i):
    oldOutput = []
    newOutput = []
    for j in range(len(dataSet[i][1])):
        nearestNeighbour = getNeighbors(dataSet[i][0], dataSet[i][1][j], k)
        newOutput.append(getClass(nearestNeighbour))
        oldOutput.append(dataSet[i][1][j][8])
    return oldOutput, newOutput
#Main function untuk proses Five Fold Validation
def fiveFoldValidation(dataSet,k):
    for i in range(len(dataSet)):
        score = []
        newOutput = getNewOutput(dataSet, k, i)
        accuracy = getAccuracyDataset(newOutput[0], newOutput[1])
        # print("DataSet ke-", i ," dengan K= ", k , " memiliki akurasi sebesar " , accuracy)
        score.append(accuracy)
    return score
#Ultimately Main Function
def main():
    data = readData()
    dataSet = splitTrainTest(data)
    #best K 31 = 75.97402597402598
    newk = [31]
    for k in newk:
        score = fiveFoldValidation(dataSet, k)
        avg = sum(score)/len(score)
        print("Data dengan K =",k, "memiliki Rata-Rata acuracy sebesar", avg)
main()
