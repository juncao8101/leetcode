## 1.两数之和

哈希表法，每一个数对应一个位置，建一个哈希表，这样就不需要遍历查找了，节省时间。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,value in enumerate(nums):
            sub=target-value
            j=hashmap.get(sub) 
            if j is not None and j!=i:
                return [i,j]
            hashmap[value]=i

```



## 3.无重复字符的最长子串



```python
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#双指针法，外层循环是右指针，里面是左指针
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        lookup=collections.deque()
        for right in range(len(s)):
            while s[right] in lookup:
                lookup.popleft()
            lookup.append(s[right])
            if len(lookup)>ans:ans=len(lookup)
        return ans

```



## 5.最长回文子串

中心扩展算法：

回文子串，也就是对称的子串。设置一个end-start用来保存目前已知的最大值，以及位置信息。

一个长度为n的字符串有2n-1个中心，为什么不是n呢，因为像abba这种，对称点在b和b之间，这一类也要算进去。

extend函数的参数是两个参数，表示一个中心，两个参数相同则表示以数字为中心，如果两个参数是i和i+1说明以间隔为中心。它的返回值为子串长度。

我们对每个中心调用extend函数，cur_len保存两次的最大值，end-start用来保存最大子串长度以及位置信息。

遍历完成之后，取出s[start:end+1] 即可。

```python
class Solution():
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        start = 0
        end = 0
        for i in range(n):
            odd_len = self.extend(s,n,i,i)    #odd_len表示这个子串长度一定是奇数
            even_len = self.extend(s,n,i,i+1)    #子串长度为偶数
            cur_len = max(odd_len,even_len)
            if(cur_len > end-start):
                start = int(i-(cur_len-1)//2)
                end = int(i+(cur_len)//2)
        return s[start:end+1]
    def extend(self,s,n,left,right):
        while((left>=0) and (right<=n-1) and (s[left]==s[right])):
            left-=1
            right+=1
        return right-left-1

```

## 11.盛最多水的容器

刚开始可能会疑惑两边一直往中间靠会不会错过最大值呢，其实不会，因为一开始就把指针指向了数组的最左边和最右边，这个时候宽是最大的，往中间靠的过程中一定会取到最大的矩形面积。

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right,area=0,len(height)-1,0
        while(left<right):
            if(height[left]<height[right]):
                area=max(area,height[left]*(right-left))
                left+=1
            else:
                area=max(area,height[right]*(right-left))
                right-=1
        return area

```

## 13.罗马数字转整数

```python
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}        
        ans=0        
        for i in range(len(s)):            
            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:                
                ans-=a[s[i]]
            else:
                ans+=a[s[i]]
        return ans

```

或者：

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        sums=0
        i=0
        while(i<=len(s)-2):
            if(s[i]+s[i+1] in d.keys()):
                sums+=d[s[i]+s[i+1]]
                i+=2
                continue
            sums+=d[s[i]]
            i+=1
        if(i==len(s)-1):
            sums+=d[s[i]]
        return sums

```

## 14.最长公共子串

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ''
        s1=min(strs)
        s2=max(strs)
        for i,x in enumerate(s1):
            if(x!=s2[i]):
                return s1[:i]
        return s1

```



## 19.删除链表倒数第n个节点

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first=ListNode(0)
        second=ListNode(0)
        first.next=head
        second.next=head
        flag=first
        for i in range(n+1):       #因为要使用两个指针，先将两个指针隔开一定的距离，最后第二个指针找到末尾的时候直接可以删除前面的。
            second=second.next
        while(second!=None):
            first=first.next
            second=second.next
        first.next=first.next.next
        return  flag.next

```

## 20. 有效的括号

```python
class Solution:
    def isValid(self, s: str) -> bool:
        if(not s):return True
        stack=[]
        hashmap={')':'(','}':'{',']':'['}
        for p in s:
            if p in hashmap:
                q=stack.pop() if stack else ‘#’   
                if(hashmap[p]!=q):
                    return False
            else:
                stack.append(p)
        if not stack:return True
#			q=stack.pop() if stack else ‘#’  因为这句话，表示q可能是因为栈空了赋给的哑值，所以后面应该哈希p而不是q，否则会出错。
```

## 21.合并两个有序链表

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new=ListNode(None)
        head=new
        while(l1 and l2):
            if(l1.val<=l2.val):
                new.next=l1
                l1=l1.next
            else:
                new.next=l2
                l2=l2.next
            new=new.next
        if l1:
            new.next=l1
        else:
            new.next=l2
        return head.next

```



## 24.两两交换链表节点

```python
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例:
# 
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre=ListNode(None)
        pre.next = head
        move=pre
        while(move.next and move.next.next):
            start=move.next
            end=move.next.next
            start.next=end.next
            end.next=start
            move.next=end
            move=start
        return pre.next
```

## 26.删除排序数组中的重复项

双指针法，i是前面的慢指针，j是后面的快指针。i固定，j往后跑，如果发现相同，j继续跑直到两个值不同，i往后+1。

把j位置的值给i的位置。最后，i前面的就都是无重复的项了。

这一题不能新建数组，必须在原位修改，而且答案检查之后检查前面数组长度个值，也就暗示了可以用后面的值把前面的覆盖掉。

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(1,len(nums)):
            if(nums[i]!=nums[j]):
                i+=1
                nums[i]=nums[j]
        return i+1

```

## 27.移除元素

采用倒序

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=len(nums)
        for i in range(j-1,-1,-1):
            if nums[i]==val:
                nums.pop(i)    
        return len(nums)

```



## 22.括号生成

```python
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
# 
# 例如，给出 n = 3，生成结果为：
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
# 
#回溯法
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        def backward(s='',left=0,right=0):
            if len(s)==2*n:
                ans.append(s)
                return 
            if left<n:
                backward(s+'(',left+1,right)
            if right<left:
                backward(s+')',left,right+1)
        backward()
        return ans
```

<img src="https://img-blog.csdn.net/20171113152842441" alt="img" style="zoom:40%;" />

## 31.下一个排列

```python
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 
# 必须原地修改，只允许使用额外常数空间。
# 
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=j=len(nums)-1
        while i>=1 and nums[i-1]>=nums[i] :
            i-=1
        if i==0:
            return nums.reverse()
        #定位到最后递减的位置
        while j>=0 and nums[j]<=nums[i-1]:
            j-=1
        nums[j],nums[i-1]=nums[i-1],nums[j]
        left=i
        right=len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
```

## 33.搜索旋转排序数组

```python
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 
# 你可以假设数组中不存在重复的元素。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 示例 1:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 
# 
# 示例 2:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
# 
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low+(high-low)/2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[low]:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
```

## 34.在排序数组中查找元素的第一个和最后一个位置

```python
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 如果数组中不存在目标值，返回 [-1, -1]。
# 
# 示例 1:
# 
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 
# 示例 2:
# 
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
# 
#
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def left_search(nums, target):
            left=0
            right=len(nums)-1
            while left <= right:
                mid=(left+right)/2
                if nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return left
        def right_search(nums,target):
            left=0
            right=len(nums)-1
            while left <= right :
                mid = (left+right)/2
                if nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return right
        l,r=left_search(nums, target),right_search(nums,target)
        return [l,r] if l<=r else [-1,-1]
```

## 35.搜索插入位置

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        n=len(nums)
        while(i<n):
            if(nums[i]>=target):
                return i
            i+=1
        return n
#查找和插入在一起实现，因为是有序数组
```



## 39.组合总数

```python
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的数字可以无限制重复被选取。
# 
# 说明：
# 
# 
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
#
class Solution(object):
    def combinationSum(self, candidates, target):
        
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        def backtrack(nums, target,index,path):
            if target<0:return 
            if target==0:
                res.append(path)
                return 
            for i in xrange(index,len(nums)):
                if nums[i]>target:break
                backtrack(nums,target-nums[i],i,path+[nums[i]])
        candidates.sort()
        backtrack(candidates,target,0,[])
        return res

```

## 40.组合总数II

```python
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
# 
# 说明：
# 
# 
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
# 
#
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        candidates.sort()
        self.backtracking(candidates,0,target,[],res)
        return res
    def backtracking(self,nums,start,target,path,res):
        if target == 0:
            res.append(path)
            return
        for i in xrange(start,len(nums)):
            if i>start and nums[i] == nums[i-1]:
                continue	#由于是排序过的，如果前后相等就跳过，避免重复选取
            if nums[i]>target:
                break		#后面的数字都会比target大
            self.backtracking(nums,i+1,target-nums[i],[nums[i]]+path,res)
    	
```



## 46.全排列

```python
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def backtrack(nums,path):
            if not nums:
                res.append(path)
            for i in xrange(len(nums)):
                backtrack(nums[:i]+nums[i+1:],path+[nums[i]])
        res=[]
        backtrack(nums,[])
        return res
```

## 47.全排列II

```python
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 
# 示例:
# 
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
#
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(nums,path):
            if not nums:
                res.append(path)
                return
            for i in xrange(len(nums)):
                if i>=1 and nums[i]==nums[i-1]:
                    continue
                backtrack(nums[:i]+nums[i+1:],path+[nums[i]])
        res=[]
        nums.sort()
        backtrack(nums,[])
        return res
```

## 48.旋转图像

```python
# 给定一个 n × n 的二维矩阵表示一个图像。
# 
# 将图像顺时针旋转 90 度。
# 
# 说明：
# 
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
# 
# 示例 1:
# 
# 给定 matrix = 
# [
# ⁠ [1,2,3],
# ⁠ [4,5,6],
# ⁠ [7,8,9]
# ],
# 
# 原地旋转输入矩阵，使其变为:
# [
# ⁠ [7,4,1],
# ⁠ [8,5,2],
# ⁠ [9,6,3]
# ]
# 
# 
# 示例 2:
# 
# 给定 matrix =
# [
# ⁠ [ 5, 1, 9,11],
# ⁠ [ 2, 4, 8,10],
# ⁠ [13, 3, 6, 7],
# ⁠ [15,14,12,16]
# ], 
# 
# 原地旋转输入矩阵，使其变为:
# [
# ⁠ [15,13, 2, 5],
# ⁠ [14, 3, 4, 1],
# ⁠ [12, 6, 8, 9],
# ⁠ [16, 7,10,11]
# ]
# 
# 
#1
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                #先沿着左上到右下的对角线作对称变换
        for i in range(n):
            for j in range(n/2):
                matrix[i][j],matrix[i][~j]=matrix[i][~j],matrix[i][j]
                #然后以水平中心线作对称变换
                
#2.也可以先以水平中心线作对称变换，然后沿着左上到右下的对角线作对称变换，以下：
class Solution:
    def rotate(self, A):
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
#3.最简洁的，用python的zip函数：
'''
zip的用法示例
>>> A=[[1,2,3],[4,5,6],[7,8,9]]
>>> zip(A)
<zip object at 0x1034320c8>
>>> list(zip(A))
[([1, 2, 3],), ([4, 5, 6],), ([7, 8, 9],)]
>>> list(zip(*A))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
>>> b=list(zip(*A))
>>> list(zip(*b))
[(1, 2, 3), (4, 5, 6), (7, 8, 9)]
>>> list(zip(A[0],A[1],A[2]))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
>>> list(zip(*A[::-1]))
[(7, 4, 1), (8, 5, 2), (9, 6, 3)]
'''
#所以可以这么写：
class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])
```

## 53.最大子序和

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        numsum=0
        for i in range(0,len(nums)):
            if(numsum>0):
                numsum+=nums[i]
            else:
                numsum=nums[i]
            res=max(res,numsum)
        return res

```

