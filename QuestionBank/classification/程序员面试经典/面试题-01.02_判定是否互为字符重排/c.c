bool CheckPermutation(char* s1, char* s2){
    char set[100] = {0};
    char *p = s1;
    while(*p != 0) {
        set[*(p++) - 'A']++;
    }
    p = s2;
    while(*p != 0) {
        if(set[*p - 'A'] == 0) {
            return false;
        }
        set[*(p++) - 'A']--;
    }
    return true;
}
/**
* 使用数组模拟集合
*
*/