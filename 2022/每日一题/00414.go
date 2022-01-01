/**

414. 第三大的数

给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hand-of-straights
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

**/

package main

import (
	"fmt"
)

func thirdMax(nums []int) int {
    l := len(nums)
    if l == 1 {
        return nums[0]
    }
    if l == 2 {
        if nums[0] > nums[1] {
            return nums[0]
        }
        return nums[1]
    }

    // 冒泡排序
    cnt := 0
    i := 0
    for ; i < l - 1 && cnt < 3; i++ {
        for j := 0; j < l - i - 1; j++ {
            if nums[j] > nums[j+1] {
                nums[j], nums[j+1] = nums[j+1], nums[j]
            }
        }
        cnt++
        if i != 0 && nums[l-i-1] == nums[l-i] {
            cnt--
        }
    }

    return nums[l-i-1]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func main() {

	param_1 := []int{7, 2, 10, 6, 2, 3, 4, 7, 8}

	res := thirdMax(param_1)

	fmt.Println(res)

	return
}
