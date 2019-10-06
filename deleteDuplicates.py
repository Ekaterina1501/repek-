def deleteDuplicates(str):
    new_str=[]
    [new_str.append(i) for i in str if i not in new_str]
    return new_str
print(deleteDuplicates([1,'cat',2,1,'dog','cat']))

