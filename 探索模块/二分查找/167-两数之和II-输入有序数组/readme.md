# 分析

方法一：
	两遍for循环
	时间复杂度O(n^2)
	超时

方法二：
	双指针p,q
	如果nums[p]+nums[q]>target
		q--
	如果nums[p]+nums[q]<target
		p++
	时间复杂度O(n)[n<=len(nums)]

方法三：对方法二优化
	折半查找，如果mid大于target
	则只会出现在左边
	则right=mid
	接着再用方法二的步骤

# 程序见本文件夹