class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int m = matrix.size();
        for (int i = 0; i < m/2; i++) {
            for (int j = 0; j < m; j++) {
                auto tmp = matrix[i][j];
                matrix[i][j] = matrix[m-i-1][j];
                matrix[m-i-1][j] = tmp;
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = i; j < m; j++) {
                auto tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
        
        return ;
    }
};
/**
*
* 这里利用了一个算法
* 上下反转，再反斜线 \ 对称
* 相当于旋转90°
*
*/