## 58.最后一个单词的长度

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt,tail=0,len(s)-1
        while(tail>=0 and s[tail]==' '):
            tail-=1
        while(tail >=0 and s[tail]!=' '):
            tail-=1
            cnt+=1
        return cnt

```

## 62.不同路径

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        up=1
        down=1
        a=m+n-2
        for i in range(m-1):
            up*=a
            a-=1
        for i in range(1,m):
            down*=i
        return up/down

```



## 66.加一

利用eval函数和map函数，比较简洁

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for c in digits:
            s+=str(c)
        tmp=eval(s)+1
        res=list(map(int,str(tmp)))
        return res

```

## 69.x的平方根

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<1:
            return 0
        g=x
        while(g*g-x>0.01):
            g=(g+x/g)/2
        return int(g)

```

## 70.爬楼梯

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if(n==1):return 1
        dp=[None]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

```

## 83.删除排序链表中的重复元素

双指针法

```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(head==None):return None
        slow=head
        fast=head.next
        while(fast!=None):
            if(slow.val!=fast.val):
                slow=slow.next
                slow.val=fast.val
            fast=fast.next
        slow.next=None
        return head

```

or

```
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(head==None):return None
        slow=head
        fast=head.next
        while(fast!=None):
            if(slow.val!=fast.val):
                slow=slow.next
                slow.val=fast.val
            fast=fast.next
        slow.next=None
        return head

