class Solution:
    def simplifyPath(self, path: str) -> str:
        can_path = path.split('/')
        res = []
        for d in can_path:
            if d == "..":
                if len(res) >= 2:
                    res.pop()
                    res.pop()
                
            elif d and d != '.':
                res.append('/')
                res.append(d)
        return "".join(res) if res else '/'
            