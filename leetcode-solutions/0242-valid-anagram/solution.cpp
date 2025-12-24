class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }
        unordered_map<char,int> anag;
        for( char c: s){
            anag[c]++;
        }
        for(char c:t){
            if(anag[c] ==0){
                return false;
            }
            anag[c]--;
        }
        return true;
    }
};
