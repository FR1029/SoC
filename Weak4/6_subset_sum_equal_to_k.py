from os import *
from sys import *
from collections import *
from math import *

def f(ind, target, arr, dp):
    if target == 0:
        return True
        
    if ind == 0:
        return arr[0] == target
    
    if dp[ind][target] != -1:
        return dp[ind][target]
    
    notTake = f(ind - 1, target, arr, dp)
    take = False

    if arr[ind] <= target:
        take = f(ind - 1, target - arr[ind], arr, dp)
    
    dp[ind][target] = take or notTake
    return dp[ind][target]

def subsetSumToK(n, k, arr):
    dp = [[-1 for _ in range(k + 1)] for _ in range(n)]

    return f(n - 1, k, arr, dp)