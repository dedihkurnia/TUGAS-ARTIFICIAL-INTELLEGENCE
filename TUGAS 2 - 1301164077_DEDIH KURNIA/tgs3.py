import csv
import math
import collections

# Global Variable for K - Nearest Neighbour
# set K value
K = 7
save = True

# Function to read data train
# Input : -
# Output : array[1..n] of array[1..6] of float, last index is it class
def cekDataTrain():
    with open('DataTrain_Tugas3_AI.csv') as file:
        reader = csv.reader(file, delimiter=',')
        # Skip header
        next(reader)
        # Initialize array for result
        data = []
        for row in reader:
            # Remove first column (Index column)
            # Convert other column to float
            data.append(list(map(lambda x: float(x), row[1:])))
        return data


# Function to read data test
# Input -
# Output : array[1..n] of array[1..5] of float
def cekDataTest():
    with open('DataTest_Tugas3_AI.csv') as file:
        reader = csv.reader(file, delimiter=',')
        # skip header
        next(reader)
        # initialize array for result
        data = []
        for row in reader:
            # remove first column (Index column)
            # convert column 1 - 6 to float
            data.append(list(map(lambda x: float(x), row[1:6])))
        return data

# Function to measure distance between 2 data using euclidean distance algorithm
# Input : array of float, array of float
# Output : distance between 2 array of float
def jarakEuclidean(inputX, inputY):
    # Check if equal length
    euclidean = list(map(lambda x,y: (x - y)**2, inputX, inputY))
    return math.sqrt(sum(euclidean))

def simpanHasil(dataHasil):
    with open('TebakanTugas3.csv', mode='w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        i = 1
        for hasil in dataHasil:
            writer.writerow([i, hasil])
            i += 1

if __name__ == '__main__':
    # ambil data yang telah di cek
    training_data = cekDataTrain()
    test_data = cekDataTest()
    dataHasil = []
    for test in test_data:
        list_distance = []
        for train in training_data:
            # Dapatkan jarak euclidean, dan atur indeks terakhir sebagai kelas mereka
            list_distance.append([jarakEuclidean(test, train[:5]), train[5]])
        # Sort the distance Ascending
        list_distance.sort(key=(lambda x:x[0]))
        # Slice the list, get the first K data
        nearest_distance = list_distance[:K]
        # Split between distance and class into individual list
        distance, class_type = zip(*nearest_distance)
        # Count the class type
        counter = collections.Counter(class_type)
        # Get the most common count
        hasil = counter.most_common(1)[0][0]
        print (hasil)
        # Append it to results
        dataHasil.append(int(hasil))
    # Save if save equal true
    if save:
        simpanHasil(dataHasil)
