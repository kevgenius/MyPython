A = [1, 2, 3]
B = []
for x in A:
    if x not in B:
        B.append(x)
    if len(B) == len(A):
        print(B)
print('-'*100)


x = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'b1', 'b2', 'b3', 'b4', 'b5']
A = []
B = []
toA = []
toB = []

for i in x:
    if i.startswith('a') and len(toA) < 2:
        toA.append(i)
    elif i.startswith('a') and len(toA) == 2:
        A.append(toA)
        toA = []
        toA.append(i)
if len(toA) != 0:
    A.append(toA)
print(A)
    #
    # elif i.startswith('b') and len(toB) < 2:
    #     toB.append(i)
    # elif i.startswith('b') and len(toB) == 2:
    #     toB.append(i)
    #     toB = []
    #

#     elif i.startswith('b'):
#         B.append(i)
# print(A)
# print(B)

print("-"*100)


for i in range(3.3):
    print(i)


