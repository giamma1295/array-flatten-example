def flatten(array):

    result = []
    found_arrays = False

    for el in array:
        if type(el) is list:
            found_arrays = True
            result += el
        else:
            result.append(el)
    
    if found_arrays:
        return flatten(result)
    else:
        return result

def main():
    nested = [[1,2,[3]],4]
    flatten_result = flatten(nested)
    print(f'Starting Array is:  {nested}\nAfter flatting is: {flatten_result}')

    nested = [[1,2,[3,5,[8,1,5,[5,2,345,93,293],4,[12,94832]]],[1,43,23,94,82]],4,[34,485,[143]]]
    flatten_result = flatten(nested)
    print(f'Starting Array is:  {nested}\nAfter flatting is: {flatten_result}')


if __name__ == '__main__':
    main()



