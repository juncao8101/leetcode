class Solution(object):
    def LCS(self,str1,str2):
        if not str1 or not str2:return 0
        dp=[[0 for _ in range(len(str1))] for _ in range(len(str2))]
        res=0
        
        for j in range(len(str1)):
            if str1[j]==str2[0]:
                dp[0][j]=1

        for i in range(len(str2)):
            if str2[i]==str1[0]:
                dp[i][0]=1

        for i in range(1,len(str2)):
            for j in range(1,len(str1)):
                if str1[j]==str2[i]:
                    dp[i][j]=dp[i-1][j-1]+1
                    res=max(res,dp[i][j])
        return res
print(Solution().LCS('12345','345678'))
# 3


        
