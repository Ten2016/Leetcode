class Solution {
public:
    bool CheckPermutation(string s1, string s2) {
        array<char, 100> arr_my {0};
        for( auto c : s1) {
            arr_my[c-'A']++;
        }
        for( auto c : s2) {
            if(arr_my[c-'A'] == 0)
                return false;
            arr_my[c-'A']--;
        }
        return true;

    }
};