```

## 88.合并两个有序数组

要求是对nums1原地修改，用双指针法，为了使空间复杂度为O（1），让指针从末尾向前移动。

如果pm此时如果已经为-1了，无法继续移动，所以要记得最后要把第二个数组没移动完的全部移过来。

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pm=m-1
        pn=n-1
        tail=m+n-1
        while(pm>=0 and pn>=0):
            if(nums2[pn]>nums1[pm]):
                nums1[tail]=nums2[pn]
                pn-=1
            else:
                nums1[tail]=nums1[pm]
                pm-=1
            tail-=1
        nums1[:pn+1]=nums2[:pn+1]

```



## 94.二叉树的中序遍历

```python
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def inorderTraversal(self, root: TreeNode) -> List[int]:
    t=root
    stack=[]
    result=[]
    while(t or stack):
        while(t):
            stack.append(t)     #一路向左并将沿途节点压入堆栈
            t=t.left
        t=stack.pop()
        result.append(t.val)     #访问节点
        t=t.right         #转向右子树
    return result
#while(t)这个语句有两个功能，一是第一遍遍历root的时候，一路把左子树节点放入栈，二是每次从栈中pop出来节点的时候，都会考察这个节点的右子树，把右子树的左节点也要一路放到栈中。
```

## 96.不同的二叉搜索树

```python
#结题思路：假设n个节点存在二叉排序树的个数是G(n)，1为根节点，2为根节点，...，n为根节点，当1为根节点时，其左子树节点个数为0，右子树节点个数为n-1，同理当2为根节点时，其左子树节点个数为1，右子树节点为n-2，所以可得G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
#
#dp[0]=1
#
#dp[1]=1
#
#dp[2]=dp[0]*dp[1]+dp[1]*dp[0] 
#
#dp[3]=dp[0]*dp[2]+dp[1]*dp[1]+dp[2]*dp[0]
#
#写出前两个公式，找规律，发现dp[i]中的i决定多项式的项数，而且每一项之和等于i-1，所以内层循环循环range(i)遍，每次加上dp[i]*dp[i-1-j]。
class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-j-1]
        return dp[n]

```

## 98.验证二叉搜索树

```python
#二叉搜索树的特点是，中序遍历一定为升序。
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack,temp=[],float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            if root.val<=temp:
                return False
            temp=root.val
            root=root.right
        return True

```

```python
#递归法
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node,lower = float('-inf'),upper = float('inf')):
            if not node:
                return True
            val=node.val
            if val<=lower or val>=upper:
                return False
            if not helper(node.right,val,upper):
                return False
            if not helper(node.left,lower,val):
                return False
            
            return True
        return helper(root)

```



## 100.相同的树

树结构相同，也就是每一个节点要相同，相对的节点，要么都为None，要么值相等，值相等的话还要继续递归比较子树。其他情况返回False。

1.递归

```python
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if(p==None and q==None):
            return True
        if(p!=None and q!=None and p.val==q.val):
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False

```

2.迭代

```python
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack=[]
        stack.append((p,q))
        while(stack):
            (a,b)=stack.pop()
            if(a==None and b==None):
                continue
            elif(a!=None and b!=None and a.val==b.val):
                stack.append((a.left,b.left))
                stack.append((a.right,b.right))
            else:
                return False
        return True 

```

## 101.对称的树

要使树对称，保证每一个节点的两个子节点对称即可，递归写法，对称，要么都为None，要么都相等，如果值相同，递归比较子树是否对称，其他的情况均为return False

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(root1,root2):
            if(root1==None and root2==None):
                return True
            elif(root1!=None and root2!=None and root1.val==root2.val):
                return check(root1.left,root2.right) and check(root2.left,root1.right)
            else:
                return False
        return check(root,root)

```

## 102.二叉树的层序遍历

1.递归

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(root1,root2):
            if(root1==None and root2==None):
                return True
            elif(root1!=None and root2!=None and root1.val==root2.val):
                return check(root1.left,root2.right) and check(root2.left,root1.right)
            else:
                return False
        return check(root,root)

```

2.迭代:利用迭代，每次将上一层进栈的元素全部都被pop出去加入列表之后进行下一轮

这里的temp_list和sub_list每一轮都会更新，保证了每一层之间相互独立

```python
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if(root==None):
            return None
        stack,res=[root],[]
        while(stack):
            temp_stack=[]
            sub_list=[]
            for node in stack:
                sub_list.append(node.val)
                if(node.left):
                    temp_stack.append(node.left)
                if(node.right):
                    temp_stack.append(node.right)
            stack=temp_stack
            res.insert(0,sub_list)        #这个是从底层倒着输出的 对应107题，对于这道题目,应改成res.append(sub_list)
        return res

```

## 104.求二叉树最大深度

1.递归:

如何计数呢，递归的层数就是一个计数器，每次取出子树中的最深的，然后加一，返回到上一层，最后得到最大深度。

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(root==None):
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

```

2.深度优先搜索:

节点的处理方式是设置一个元组，存储此时节点高度值。先根节点入栈。

如果栈里面还有元素，pop一个，检查是否为None，如果不是，更新depth的值。

然后左右子树入栈。

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(root==None):
            return 0
        stack,depth=[],0
        stack.append((1,root))
        while stack:
            cur,node=stack.pop(）
            if node:
                depth=max(depth,cur)        #这一句要放在if里面，因为None可能也被当做有效节点入栈了，要过滤掉再更新深度
                                            #或者我们可以在这里检查一下左子树和右子树是否为None
                stack.append((cur+1,node.left))
                stack.append((cur+1,node.right))
        return depth

```

