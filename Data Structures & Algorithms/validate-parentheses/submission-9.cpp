class Solution {
public:
    bool isValid(string s) {
        if(s.length() < 2) return false;

        std::stack<char> st;

        st.push(s[0]);
        short idx = 1;

        while(!st.empty() || idx < s.length())
        {
            if(idx >= s.length()) return false;

            char sign = s[idx];
            if(sign == '[' || sign == '{' || sign == '(')
            {
                st.push(sign);
                idx++;
                continue;
            }
            else
            {
                if(st.empty()) return false;
                
                char top = st.top();

                std::cout << top << '\n';
                
                if(sign == ')' && top == '(')
                {
                    st.pop();
                }
                else if(sign == '}' && top == '{')
                {
                    st.pop();
                }
                else if(sign == ']' && top == '[')
                {
                    st.pop();
                }
                else
                {
                    return false;
                }

                idx++;
            }
        }

        if(st.empty() && idx == s.length()) return true;
        return false;
    }
};
