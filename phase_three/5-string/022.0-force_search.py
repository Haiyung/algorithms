# 字符串匹配暴力法代码示例


def forceSearch(txt, pat):
    n, m = len(txt), len(pat)
    for i in range(n-m+1):
        for j in range(m):
            if txt[i+j] != pat[j]:
                break
        if j == m:
            return i
    return -1