## 105.从前序遍历与中序遍历构造二叉树

```python
class Solution(object):
    def buildTree(self, preorder, inorder):
        if(not inorder):
            return None
        x=preorder.pop(0)
        root=TreeNode(x)
        mid=inorder.index(x)
        root.left=self.buildTree(preorder[:mid],inorder[:mid])
        root.right=self.buildTree(preorder[mid:],inorder[mid+1:])
        #为啥preorder的mid不用+1呢，因为preorder的第一个数已经弹出来了，而inorder的中间节点还在里面，所以要把那个跳过，要+1
        return root

```

## 106.从中序和后序遍历序列构造二叉树

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if(len(inorder)==0):return None
        x=postorder.pop()        #唯一不同之处
        mid=inorder.index(x)
        root=TreeNode(x)
        root.left=self.buildTree(inorder[:mid],postorder[:mid])
        root.right=self.buildTree(inorder[mid+1:],postorder[mid:])
        return root

```



## 108.将有序数组转换为平衡的二叉搜索树

思路是取数组中点作为节点，可以保证平衡，它的左子节点就是左边的中点，右子节点就是右边的中点，以此类推，写成递归。

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildTree(nums,l,r):
            if(l>r):
                return None    #表示叶子节点左右都赋值为None
            m=int(l+(r-l)/2)
            root=TreeNode(nums[m])
            root.left=buildTree(nums,l,m-1)
            root.right=buildTree(nums,m+1,r)
            return root    #返回root赋给上层节点的left和right
        if not nums:
            return None
        else:
            return buildTree(nums,0,len(nums)-1)

```

## 110.平衡二叉树递归版

```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res=True
        def judge(root):
            if(not root):return 0
            left=judge(root.left)+1
            right=judge(root.right)+1
            if(abs(left-right)>1):
                self.res=False
            return max(left,right)
        judge(root)
        return self.res
#换一种写法：
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if(not root):return 0
            left=depth(root.left)
            if(left==-1):return -1
            right=depth(root.right)
            if(right==-1):return -1
            return max(left,right)+1 if abs(left-right)<2 else -1
        return depth(root)!=-1

```

## 111.最小深度

```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if(not root):return 0
        if(not root.left):return self.minDepth(root.right)+1
        if(not root.right):return self.minDepth(root.left)+1
        return min(self.minDepth(root.left),self.minDepth(root.right))+1
#四个出口条件，1.此时参数为None，返回0即可，表示并不增加深度
#           2.左子树节点为空，返回右子节点的最小深度+1，。为什么不返回0，因为此时这个节点可能不是叶子节点，还要考察右子树节点
#           3.与上面类似
#           4.左右子树都有节点，那么返回左右子树中的最小深度，并且+1

```

```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if(root==None):
            return 0
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1
#这个是错的，因为对于[1,2]，应该返回2，上面的写法返回了1.

```

广度优先遍历：

```python
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if(not root):return 0
        queue = deque([(1,root)])
        while(queue):
            depth,node=queue.popleft()
            if(not node.left and not node.right):return depth
            if(node.left):queue.append((depth+1,node.left))
            if(node.right):queue.append((depth+1,node.right))

```

## 112.路径总和

1.递归法：

```python
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if(not root):return False
        if(root.val==sum and not root.left and not root.right):
            return True
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
```

2.深度优先搜索，迭代：

```python
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if(not root):return False
        stack=[(root,sum-root.val)]
        while(stack):
            node,cur_sum=stack.pop()
            if(not node.left and not node.right and cur_sum==0):
                return True
            if(node.left):
                stack.append((node.left,cur_sum-node.left.val))
            if(node.right):
                stack.append((node.right,cur_sum-node.right.val))
                   
        return False

```

## 118.杨辉三角

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        for i in range(numRows):
            now=[1]*(i+1)   #初始化每一行的数组，并且开头和结尾肯定为1
            if(i>=2):   #当三行或者三行以上才会进入找个条件
                for j in range(1,i):
                    now[j]=pre[j-1]+pre[j]
            result.append(now)
            pre=now
        return result

```

## 121.买卖股票的最佳时机

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pri=float('inf')
        profit=0
        for i in prices:
            if i<min_pri:
                min_pri=i
            elif i-min_pri>profit:
                profit=i-min_pri
        return profit

```

## 122.买卖股票的最佳时机(2)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        length=len(prices)
        maxprofit=0
        while(i<length-1):
            while(i<length-1 and prices[i]>=prices[i+1]):
                i+=1
            valley=prices[i]
            while(i<length-1 and prices[i]<prices[i+1]):
                i+=1
            peak=prices[i]
            maxprofit+=peak-valley
        return maxprofit

```

## 125.验证回文串

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(filter(str.isalnum,s)).lower()
        return s[::-1]==s

```

## 141.环形链表

```python
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a=set()
        while(head):
            if(head in a):
                return True
            else:a.add(head)
            head=head.next
        return False

```

filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
该函数接收两个参数，第一个为函数，第二个为迭代器，迭代器的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新的迭代器中。

## 150.逆波兰表达式

```python
#根据逆波兰表示法，求表达式的值。
# 
# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
# 
# 说明：
# 
# 
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
# 
# 
# 示例 1：
# 
# 输入: ["2", "1", "+", "3", "*"]
# 输出: 9
# 解释: ((2 + 1) * 3) = 9
# 
# 
# 示例 2：
# 
# 输入: ["4", "13", "5", "/", "+"]
# 输出: 6
# 解释: (4 + (13 / 5)) = 6
# 
# 
# 示例 3：
# 
# 输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# 输出: 22
# 解释: 
# ⁠ ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
# 
#
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    # python的 b / a 会向下取整， 比如 -1 / 132 = -1。 
                    #题目要求是取整数部分，那么负数的时候，实际应该是向上取整
                    # 解决方法： int(b / float(a))
                    stack.append(int(l/float(r)))
        return stack.pop()

```



## 155.最小栈

