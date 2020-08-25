# 递归代码模板


# Python
def recursion(level, param1, param2):
    # recursion terminator 递归终止条件
    if level > MAX_LEVEL:
        process_result
        return

    # process logic in current level 处理当前层的业务逻辑
    process(level, data)

    # drill down 进入下一层
    self.recursion(level + 1, p1)

    # reverse the current level status if needed


'''Java
public void recur(int level, int param) { 
  // terminator 
  if (level > MAX_LEVEL) { 
    // process result 
    return; 
  }
  // process current logic 
  process(level, param); 
  // drill down 
  recur( level: level + 1, newParam); 
  // restore current status 
}
'''


'''JavaScript
const recursion = (level, params) =>{
   // recursion terminator
   if(level > MAX_LEVEL){
     process_result
     return 
   }
   // process current level
   process(level, params)
   //drill down
   recursion(level+1, params)
   //clean current level status if needed
}
'''
