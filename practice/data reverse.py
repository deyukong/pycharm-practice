def data_reverse(data):
    numbytes = int(len(data)/8)
    datareverse = []

    for i in range((numbytes-1)*8, -1, -8):
        slice = data[i:i+8]
        print(slice)
        for value in slice:
            datareverse.append(value)
    print(datareverse)


data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0])
