import csv

class MergeSort():
    def  __init__(self, data):
        self.data = data

    def mergeSort(data):
        if len(data) > 1:
            mid = len(data)//2
            left_subArray = data[:mid]
            right_subArray =  data[mid:]

            MergeSort(left_subArray)
            
            MergeSort(right_subArray)

            i = 0
            j = 0

            k = 0
            while i < len(left_subArray) and j <len(right_subArray):
                if left_subArray[i][9] < right_subArray[j][9]:
                    data[k]= left_subArray[i]
                    i+=1
                else:
                    data[k] = right_subArray[j]
                    j+=1
                k+=1

            while i < len(left_subArray):
                data[k] = left_subArray[i]
                i+=1
                k+=1

            while j < len(right_subArray):
                data[k] = right_subArray[j]
                j+=1
                k+=1




csv_data = []
with open('real-estate.csv', 'r') as file:
            reader = csv.reader(file)
            csv_data.extend(list(reader))

sorted=MergeSort(csv_data)
# print(sorted.data)
with open('write.csv', 'w') as file:
    # create the csv writer
    writer = csv.writer(file)

    # write a row to the csv file
    writer.writerow(sorted.data)
# print(writer)
