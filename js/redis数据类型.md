# 数据类型

**字符串类型**

**整形**

**哈希类型**

Redis并不要求每个键都依据此结构存储, 我们可以自由的为任何键增减字段而不影响其他键.

```
HSET key field value
HGET key field
HMSET key field value [field value ...]
HMGET key field [field ...]
HGETALL KEY
