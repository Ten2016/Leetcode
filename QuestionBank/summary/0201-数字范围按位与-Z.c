>>:题目描述：
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1: 

输入: [5,7]
输出: 4
示例 2:

输入: [0,1]
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


>>:解法：
根据题意,最简单的办法就是将m到n之间的所有数想与。
但是对于范围非常大的区间,会出现超时。
可以分析与运算的操作特点来进行优化。


>>:程序：

class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int ans = 0;
        while(m != n){
            m >>= 1;
            n >>= 1;
            ++ans;
        }
        return m<<ans;
    }
};