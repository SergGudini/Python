# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.


#lst = [1, 1, 2, 2, 3, 3]
#lst = [1, 2, 3, 4, 5]
#lst = [1, 2, 3, 2, 4, 5, 4]
#lst = [1, 1, 1, 1, 1]
lst = [1, 2, 3, 4, 5, 6, 7]

dublicates = []

for i in lst:
    index = lst.index(i)
    for j in lst[index+1::]:
        if i == j and i not in dublicates:
            dublicates.append(j)

print(dublicates)