bubble_list = [2,5,2,5,7,8,93,21,8,3]
for i in range(len(bubble_list)):
    for j in range(i,len(bubble_list)):
        if bubble_list[i]>bubble_list[j]:

            bubble_list[i], bubble_list[j] = bubble_list[j], bubble_list[i]
print(bubble_list)