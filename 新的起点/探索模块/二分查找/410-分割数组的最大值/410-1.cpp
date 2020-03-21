class Solution {
public:
	int splitArray(vector<int>& nums, int m) {
		int size = nums.size();
		vector<int>row(size,0);
		vector<vector<int>>re;
		for (int i = 0; i <= m; i++)re.push_back(row);//二维数组
		//将数组分成1段的情况
		int sum = 0;
		for (int j = 0; j < size; j++){
			sum += nums[j];
			re[1][j] = sum;
		}
 
		//填表
		int temp, now;
		for (int i = 2; i <= m;i++){//i表示要分成的段数
			for (int j = i - 1; j < size;j++){
				temp = INT_MAX;
				for (int k = i - 2; k <= j - 1; k++){
					//re[i][j]表示将数组索引从0到j的元素分成i段
					now = max(re[i-1][k],re[1][j]-re[1][k]);
					if (now<=temp)temp = now;
				}
				re[i][j] = temp;
			}
		}
		return re[m][size - 1];
	}
};
