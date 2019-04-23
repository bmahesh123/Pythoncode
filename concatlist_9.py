def list_concat(list):
    output= ''
    for data in list:
        output = output + str(data)
        print(str(data))
    return output

print(list_concat([2, 4, 6, 8, 10]))