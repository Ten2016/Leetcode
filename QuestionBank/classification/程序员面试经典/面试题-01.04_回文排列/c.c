bool canPermutePalindrome(char* s){
    char set[256] = {0};
    for(char *p = s; *p != 0; p++)
        set[*p]++;
    bool flag = false;
    for(int i =0; i < 256; i++) {
        if(set[i] & 1) {
            if(flag)
                return false;
            flag = true;
        }
    }
    return true;
}