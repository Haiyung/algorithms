# Source : https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
# Author : Haiyung
# Date   : 2020-08-25


'''电话号码的字母组合

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
'''


def letter_combinations(digits):
    telephone_digits = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def helper(result, digits, tmp, index):
        # terminator
        if index == len(digits):
            result.append(tmp)
            return

        # process logic
        digit = telephone_digits[digits[index]]
        for i in digit:
            t = tmp + i
            # drill down
            helper(result, digits, t, index + 1)

    result = []
    if len(digits) == 0:
        return result
    helper(result, digits, "", 0)
    return result


re = letter_combinations("23")
print(re)
