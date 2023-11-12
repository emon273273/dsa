# # import array

# # emon = array.array('i', [1, 2, 3, 4])

# # print(emon)


# from array import *

# emon = array('i', [101, 102, 103, 104])


# import array as arr

# stu_roll = arr.array("i", [12, 3, 4, 5])

# print(stu_roll)


from array import *

emon = array('i', [101, 102, 103, 104])


# for loop dui vabe element neya jay

# method1

# with index

n = len(emon)

for i in range(n):
    print(i, emon[i])


print("without index")

for ele in emon:
    print(ele)


print("while looop er sahajje")

m=len(emon)
i=0
while (i<n):

    print(emon[i])
    i+=1