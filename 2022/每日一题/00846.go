/**

846. 一手顺子

Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。

给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true ；否则，返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hand-of-straights
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

**/

package main

import (
	"fmt"
	"sort"
)

func isNStraightHand(hand []int, groupSize int) bool {
    l := len(hand)
    if l % groupSize != 0 {
        return false
    }
    sort.Ints(hand)

    // 算法复杂度 O(n^2)
    for i := 0; i <= l - groupSize; i++ {
        if hand[i] == -1 {
            continue
        }
        pre := hand[i]
        cnt := 1
        for j := i+1; j < l && cnt < groupSize; j++ {
            if hand[j] == -1 {
                continue
            }
            if hand[j] - pre > 1 {
                return false
            }
            if hand[j] == pre {
                continue
            }
            pre = hand[j]
            hand[j] = -1
            cnt++
        }
        if cnt != groupSize {
            return false
        }
    }

    return true
}

func main() {

	param_1 := []int{1, 2, 3, 6, 2, 3, 4, 7, 8}
	param_2 := 3

	res := isNStraightHand(param_1, param_2)

	fmt.Println(res)

	return
}
