# for i in range (1,5) :
#     print("*" * i)

# i = 1
# while i <= 4 :
#     print("*" * i)
#     i += 1

# --------------------------

# for i in range (1,3):
#     for k in range (1,5) :
#         print("*" * k)

# i, k = 1, 1
# while i <= 2 :
#     while k <= 4 :
#         print("*" * k)
#         k += 1
#     i += 1
#     k = 1

# -------------------------

i, k = 5, 1
while i >= 0 :
    print("{0}{1}".format(" " * i, "*" * (2 * k - 1)))
    i -= 1
    k += 1
