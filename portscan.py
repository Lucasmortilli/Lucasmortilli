import socket
porta = [21, 22, 23, 433, 70, 80,8080, 50, 30]

for portas in range(1, 6000):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.0)
	c = s.connect_ex(('bancocn.com', portas))
	if c == 11 or 0:
		print(portas, c)
