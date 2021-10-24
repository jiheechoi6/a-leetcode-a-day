class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<pair<int, int>> dirc = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        vector<int> step_size = {int(matrix[0].size()), int(matrix.size()-1)};  //vertical, horizontal
        vector<int> answer = {};
        
        pair<int, int> cur_pos = {-1, 0};
        int dir_idx = 0;
        while(step_size[0] || step_size[1]){
            int step = step_size[dir_idx%2];
            if(!step) break;
            for(int i=0; i<step; i++){
                cur_pos.first += dirc[dir_idx].first;
                cur_pos.second += dirc[dir_idx].second;
                answer.push_back(matrix[cur_pos.second][cur_pos.first]);
            }
            step_size[dir_idx%2]--;
            dir_idx = ++dir_idx % 4;
        }
        
        return answer;
    }
};
