char* replaceSpaces(char* S, int length){
    int i=length-1, j=strlen(S)-1;
    while(i >= 0) {
        if(S[i] == ' ') {
            S[j] = '0';
            S[j-1] = '2';
            S[j-2] = '%';
            j-=3;
        }
        else {
            S[j--] = S[i];
        }
        i--;
    }
    return S+j+1;
}