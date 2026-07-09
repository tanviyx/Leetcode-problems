class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        
        vector<vector<int>> matrix(n, vector<int>(n));

        int top = 0;
        int bottom = n - 1;
        int left = 0;
        int right = n - 1;

        int num = 1;

        while (top <= bottom && left <= right) {

            // 1. Fill top row (left -> right)
            for (int i = left; i <= right; i++) {
                matrix[top][i] = num++;
            }
            top++;

            // 2. Fill right column (top -> bottom)
            for (int i = top; i <= bottom; i++) {
                matrix[i][right] = num++;
            }
            right--;

            // 3. Fill bottom row (right -> left)
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    matrix[bottom][i] = num++;
                }
                bottom--;
            }

            // 4. Fill left column (bottom -> top)
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    matrix[i][left] = num++;
                }
                left++;
            }
        }

        return matrix;
    }
};