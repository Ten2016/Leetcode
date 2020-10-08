bool func(char *p, char *q, int diff) {
    if(diff > 1)
        return false;
    if(*p == 0 && *q == 0)
        return true;
    if(*p == 0 || *q == 0) {
        if (diff > 0)
            return false;
        return  (*p == 0)&&(*(q+1) == 0) || 
                (*q == 0)&&(*(p+1) == 0);
    }
    if(*p == *q)
        return func(p+1, q+1, diff);
    return  func(p+1, q, diff+1) || 
            func(p, q+1, diff+1) ||
            func(p+1, q+1, diff+1);
}

bool oneEditAway(char* first, char* second){
	if(first == NULL || second == NULL)
		return false;
    return func(first, second, 0);
}