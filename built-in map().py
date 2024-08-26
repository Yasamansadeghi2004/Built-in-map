def mymap(func, *arg):
    zipresult = zip(*arg)
    result =[]
    for item in zipresult:
        result.append(func(*item))
    return result


    
def sum (a,b):
    return a+b
    



print(list(mymap(sum,(1,2),(2,3))))
