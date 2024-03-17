import numpy as np
import time

###################
#
# NumPy Library
#
####################



ary = np.array([1,2,4,45,2,55,22,9,7])
reshp = ary.reshape(3,3)
slic = ary[2:4]

ary2 = np.array([1,23,44,3,22])
TruthyValues = np.array([True,False,True,False,True])
filterArray = ary2[TruthyValues]

ary2.sort()
sort = ary2

search = np.where(ary2 == 44)
while True:
    print('play with array -- \n')
    
    print('[0] - Quit')
    print('[1] - Reshape array {array.reshape}')
    print('[2] - Slice {array[index:index]}')
    print('[3] - Filter {array[Trur,False]}')
    print('[4] - Sort {array.sore}')
    print('[5] - Search {np.wehere(array==Value)}}')
    

    
    choice = int(input('> '))
    if choice == 0:
        break
    
    elif choice == 1:
        print('array: ',ary)
        print('reShaped array [3,3]]\n',reshp)
    elif choice == 2:
        print('array: ',ary)
        print('slice[2:4]\n',slic)
    elif choice == 3:
        print('array: ',ary2)
        print(f'TruthyValuse{TruthyValues}\nFilter array: ',filterArray)
    elif  choice == 4:
        print('array: ',ary2)
        print('sorter array: ',sort)
    else:
        print('arrays: ',ary2)
        print('search: np.where(array==44)',search)
    time.sleep(3)
    

