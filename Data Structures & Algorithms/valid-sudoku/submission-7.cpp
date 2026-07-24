class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        for(int i=0; i < board.size(); i++)
        {
            for(int j=0; j < board[i].size(); j++)
            {

                std::map<char,int> rowCheck = {};
                for(int k=j; k < board[i].size(); k++)
                {
                    if(board[i][k] == '.') continue;
                    if(rowCheck.count(board[i][k]))
                    {
                        return false;
                    }
                    else
                    {
                        rowCheck[board[i][k]] = 1;
                    }
                }

                // Check grid
                if(i % 3 == 0 && j % 3 == 0)
                {
                    std::map<char,int> gridCheck = {};
                    
                    for(int k=i; k < i+3; k++)
                    {
                        for(int l=j; l < j+3; l++)
                        {
                            if(board[k][l] == '.') continue;
                            if(gridCheck.count(board[k][l]))
                            {
                                return false;
                            }
                            else
                            {
                                gridCheck[board[k][l]] = 1;
                            }
                        }
                    }
                }

                // Check column
                std::map<char,int> colCheck = {};
                for(int k = i; k < board.size(); k++)
                {
                    if(board[k][j] == '.') continue;
                    if(colCheck.count(board[k][j]))
                    {
                        return false;
                    }
                    else
                    {
                        colCheck[board[k][j]] = 1;
                    }
                }
            }
        }

        return true;
    }
};
