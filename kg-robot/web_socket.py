# 编写自己的web服务器，发送html页面
# http是给予TCP实现的
import socket

def service_client(new_socket):
    request = new_socket.recv(1024).decode("utf-8")
    print(request)

    response_head = "HTTP/1.1 200 OK\r\n"
    # 分割http响应头和响应body
    response_head += '\r\n'
    response_body = read_html('test.html').decode('utf-8')
    data = response_head + response_body
    new_socket.send(data.encode("utf-8"))
    new_socket.close()

def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定
    tcp_server_socket.bind(("", 7090))
    # 3. 监听套接字
    tcp_server_socket.listen(128)
    while True:
        # 4. 等待连接
        new_socket, client_addr = tcp_server_socket.accept()
        # 5. 发送数据
        service_client(new_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


def read_html(file_path):
    file = open(file_path, 'rb')
    file_data = file.read()
    file.close()
    return file_data


if __name__ == '__main__':
    main()

