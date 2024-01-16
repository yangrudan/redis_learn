# 事务(transaction)

MULTI => QUEUED => EXEC 

**一个事务中的命令要么都执行, 要么都不执行**

# 过期时间

EXPIRE 设置过期时间

TTL 查看剩余时间

# 排序

* 1. SORT命令
  
  时间复杂度O(n + mlogm), n表示要排序的列表中元素个数, m表示要返回的元素个数;

* 2. BY参数

* 3. SORT命令的GET参数

* 4. STORE参数


# 消息通知

任务队列, 优先级队列, 发布订阅, 流与消费组, 管道
