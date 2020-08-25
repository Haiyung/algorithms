// DFS 代码模板


// 递归写法


//JavaScript
const visited = new Set()
const dfs = node => {
    if (visited.has(node)) return
    visited.add(node)
    dfs(node.left)
    dfs(node.right)
}