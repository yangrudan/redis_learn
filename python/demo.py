# 在线的用户,每分钟记录一个键, 判断在最近的10个集合键是否出现至少1次, 用SUNION命令实现

import web
import time
import redis

r = redis.StrictRedis()

"""配置路由规则
'/': 模拟用户的访问
'/online': 查看在线的用户
"""
urls = (
    '/', 'visit',
    '/online', 'online'
)
app = web.application(urls, globals())


"""返回当前时间对应的键名
如28分对应的键名是active.users:28
"""
def time_to_key(current_time):
    return "active.users:" + time.strftime('%M', time.localtime(current_time))


"""返回最近10分钟的键名
结果是列表类型
"""
def key_in_last_10_minutes():
    now = time.time()
    result = []
    for i in range(10):
        result.append(time_to_key(now - i *60))
    return result


class visit:
    """模拟用户访问
    将用户的user agent作为用户的ID加入当前时间对应的键中
    """
    def GET(self):
        user_id = web.ctx.env['HTTP_USER_AGENT']
        current_key = time_to_key(time.time())
        pipe = r.pipeline()
        pipe.sadd(current_key, user_id)
        # 设置键的生存时间10分钟
        pipe.expire(current_key, 10 * 60)
        pipe.execute()

        return 'User:\t ' + str(user_id) + '\r\nKey:\t' + current_key
    

class online:
    """查看当前在线的用户列表
    """
    def GET(self):
        online_users = r.sunion(key_in_last_10_minutes())
        result = ""
        for user in online_users:
            result += 'User Angent: ' + str(user) + '\r\n'
        return result
    

if __name__ == "__main__":
    app.run()