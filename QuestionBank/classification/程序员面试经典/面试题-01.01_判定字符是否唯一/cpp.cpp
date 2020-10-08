class Solution {
public:
    bool isUnique(string astr) {
        unordered_set<char> uset_my;
        for(auto c : astr) {
            if(uset_my.find(c) != uset_my.end()) {
                return false;
            }
            uset_my.emplace(c);
        }
        return true;
    }
};
/**
* 使用无序集合
*
*/