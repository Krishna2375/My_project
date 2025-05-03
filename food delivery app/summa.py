# n=1
# m=-1
# for i in range (5):
#     print(n,m)
#     n=n+1
#     m=m-1

# class Solution(object):
#     def isPalindrome(self,num):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         num1=str(num)
#         revese_num=num1[::-1]
#         print(revese_num)
#         if num == revese_num:
#             return True
#         else:
#             return False

# num=int(input())
# s1=Solution()
# a=s1.isPalindrome(num)
# print(a)

# a="-121"
# b="121-"
# if a==b:
#     print(1)

# class Solution(object):
#     def isPalindrome(self,x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x<0:
#             return False
#         else:
#             num1=str(x)
#             revese_num=num1[::-1]
#             #re=int(revese_num)
#             if num1==revese_num:
#                 return True
#             else:
#                 return False

# x=int(input())
# s1=Solution()
# a=s1.isPalindrome(x)
# print(a)

# a=["skfjjh","segkjjh","srfgijh","sdfgjh","sgfij","sfsdfaiuhg"]
# v=a[0][0]
# k=a[1][0]
# check=a[2]
# final=""
# common=""

# def prefix():
#     for i in range (min(len(a[0]),len(a[1]))):
#         if a[0][i]==a[1][i]:
#             v=a[0][0+1]
#             k=a[1][0+1]
#             common+=a[0][i]
#         elif v!=k:
#             break
#     if common:
#         for j in range(check,len(a)):
#             if common in check(0,len(common)):
#                 check=a[2+1]
#                 final+=a[2][j]
#     print(final)

# prefix()

# m=list(s)
#         a=["(","[","{"]
#         b=[")","]","}"]
#         for i in range (len(a)):
#             if i in m:
#                 for j in range (len(b)):
#                     if j in s:
#                         index=m.index(j)
#                         if index%2==0:
#                             return True
#         return False
