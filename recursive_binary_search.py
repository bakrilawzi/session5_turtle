def recursive_function(list, target):

    if len(list)==0:
        return False
    else:
        mid = (len(list))//2
        if list[mid]==target:
            return True
        else:
            if list[mid]<target:
                print(list)
                return recursive_function(list[mid + 1:], target)
            else:
                print(list)
                return recursive_function(list[:mid - 1], target)


def verify(result):
    print("the target is" , result)

verify(recursive_function([n for n in range(0, 11)], 7))