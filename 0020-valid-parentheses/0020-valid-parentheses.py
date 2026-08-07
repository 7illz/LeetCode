class Solution(object):
    def isValid(self, s):
        var = []
        flag = False

        for i in range(len(s)):
            if i == 0 and (s[i] == ')' or s[i] == '}' or s[i] == ']'):
                return False

            if s[i] == '(':
                var.append(')')

            if s[i] == '{':
                var.append('}')

            if s[i] == '[':
                var.append(']')

            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                if not var:
                    return flag
                if var[-1] == s[i]:
                    var.pop(-1)
                else:
                    return flag

        if not var:
            flag = True

        return flag