关键在于如何始终保存着最小值，可以引入一个辅助栈，这个栈相当于只保存data栈里面由底向上递减的那些数。

data删除栈顶元素的时候，如果它大于辅助栈的栈顶元素，就不用管，如果小于等于辅助栈栈顶元素，则在辅助栈也要删一个。

```python
class MinStack(object):
    def __init__(self):
        self.data=[]
        self.helper=[]
    def push(self, x):
        self.data.append(x)
        if(len(self.helper)==0 or x<=self.helper[-1]):
            self.helper.append(x)
    def pop(self):
        if(self.data[-1]<=self.helper[-1]):
            self.helper.pop()
        self.data.pop()
    def top(self):
        return self.data[-1]
    def getMin(self):
        return self.helper[-1]

```

## 173.二叉搜索树迭代器

push_back函数，给它一个节点，它会把这个节点一路取左节点放进栈里，这个过程在root节点初始化用到，以及取右节点的时候用到。

```python
class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self.push_stack(root)
    def next(self):
        tmp = self.stack.pop()
        if tmp.right:
            self.push_stack(tmp.right)
        return tmp.val
    def push_stack(self,node):
        while(node):
            self.stack.append(node)
            node=node.left
        
    def hasNext(self):
        return bool(self.stack)

```

## 232.两个栈实现一个队列

```python
class MyQueue:
    def __init__(self):
        self.stackA=[]
        self.stackB=[]
    def push(self, x: int) -> None:
        self.stackA.append(x)
    def pop(self) -> int:
        if self.stackB:
            return self.stackB.pop()
        if not self.stackA:
            return None
        else:
            while(self.stackA):
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()
    def peek(self) -> int:
        if(self.stackB):
            return self.stackB[-1]
        if(not self.stackA):
            return None
        else:
            return self.stackA[0]
    def empty(self) -> bool:
        if not self.stackA and not self.stackB:
            return True
        else:
            return False

```



## 237.删除链表中的节点

给一个节点要求删除当前节点。由于不知道头结点，肯定无法跑到前驱然后再删除。可以把下一个节点的值赋给当前节点，然后删除下一个节点。

```python
class Solution:
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next

```



## 938.二叉搜索树的范围和

1.递归版：对节点的值进行比较，递归调用。需要注意的是，节点值可能会小于L或者大于R，这时候对于前者要继续找L.right，对于后者要继续找R.left。

出口条件是刚好在L和R之间，直接算入总和里。

```python
class Solution(object):
    def rangeSumBST(self, root, L, R):
        if not root:return 0
        numsum=0
        if(L<=root.val<=R):
            numsum+=root.val
            numsum+=self.rangeSumBST(root.left,L,R)
            numsum+=self.rangeSumBST(root.right,L,R)
        if(L>root.val):
            numsum+=self.rangeSumBST(root.right,L,R)
        if(R<root.val):
            numsum+=self.rangeSumBST(root.left,L,R)
        return numsum

```

2.非递归版:采用迭代算法，把需要判断的加入栈，反复执行检查直到该访问的都访问到位。

```
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack,summ=[],0
        stack.append(root)
        while(stack):
            t=stack.pop()
            if(t):
                if(L<=t.val<=R):
                    summ+=t.val
                if(L<t.val):
                    stack.append(t.left)
                if(t.val<R):
                    stack.append(t.right)
        return summ

```

## [49] 字母异位词分组

```python
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 
# 示例:
# 
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# 说明：
# 
# 
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
# 建立一个字典，key就是不同的字母异位词，用tuple保存，因为key必须是不可变类型。
# 对每一个字符串排序转换为tuple，看是否在字典中找到，如果找到，就把新词加到后面，否则添加进去。
# 最后返回字典所有的值
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram={}
        for str in strs:
            key=tuple(sorted(str))
            anagram[key]=anagram.get(key,[])+[str]
        return anagram.values()
```

## [50] Pow(x, n)

```python
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
# 
# 示例 1:
# 
# 输入: 2.00000, 10
# 输出: 1024.00000
# 
# 
# 示例 2:
# 
# 输入: 2.10000, 3
# 输出: 9.26100
# 
# 
# 示例 3:
# 
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 说明:
# 
# 
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
# 
# 用递归做，小技巧是指数为偶数可以转换为底数改为底数的平方，指数变为原来1/2
#
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==1:return x
        if n==0:return 1
        if n<0:
            return 1/self.myPow(x,-n)
        if n%2:
            return x*self.myPow(x,n-1)
        return self.myPow(x*x,n/2)

```

## [54] 螺旋矩阵

```python
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
# 
# 示例 1:
# 
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2:
# 
# 输入:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix:
            return list(matrix.pop(0))+self.spiralOrder(zip(*matrix)[::-1])
#要给matrix.pop(0)加上list，因为第二次及以后pop出来的是元组
        else:
            return []

```

## [55] 跳跃游戏

```python
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 判断你是否能够到达最后一个位置。
# 
# 示例 1:
# 
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
# 
# 
# 示例 2:
# 
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
# 
# 
#
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal=len(nums)-1
        for i in reversed(range(len(nums))):
            if nums[i]+i>=goal:	#如果可以从i位置跳不大于nums[i]步到达goal,缩小goal
                goal=i
        return not goal		#遍历到0如果goal不是0，返回False，为0说明可以从开始到达最后一个位置
```

## [56] 合并区间

```python
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 示例 1:
# 
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
#先数组排序，这样每个区间的左边界都是递增排列，判断的时候只需要判断后者的左边界是否小于前者的右边界
#如果是取出两个区间右边界的最大值作为前一个的右边界。因为是排过序的，所以每次只需要和前一个比较就行了。
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        new=[]
        for i in sorted(intervals):
            if new and i[0]<=new[-1][-1]:
                new[-1][-1]=max(i[-1],new[-1][-1])
            else:
                new.append(i)
        return new
```

## [61] 旋转链表

```python
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 
# 
# 示例 2:
# 
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p=head
        length=0
        while(p):
            p=p.next
            length+=1   #求链表长度

        k=k%length
        if length<=1 or k==0:return head   #边界情况    

        step=length-k-1
        p=head
        while(step):
            p=p.next
            step-=1     
        new_head=p.next
        p.next=None     #定位新的头结点,并且设置尾节点

        joint=new_head
        while(joint and joint.next):
            joint=joint.next
        joint.next=head         #拼接操作

        return new_head
```

