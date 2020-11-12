import mai
import view

#a = [[1, 2, 1/3, 1/5, 1/7], [1/2, 1, 1/6, 1/9, 1/9], [3, 6, 1, 1/2, 1/2], [5, 9, 2, 1, 1/2], [7, 9, 2, 2, 1]]
a = [
    [1, 4, 3, 1, 3, 4], 
    [1/4, 1, 7, 3, 1/5, 1], 
    [1/3, 1/7, 1, 1/5, 1/5, 1/6], 
    [1, 1/3, 5, 1, 1, 1/3], 
    [1/3, 5, 5, 1, 1, 3], 
    [1/4, 1, 6, 3, 1/3, 1]
    ]
sz = len(a)
for i in range(sz):
    print(a[i])

weights = mai.MAI(a)
print('weights ')
print(weights)
view.show('test.csv', weights)