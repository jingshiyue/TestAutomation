# coding:utf-8
import pika
import os


def send_msg(msg) ->str:
    """
    将消息体发送到队列中
    :param msg: 要发送的消息
    :return:
    """
    credentials = pika.PlainCredentials(username="root", password="123456")
    parameters = pika.ConnectionParameters(host="192.168.10.184",
                                           port=5672,
                                           virtual_host="/",
                                           credentials=credentials)
    connection = pika.BlockingConnection(parameters=parameters,)
    channel = connection.channel() #获得信道
    channel.queue_declare(queue="bt_sec_queue",  #声明队列
                          durable=True)
    channel.basic_publish(exchange="",  #发布消息
                          routing_key="bt_sec_queue",
                          body=msg,)
    #print(" [x] Sent %r:%r" % ("bt_sec_queue", msg))
    connection.close()


def msg_str(filepath,Type):
    """
    定义要发送的消息体
    :param filepath: 打开的文件路径
    :param Type: 打开的文件流形式 “rb”，“r”，“w”
    :return:
    """
    with open(file=filepath,mode=Type) as fp:
        data = fp.read()
        return data


if __name__ == '__main__':
    live_p_path = "E:/picture"
    id_p_path = "E:/IDcard"
    list_2 = os.listdir(live_p_path)
    list_1 = os.listdir(id_p_path)
    for i in list_2:
        print(i)
    print(len(os.listdir(id_p_path)))











