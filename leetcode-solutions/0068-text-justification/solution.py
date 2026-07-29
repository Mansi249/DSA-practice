class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        current_line = []
        current_len = 0
        for word in words:
            if len(word)+ current_len + len(current_line)<= maxWidth:
                current_line.append(word)
                current_len += len(word)
            else:
                formatted_line = self.formatline(current_line,current_len,maxWidth)
                res.append(formatted_line)
                current_line = [word]
                current_len = len(word)
        last_line = " ".join(current_line)
        trailing_space = maxWidth - len(last_line)
        res.append(last_line+" "*trailing_space)
        return res
    def formatline(self,line,length,maxWidth):
        if len(line) == 1:
            space = maxWidth - length
            return line[0] + " "*space
        total_space = maxWidth - length
        base_gap = total_space//(len(line)-1)
        extra_gap = total_space % (len(line)-1)
        res_str = ""
        for k in range(len(line)-1):
            res_str += line[k]
            res_str += " "* base_gap
            if k < extra_gap:
                res_str += " "
        res_str += line[-1]
        return res_str


