// 字符串匹配暴力法代码示例

function bf(text, pattern) {
    let n = text.length;
    let m = pattern.length;
    for (let i = 0; i < n - m + 1; i++) {
        let matched = true;
        for (let j = 0; j < m; j++) {
            if (source[i + j] !== pattern[j]) {
                matched = false;
                break;
            }
        }
        if (matched) return true;
    }
    return false;
}

console.log(bf("abcabcabx", "abcabx"));