class Solution:
    def isValid(self, s: str):
        count = 0
        for i in s:
            if i == '(':
                count += 1
            if i == ')':
                count -=1
            if count < 0:
                return False
        return count == 0
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        answers = set()
        queue = [s]
        visited = set()
        while len(queue) > 0:
            item = queue.pop(0)
            if item in visited:
                continue
            if self.isValid(item):
                answers.add(item)
            if len(answers)>0:
                continue
            for i in range(len(item)):
                if item[i] not in '()':
                    continue
                l = list(item)
                del(l[i])
                string = "".join(l)
                queue.append(string)
            visited.add(item)
        return list(answers)