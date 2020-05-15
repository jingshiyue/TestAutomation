# coding:utf-8
import redis
import json


class RedisDataBase(object):
    def __init__(self):
        self.host = "192.168.0.227"
        self.port = 6379
        self.pool = redis.ConnectionPool(host=self.host, port=self.port, password="cigit")
        self.conn = redis.Redis(connection_pool=self.pool)

    def get_hash_value(self, key, name="faceCompareChannel"):
        """通过Key值获取value,返回字典对象"""
        a = str(self.conn.hget(name, key), encoding="utf-8")
        return json.loads(a)

    def judge_exit_hash_key(self,key,name="faceCompareChannel",):
        """判断当前name中是否有对应的key"""
        return self.conn.hexists(name, key)

redis_connect = RedisDataBase()
if __name__ == '__main__':
    # a = RedisDataBase().get_hash_value(20)
    # print(a["flightNo"])
    # print(RedisDataBase().judge_exit_hash_key(100))

    a = [1,2,3]
