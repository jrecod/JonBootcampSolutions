# Returns the indices of peaks. A peak has a lower number on both the left and the right.
def peaks(data):
    #Peak list to be returned
    list_peaks = []
    #using len of data to use indicies
    for i in range(len(data)):
        #current index
        # print(data[i])
        #post index
        # print(data[i + 1])
        #previous index
        # print(data[i - 1])

        #checks to see if it is the first element in the data
        if i == 0:           
            continue
            #checks to see if it is the last element in the data
        if i == len(data)-1:           
            continue
        # chaecking to see if previous index is less than current index and seeing if post index is less than current index
        if data[i - 1] < data[i] and data[i] > data[i + 1]:
            #if both are true add current index to list_peaks
            list_peaks.append(data[i])
    return list_peaks
        


def valleys(data):
    list_valleys = []
    for i in range(len(data)):
        if i == 0:           
            continue
            #checks to see if it is the last element in the data
        if i == len(data)-1:           
            continue
        if data[i-1] > data[i] and data[i] < data[i + 1]:
            list_valleys.append(data[i])
    return list_valleys


def peaks_and_valleys(data):
    p = peaks(data)
    v = valleys(data)
    p.extend(v)
    return p
    

# def add(a, b):
#     return a + b
# c = add(5, 2)
# c += 1
# print(c)
# print(add(5, add(3, 1)))

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks(data)
print(valleys(data))
print(peaks_and_valleys(data))
# for i in range(len(data)):
#     print(i, data[i])
