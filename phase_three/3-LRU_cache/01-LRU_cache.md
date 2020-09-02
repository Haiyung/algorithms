## Cache 缓存

缓存就像是人类的记忆(回忆起来很快，但常出错误)，准确度不如书籍；

缓存还像钱包，钱包里会放常用的东西，但容量有限，不如储物柜。

O(1) 查询

O(1) 修改、更新

## 缓存的两大要素：大小

缓存大，容量大，“记忆力”强；

缓存小，就要适时的执行替换策略。

## 缓存的两大要素：替换策略

- LFU => least frequently used 最近被使用频率最小的元素
- LRU => least recently used 最近最少被使用的元素 
- [...](https://en.wikipedia.org/wiki/Cache_replacement_policies)