## [64] 最小路径和

```python

# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 动态规划的思想。每个位置都可以从上或者从左边走到，求到这个位置的最短路径，也就是取上面位置和左边位置中路径最短的，依次下去，最终都是到达上边界或者左边界，而到左边界和上边界的最短距离都是确定的。这样依次分解就求出了最短路径。
#
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row=len(grid)
        column=len(grid[0])
        for i in range(1,column):
            grid[0][i]+=grid[0][i-1]	#求上边界
        for j in range(1,row):		
            grid[j][0]+=grid[j-1][0]		#求左边界
        
        for j in range(1,row):
            for i in range(1,column):
                grid[j][i]+=min(grid[j][i-1],grid[j-1][i])		#动态规划
        return grid[-1][-1]

```

## [75] 颜色分类

```python
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
# 
# 示例:
# 
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 
# 进阶：
# 
# 
# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
# 
# 三指针，red指针在最左边，管理0，blue指针在最右边，管理2，white在中间遍历，碰到0就和red指针交换，并且red+1，white不变，碰到2就和blue交换，并且blue-1,white不变。碰到1就跳过，直到最后white和bule指针相遇，说明遍历完成。
#
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red=white=0
        blue=len(nums)-1
        while white<=blue:
            if nums[white]==0:
                nums[white],nums[red]=nums[red],nums[white]
                white+=1
                red+=1
            elif nums[white]==1:
                white+=1
            else:
                nums[white]==2
                nums[white],nums[blue]=nums[blue],nums[white]
                blue-=1
```

## [78] 子集

```python
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#第一种方法：递归
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(0,[],nums,res)
        return res
    def dfs(self,index,path,nums,res):
        res.append(path)
        for i in xrange(index,len(nums)):
            self.dfs(i+1,path+[nums[i]],nums,res)

#第二种：列表推导式
class Solution(object):
    def subsets(self, nums):
        res=[[]]
        for num in nums:
            res+=[[num]+item for item in res]
        return res
```

## [79] 单词搜索

```python
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 示例:
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
# 
#
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(board,r,c,word):
                    return True
        return False
    def dfs(self, board,r,c,word):
        if len(word)==0:return True	#若没有半路返回False且匹配了所有的字符，说明找到了。
        if (not 0<=r<=len(board)-1) or (not 0<=c<=len(board[0])-1) or word[0]!=board[r][c]:		#跳出边界线，或者首字母不相同，返回False
            return False
        temp=board[r][c]
        board[r][c]='#'		#设为哑值，以免后面重复
#        for one in board:
#            print(one)
#        print()
        res=self.dfs(board,r-1,c,word[1:]) or self.dfs(board,r,c-1,word[1:])\
        or self.dfs(board,r+1,c,word[1:]) or self.dfs(board,r,c+1,word[1:])
    													#对于每一个数上下左右齐头并进查找
        board[r][c]=temp
        return res
```

## [82] 删除排序链表中的重复元素 II

```python
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
# 
# 示例 1:
# 
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 
# 
# 示例 2:
# 
# 输入: 1->1->1->2->3
# 输出: 2->3
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        p=ListNode(0)
        p.next = head
        head=p
        left=ListNode(0)
        right=ListNode(0)
        while p.next:
            left=right=p.next		#p用来遍历，left和right用来标识相同的数字的两端
            while right.next and right.val == right.next.val:
                right=right.next
            if left==right: 	#相等说明right没有移动，也就是没找到重复的
                p=p.next
            else:
                p.next=right.next		#拼接操作
        return head.next		#这里要通过头结点的前一个节点来访问，不能用return head，要保证返回的指针不能参与内部的删减，它应该在外层观望，以免被修改。

```

##  [86] 分隔链表

```python

# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 
# 你应当保留两个分区中每个节点的初始相对位置。
# 
# 示例:
# 
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#最简单的思路是新建两个链表，小于x的放在一个，另一个放大于等于x的，最后拼接起来。
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val<x:
                l1.next = head
                l1=l1.next
            else:
                l2.next = head
                l2=l2.next
            head=head.next
        l2.next = None
        l1.next = h2.next
        return h1.next
```

## [89] 格雷编码

```python
# 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
# 
# 给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。
# 
# 示例 1:
# 
# 输入: 2
# 输出: [0,1,3,2]
# 解释:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# 
# 对于给定的 n，其格雷编码序列并不唯一。
# 例如，[0,2,3,1] 也是一个有效的格雷编码序列。
# 
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
# 
# 示例 2:
# 
# 输入: 0
# 输出: [0]
# 解释: 我们定义格雷编码序列必须以 0 开头。
# 给定编码总位数为 n 的格雷编码序列，其长度为 2^n。当 n = 0 时，长度为 2^0 = 1。
# 因此，当 n = 0 时，其格雷编码序列为 [0]。
# 
# 利用镜像对称，
#
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[0]
        for i in range(n):
            k=len(res)
            for j in reversed(range(k)):
                res.append(res[j]|1<<i)
        return res

```

## [90] 子集 II

```python
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res,cur=[[]],[]
        if not nums:
            return res
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                cur=[item+[nums[i]] for item in cur]
                                #这里的cur表示上一次添加的数组
                                #如果碰到了相同元素，为了避免重复，不能直接和res相加
                                #应该只在上一次的基础上加新东西，然后再加到res里面
            else:
                cur=[item+[nums[i]] for item in res]
            res+=cur
        return res
```



## [92] 反转链表 II

```python
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#和前面一样，p要在外面，tail始终指向下一个移动的目标
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n: return head
        p =tail= ListNode(0)
        p.next= head
        head=p
        for i in range(1,n+1):  #定好起始位置，在这里起始是第一个节点，那么i起始应该设置为1
            if i<m:
                p=p.next
            elif i==m:
                tail=p.next
            else:
                temp=ListNode(0)
                temp=tail.next
                tail.next=tail.next.next
                temp.next=p.next
                p.next=temp
        return head.next
```

