import socket

def start(host, port, content):
	
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
	
	print("recv:");
	print(data.decode("utf-8"));

	template = "";
	template += "HTTP/1.1 200 OK\r\n";
	template += "Content-Length: {length}\r\n\r\n";
	
	template = template.format(length=len(content));
	template += content;


	print("send:");
	print(template);
	data = bytes(template,encoding="utf-8");
	s.sendall(data);
	s.close();


