'''
基本概念：

   socket通常也称作"套接字"，用于描述IP地址和端口，是一个通信链的句柄，应用程序通常通过"套接字"向网络发出请求或者应答网络请求。
   两个程序通过“网络”交互数据就使用socket，它只负责两件事：建立连接，传递数据
   socket(family,type[,protocal]) 使用给定的地址族、套接字类型、协议编号（默认为0）来创建套接字
   socket类型

描述：

    socket.AF_UNIX          只能够用于单一的Unix系统进程间通信

    socket.AF_INET          服务器之间网络通信

    socket.AF_INET6         IPv6

    socket.SOCK_STREAM      流式socket , for TCP

    socket.SOCK_DGRAM       数据报式socket , for UDP

    socket.SOCK_RAW         原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次，SOCK_RAW也可以处理特殊的IPv4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头。

    socket.SOCK_SEQPACKET   可靠的连续数据包服务

    创建TCP Socket：         s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    创建UDP Socket：         s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

注意点：

    TCP发送数据时，已建立好TCP连接，所以不需要指定地址。UDP是面向无连接的，每次发送要指定是发给谁。
    服务端与客户端不能直接发送列表，元组，字典。需要字符串化repr(data)。

常见的socket函数：

    服务端函数：
        s.bind(address)             将套接字绑定到地址, 在AF_INET下,以元组（host,port）的形式表示地址.

        s.listen(backlog)           开始监听TCP传入连接。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。

        s.accept()                  接受TCP连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。

    客户端函数：
        s.connect(address)          连接到address处的套接字。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。

    公共的函数：
        s.recv(bufsize[,flag])      接受TCP套接字的数据。数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。

        s.send(string[,flag])       发送TCP数据。将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。

        s.sendall(string[,flag])    完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。

        s.close()                   关闭套接字。

基本的socket编程思路：

    TCP服务端：

        1 创建套接字，绑定套接字到本地IP与端口            # socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.bind()

        2 开始监听连接                                  #s.listen()

        3 进入循环，不断接受客户端的连接请求            #s.accept()

        4 然后接收传来的数据，并发送给对方数据         #s.recv() , s.sendall()

        5 传输完毕后，关闭套接字                     #s.close()



    TCP客户端:

        1 创建套接字，连接远端地址            # socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.connect()

        2 连接后发送数据和接收数据          # s.sendall(), s.recv()

        3 传输完毕后，关闭套接字          #s.close()

特别强调：TCP发送数据时，已建立好TCP连接，所以不需要指定地址。UDP是面向无连接的，每次发送要指定是发给谁。


'''

# 导入socket模块
import socket

# 设置好目标地址和端口
target_host = "127.0.0.1"

target_port = 80

# 创建UDP的网络通信对象
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 发送数据
client.sendto(b"hello",(target_host,target_port))   # 每次发送数据都要加上目标地址和端口

# 接收返回的信息并且打印出来
data,addr = client.recvfrom(4096)

print(data)

# 关闭连接
client.close()
