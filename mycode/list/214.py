import pandas as pd 
import numpy as np 
print("print test")



#%%
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        alpha_dict = dict()
        for alpha in s:
            if alpha_dict.get(ord(alpha)):
                alpha_dict[ord(alpha)] +=1
            else:
                alpha_dict[ord(alpha)] = 1
        for alpha in t:
            if alpha_dict.get(ord(alpha)):
                alpha_dict[ord(alpha)] -=1
                if alpha_dict[ord(alpha)]<0:
                    return False
            else:
                return False
        return True
                


# %%
def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False
