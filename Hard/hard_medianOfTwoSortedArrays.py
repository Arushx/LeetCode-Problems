'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        #creates empty list to store numbers
        string = []

        #A for loop to transfer each list element in num1 to string
        for x in nums1:
            string.append(str(x))
        #A for loop to transfer each list element in num2 to string
        for x in nums2:
            string.append(str(x))

        #Sorts strings least to greatest 
        string = sorted(string)
        #Finds the middle index of the list
        middle = len(string)/2
        
        #Checks if the list has even numbers which means there are 2 middles
        if len(string) % 2 == 0:
            #Does not add 0 if the middle is 0\
            if string[middle-1] == "0":
                median = float(string[middle-1]) 
            else:
                median = (float(string[middle-1]) + float(string[middle])) /2 #Finds the middle between the 
        #Code runs if the list has even amt of numbers
        else:
            median = float(string[middle])
        
        median = "{:.5f}".format(median)
        median = float(median)
        return median