# rows=5
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i==rows or j==1 or j==rows:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)

# * * * * *
# *
# * * * * *
#         *
# * * * * *       

rows=6
mid=rows//2+1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or i==mid:
            res+="*"+" "
        elif j==1 and i<mid or j==rows and i>mid:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)


# * * * * *
# *       *
# * * * * *
# *     *
# *       *

# rows=5
# mid=rows//2+1
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i==1 or i==mid or j==1 :
           
#            res+="R"+" "
#         elif j==rows and i<mid or i==j and i>mid-1:
#             res+="R" +" "
#         else:
#             res+=" "+" "
#     print(res)

# # * * * * *
# # * 
# # * * * * * 
# # *
# # * * * * *


# rows=5
# mid=rows//2+1
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i==1 or i==rows or i==mid or j==1:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)


# # * * * * *
# # * 
# # * * * * * 
# # *
# # * * * * *

# rows=5
# mid=rows//2+1
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i==1 or i==rows or i==mid or j==1:
#             res+="$"+" "
#         else:
#             res+=" "+" "
#     print(res)