##  [781] 森林中的兔子

```python
# 森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在 answers 数组里。
# 
# 返回森林中兔子的最少数量。
# 
# 
# 示例:
# 输入: answers = [1, 1, 2]
# 输出: 5
# 解释:
# 两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
# 之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
# 设回答了 "2" 的兔子为蓝色。
# 此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
# 因此森林中兔子的最少数量是 5: 3 只回答的和 2 只没有回答的。
# 
# 输入: answers = [10, 10, 10]
# 输出: 11
# 
# 输入: answers = []
# 输出: 0
# 
# 
# 说明:
# 
# 
# answers 的长度最大为1000。
# answers[i] 是在 [0, 999] 范围内的整数。
# 用hash来统计answers中每个数字出现的次数； 然后就是开始处理哈希表里面的统计结果了； 例如， 5出现了8次， 那么至少得2*（5+1）只兔子； 如果5出现了6次呢？ 至少需要6只兔子； 如果5出现了3次呢？ 还是6只兔子； 当val出现了t次， 如果t%（val+1） == 0， 需要（t/（val+1））*（val+1）只兔子； 如果没有整除， 则至少需要(t/(val+1)+1)*(val+1)只兔子；

from collections import Counter
import math
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        ans=Counter(answers)
        cnt=0
        print(ans)
        for each,number in ans.items():
            if each+1>=number:
                cnt+=each+1
            else:
                a=math.ceil(number/(each+1))*(each+1)
                cnt+=a
        return int(cnt)
```



## [5207] 尽可能使字符串相等

给你两个长度相同的字符串，`s` 和 `t`。

将 `s` 中的第 `i` 个字符变到 `t` 中的第 `i` 个字符需要 `|s[i] - t[i]|` 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。

用于变更字符串的最大预算是 `maxCost`。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。

如果你可以将 `s` 的子字符串转化为它在 `t` 中对应的子字符串，则返回可以转化的最大长度。

如果 `s` 中没有子字符串可以转化成 `t` 中对应的子字符串，则返回 `0`。

 

**示例 1：**

```
输入：s = "abcd", t = "bcdf", cost = 3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。
```

**示例 2：**

```
输入：s = "abcd", t = "cdef", cost = 3
输出：1
解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。
```

**示例 3：**

```
输入：s = "abcd", t = "acde", cost = 0
输出：1
解释：你无法作出任何改动，所以最大长度为 1。
```

 

**提示：**

- `1 <= s.length, t.length <= 10^5`

- `0 <= maxCost <= 10^6`

- `s` 和 `t` 都只含小写英文字母。

  

```python
class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        windowsum=0
        ans=0
        left=0
        A=[abs(ord(s[i])-ord(t[i])) for i in range(len(s))]
        for right,num in enumerate(A):      #外层循环负责用来移动右边的指针
            windowsum+=num
            while windowsum>maxCost:        #内层循环用来移动左指针
                windowsum-=A[left]
                left+=1
            windowlen=right - left + 1
            if windowlen>ans:
                ans = windowlen
        return ans
```

##   [5206].删除字符串中的所有相邻重复项 II

```python
 # 给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们
 # 使被删去的字符串的左侧和右侧连在一起。
 # 
 # 你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。
 # 
 # 在执行完所有删除操作后，返回最终得到的字符串。
 # 
 # 本题答案保证唯一。
 # 
 # 示例 1：
 # 
 # 输入：s = "abcd", k = 2
 # 输出："abcd"
 # 解释：没有要删除的内容。
 # 示例 2：
 # 
 # 输入：s = "deeedbbcccbdaa", k = 3
 # 输出："aa"
 # 解释： 
 # 先删除 "eee" 和 "ccc"，得到 "ddbbbdaa"
 # 再删除 "bbb"，得到 "dddaa"
 # 最后删除 "ddd"，得到 "aa"
 # 示例 3：
 # 
 # 输入：s = "pbbcggttciiippooaais", k = 2
 # 输出："ps"
 # 提示：
 # 1 <= s.length <= 10^5
 # 2 <= k <= 10^4
 # s 中只含有小写英文字母。
 #用栈


class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack=[]
        for c in s:
            if not stack:
                stack.append([c,1])
            elif stack[-1][0]!=c:
                stack.append([c,1])
            elif stack[-1][-1]+1<k:       #相等之后
                stack[-1][-1]+=1
            else:
                stack.pop()
                
        s=''
        print(stack)
        for c,count in stack:
            s+=count*c
        return s

```

## [263] 丑数

```python
# 编写一个程序判断给定的数是否为丑数。
# 
# 丑数就是只包含质因数 2, 3, 5 的正整数。
# 
# 示例 1:
# 
# 输入: 6
# 输出: true
# 解释: 6 = 2 × 3
# 
# 示例 2:
# 
# 输入: 8
# 输出: true
# 解释: 8 = 2 × 2 × 2
# 
# 
# 示例 3:
# 
# 输入: 14
# 输出: false 
# 解释: 14 不是丑数，因为它包含了另外一个质因数 7。
# 
# 说明：
# 
# 
# 1 是丑数。
# 输入不会超过 32 位有符号整数的范围: [−2^31,  2^31 − 1]。
# 
# 
#
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0:return False
        if num==1:return True
        if num%2==0:return self.isUgly(num/2)
        if num%3==0:return self.isUgly(num/3)
        if num%5==0:return self.isUgly(num/5)
        return False

```

## [264] 丑数 II

```python
# 编写一个程序，找出第 n 个丑数。
# 
# 丑数就是只包含质因数 2, 3, 5 的正整数。
# 
# 示例:
# 
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 
# 说明:  
# 
# 
# 1 是丑数。
# n 不超过1690。
# 
# 
#三指针
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly=[1]
        i2,i3,i5=0,0,0
        while n>=2:
            next2,next3,next5=ugly[i2]*2,ugly[i3]*3,ugly[i5]*5
            next=min(next2,next3,next5)
            if next==next2:
                i2+=1
            if next==next3:
                i3+=1
            if next==next5:
                i5+=1
            ugly.append(next)
            n-=1
        print(ugly)
        return ugly[-1]
        

```



