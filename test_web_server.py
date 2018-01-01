"""
	超简陋的web服务器，调试生成的html代码时使用

	:anthor:	s97712
	:date:		2018-01-01
"""

import socket
def start(host, port, content):
	"""
		启动web服务器

		Args:
			host:	监听的ip地址
			port:	监听的商品
			content:web服务器要显示的内容

	"""
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
	s.bind((host,port));
	s.listen(10);
	while 1:
		client_s, addr = s.accept();
		print("new connect");
		send_page(client_s, content);
	return 0;

def send_page(s, content):
	data = s.recv(10240)
	
	#print("recv:");
	#print(data.decode("utf-8"));

	template = "";
	template += "HTTP/1.1 200 OK\r\n";
	template += "Content-Length: {length}\r\n\r\n";
	
	template = template.format(length=len(content));
	template += content;


	#print("send:");
	#print(template);

	data = bytes(template,encoding="utf-8");
	s.sendall(data);
	s.close();


