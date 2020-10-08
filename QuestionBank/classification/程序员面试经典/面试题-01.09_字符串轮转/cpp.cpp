class Solution {
public:
    bool isFlipedString(string s1, string s2) {
        if (s1 == "" && s2 == "")
            return true;
        s1 += s1;
        return  s1.size() == s2.size()*2 && 
                s1.find(s2) != string::npos;
    }
};