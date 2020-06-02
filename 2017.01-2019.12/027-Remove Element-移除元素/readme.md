# 分析

方法一：
	# 针对python
	使用nums.remove()方法移除val
	返回新nums长度

方法二：
	一重循环
	初始指针p指向index(0)
	循环i遍历nums
	遇到非val元素,将nums(i)元素直接覆盖nums(p)
	将index(p)向后移一位，直至遍历结束
	遍历结束后，返回index(p)
	时间复杂度：O(n)
	空间复杂度：O(1)
	# 较快

方法三：
	初始指针p指向index(0)，q指向index(len(nums))
	p<=q
	如果：
		遇到val元素,将nums(q)元素直接覆盖nums(p)
		q--
	否则：
		p++	
	返回p	
	时间复杂度：O(n)-----（n为要删除的数的个数）
	空间复杂度：O(1)
	# 最快


# 程序见本文件	