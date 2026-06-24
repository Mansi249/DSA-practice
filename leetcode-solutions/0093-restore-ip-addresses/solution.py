class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []

        def dfs(i):
            if len(path) == 4:
                if i == len(s):
                    res.append(".".join(path))
                return

            for j in range(i, min(i + 3, len(s))):
                part = s[i:j + 1]

                if len(part) > 1 and part[0] == "0":
                    continue
                if int(part) > 255:
                    continue

                path.append(part)
                dfs(j + 1)
                path.pop()

        dfs(0)
        return res
