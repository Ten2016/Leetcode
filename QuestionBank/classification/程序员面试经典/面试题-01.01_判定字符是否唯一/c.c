bool isUnique(char* astr){
    char set[256] = {0};
    for(char *p = astr; *p != '\0'; p++) {
        if(set[*p] > 0)
            return false;
        set[*p]++;
    }
    return true;
}
/**
* 使用数组模拟集合
*
*/