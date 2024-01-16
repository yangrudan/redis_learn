# 数据类型

**1.字符串类型**

**2.整形**

**3.哈希类型**

Redis并不要求每个键都依据此结构存储, 我们可以自由的为任何键增减字段而不影响其他键.

```
HSET key field value
HGET key field
HMSET key field value [field value ...]
HMGET key field [field ...]
HGETALL KEY
```

**4.列表类型**

**5.集合类型**

**6.有序集合类型**

**7.流类型**