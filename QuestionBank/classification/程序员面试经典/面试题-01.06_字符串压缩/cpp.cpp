class Solution {
public:
    string compressString(string S) {
        int i=0, j=0;
        int len = S.size();
        string res;
        stringstream ss;
        while(j <= len) {
            if (j == len || S[i] != S[j]) {
                res += S[i];
                ss.str("");
                ss << j-i;
                res += ss.str();
                i = j;
            }
            j++;
        }
        return res.size()>=len?S:res;
    }
};