## 5198. 丑数 III

```python
#请你帮忙设计一个程序，用来找出第 `n` 个丑数。
#
#丑数是可以被 `a` **或** `b` **或** `c` 整除的 **正整数**。

#**示例 1：**
#
#```
#输入：n = 3, a = 2, b = 3, c = 5
#输出：4
#解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
#```
#
#**示例 2：**
#
#```
#输入：n = 4, a = 2, b = 3, c = 4
#输出：6
#解释：丑数序列为 2, 3, 4, 6, 8, 9, 12... 其中第 4 个是 6。
#```
#
#**示例 3：**
#
#```
#输入：n = 5, a = 2, b = 11, c = 13
#输出：10
#解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
#```
#
#**示例 4：**

#输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
#输出：1999999984

#**提示：**
#
#1 <= n, a, b, c <= 10^9
#1 <= a * b * c <= 10^18
# 本题结果在 [1, 2 * 10^9]的范围内
#二分查找
from fractions import gcd
class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        #最小公倍数
        def lcm(a,b):
            return a*b/gcd(a,b)
       #计算[1,mid]有多少丑数
       #这种实现时间复杂度会高一个log(n)数量级，最小公倍数可以预处理。
        def get_idx(mid):		#容斥原理
            return mid // a + mid // b + mid // c - mid //lcm(a,b) - mid//lcm(b,c) - mid //lcm(c,a) + mid//lcm(lcm(a,b),c)
        l = 1; r = 2*10**9+1
        while ( l < r ):
            mid = (l+r+1)/2
            idx = get_idx(mid)
            if idx == n:
                l = mid
                break
            elif idx < n:
                l = mid
            elif idx > n:
                r = mid-1
				return l-min(l%a,l%b,l%c)
```

## [63] 不同路径 II

```python
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 
# 
# 
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 
# 说明：m 和 n 的值均不超过 100。
# 
# 示例 1:
# 
# 输入:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 
# 动态规划
#
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:return 0
        row_len=len(obstacleGrid)
        col_len=len(obstacleGrid[0])
        obstacleGrid[0][0] =1-obstacleGrid[0][0]
        for r in range(1,row_len):
            obstacleGrid[r][0]=obstacleGrid[r-1][0]*(obstacleGrid[r][0]==0)
        for c in range(1,col_len):
            obstacleGrid[0][c]=obstacleGrid[0][c-1]*(obstacleGrid[0][c]==0)
        for r in range(1,row_len):
            for c in range(1,col_len):
                obstacleGrid[r][c]=(obstacleGrid[r-1][c]+obstacleGrid[r][c-1])*(obstacleGrid[r][c]==0)
        return obstacleGrid[-1][-1]


```

## [120] 三角形最小路径和

```python
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 
# 例如，给定三角形：
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 
# 说明：
# 
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
# 
#动态规划
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j==0:
                    triangle[i][j]=triangle[i-1][j]+triangle[i][j]
                elif j==len(triangle[i])-1:
                    triangle[i][j]=triangle[i-1][j-1]+triangle[i][j]
                else:
                    triangle[i][j]=min(triangle[i-1][j],triangle[i-1][j-1])+triangle[i][j]
        return min(triangle[-1])

```

## [139] 单词拆分

```python
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 
# 说明：
# 
# 
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 
# 
# 示例 2：
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 动态规划

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True              #这里的dp[0]=True并不表示位置，而是表示一种初始状态
        for i in range(1,n+1):
            for word in wordDict:       #同一个位置可能有好几种到达的方式，所以要遍历wordDict
                if i>=len(word) and dp[i-len(word)] and s[i-len(word):i]==word:
                    dp[i]=True          #dp[i]为True表示从头分割的话可以分割到第i个位置来
                                        
        return dp[-1]
        
```

## [152] 乘积最大子序列

```python
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
#动态规划
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=imax=imin=nums[0]
        for i in range(1,len(nums)):
            candidates = (nums[i], imax * nums[i], imin * nums[i])
            imax = max(candidates)
            imin = min(candidates)
            res=max(res,imax)
        return res

```

## [198] 打家劫舍

```python
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
# 
# 示例 1:
# 
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
# 示例 2:
# 
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#动态规划
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        n=len(nums)
        if n==0:return 0
        if n==1:return nums[0]
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(dp[0],nums[1])
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]

```

## [213] 打家劫舍 II

```python
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
# 
# 示例 1:
# 
# 输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
# 
# 
# 示例 2:
# 
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:return 0
        if len(nums)==1:return nums[0]
        def help(nums):
            n=len(nums)
            if n==0:return 0
            if n==1:return nums[0]
            dp=[0]*n
            dp[0]=nums[0]
            dp[1]=max(dp[0],nums[1])
            for i in range(2,n):
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
            return dp[-1]

        return max(help(nums[1:]),help(nums[:-1]))


```

## [221] 最大正方形

```python
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
# 
# 示例:
# 
# 输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:return 0
        res=0
        row=len(matrix)
        col=len(matrix[0])
        dp=[[0 for _ in range(col+1)] for _ in range(row+1)]
        
        for i in range(1,row+1):
            for j in range(1,col+1):
                if matrix[i-1][j-1]=='1':
                    dp[i][j]=min(int(dp[i-1][j-1]),int(dp[i-1][j]),int(dp[i][j-1]))+1
                    res=max(res,dp[i][j])
        return res*res


```

## [279] 完全平方数

```python
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# 
# 示例 1:
# 
# 输入: n = 12
# 输出: 3 
# 解释: 12 = 4 + 4 + 4.
# 
# 示例 2:
# 
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.
# 
#
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        for i in range(1,n+1):
            j=1
            imin=float('inf')
            while i-j*j>=0:
                imin=min(imin,dp[i-j*j]+1)
                j+=1
            dp[i]=imin
        return dp[n]
            

```

## [300] 最长上升子序列

```python
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# 
# 示例:
# 
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 
# 说明:
# 
# 
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
# 
# 
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
# 
#动态规划
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:return 0
        dp=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # + 1 的位置不要加错了
                    dp[i] = max(dp[i],dp[j] + 1)
        # 最后要全部走一遍，看最大值
        return max(dp)

```