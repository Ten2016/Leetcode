>>:题目描述：
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


>>:解法：
根据题目描述,想到最简单的方法就是先排序。
然后按照排序结果一次遍历,设置前后两个指针,标记连续的长度。
此方法时间复杂度为O(NlogN)。

另外,可以使用哈希表将数据存储起来,然后进行查找。


>>:程序：

//方法一,采用先排序再查找
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0) return 0;
        sort(nums.begin(), nums.end());
        int ans = 0;
        int i, k;
        for(i=1, k=0; i<nums.size(); ++i){
            if(nums[i] != nums[i-1]+1){
                if(nums[i] == nums[i-1])
                    ++k;
                else{
                    ans = max(ans, i-k);
                    k = i;
                }
            }
        }
        return max(ans, i-k);
    }
};

//方法二,采用哈希表查找

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0) return 0;
        unordered_set<int> set_t;
        for(auto i : nums)
            set_t.insert(i);
        int ans=0;
        for(auto i : set_t){
            if(set_t.count(i-1))
                continue;
            int k = i+1;
            while(set_t.count(k)) ++k;
            ans = max(ans, k-i);
        }
        return ans;
    }
};