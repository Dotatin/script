import telnetlib
import time


def view_port_status(tn, port, switch):
	if switch == 1 or switch == 3:
		tn.write('show ports ' + port + '\n')
		time.sleep(0.5)
		tn.read_until('Command: show ports ' + port , timeout =1)
		result = tn.read_very_eager()
		print(result[1:340])
	else:
		tn.write('show ports ' + port + '\n' + 'q' + '\n' )
		time.sleep(0.5)
		tn.read_until('Command: show ports ' + port , timeout =1 )
		result = tn.read_very_eager()
		print(result[1:350])

def disable_port_security(tn,port, switch):
	if switch == 1 or switch == 2:
		tn.write('config port_sec ports  ' + port +  '  admin_state disable max_lea 2 lock_address DeleteOnTimeout\n')
	else:
		tn.write('config port_sec ports  ' + port +  '  admin_state disable max_lea 2 lock_address deleteontimeout \n')
	time.sleep(1)
	print('Success\n')

def view_error_ports(tn, port, switch):
	if switch == 1 or switch == 3:
		tn.write('show error ports '+ port +'\n')
		time.sleep(1)
		tn.read_until('Command: show error ports '+ port, timeout =1)
		result = tn.read_very_eager()
		print(result[3:603])
	else:
		tn.write('show error ports '+ port +'\n' + 'q' + '\n')
		time.sleep(1)
		tn.read_until('show error ports '+ port, timeout =1)
		result = tn.read_very_eager()
		print(result[2:620])

def view_utilization_ports(tn, port, switch):
	if switch == 1:
		tn.write('show utilization ports ' + port + '\n')
		time.sleep(1)
		tn.read_until('Command: show utilization ports', timeout =1)
		result = tn.read_very_eager()
		print(result[3:350])
	elif  switch == 2:
		tn.write('show utilization ports ' + port + '\n'  + 'q' + '\n')
		time.sleep(1)
		tn.read_until('Command: show utilization ports ' + port, timeout =1)
		result = tn.read_very_eager()
		print(result[1:110])
	elif  switch == 3:	
		tn.write('show utilization ports ' + '\n')
		time.sleep(1)
		tn.read_until('Command: show utilization ports', timeout =1)
		result = tn.read_very_eager()
		print(result[2:1768])

def view_mac_address_cisco(tn, company):
	if company == 1:#Proline
		mac_address = '00-1E-F7-41-C3-C0'
		tn.write('show fdb mac_address '+ mac_address + '\n')
		time.sleep(1) 
		tn.read_until('Command: show fdb mac_address ' + mac_address, timeout =1 )
		result = tn.read_very_eager()
		print(result)
	elif company == 2:#Delta
		mac_address = '00-1B-0D-E4-79-00'
		tn.write('show fdb mac_address '+ mac_address + '\n')
		time.sleep(1) 
		tn.read_until('Command: show fdb mac_address '+ mac_address, timeout =1 )
		result = tn.read_very_eager()
		print(result)
	elif company == 3:#Rusanovka
		mac_address = '00-24-14-2C-E8-80'
		tn.write('show fdb mac_address '+ mac_address + '\n')
		time.sleep(1) 
		tn.read_until('Command: show fdb mac_address '+ mac_address, timeout =1 )
		result = tn.read_very_eager()
		print(result)
	elif company == 4:#Sunline
		mac_address = '00-1D-70-82-CC-C0'
		tn.write('show fdb mac_address  '+ mac_address + '\n')
		time.sleep(1) 
		tn.read_until('Command: show fdb mac_address '+ mac_address, timeout =1)
		result = tn.read_very_eager()
		print(result)	
	elif company == 5:#Bereznyaki
		mac_address = '00-18-74-2D-EF-C0'
		tn.write('show fdb mac_address '+ mac_address + '\n')
		time.sleep(1) 
		tn.read_until('Command: show fdb mac_address '+ mac_address, timeout =1)
		result = tn.read_very_eager()
		print(result)	

def	leave_the_switch(tn):
	tn.write('logout')
	time.sleep(1)
	print('Success')

def switch_control_dlink(telnet_host, company,switch):
	tn = telnet_host
	print('\nWrite port')
	port = raw_input()
	while True:
		print('\nAction:\n1. View port status\n ')
		print('2. Disable port security\n')
		print('3. View error ports\n')
		print('4. View utilization ports\n')
		print('5. View mac-address cisco\n')
		print('6. Leave the switch\n')
		print('Your Answer:')

		action = int(raw_input())
		if action == 1:
			view_port_status(tn, port,switch)
		elif action == 2:
			disable_port_security(tn,port, switch)	
		elif action == 3:
			view_error_ports(tn, port,switch)
		elif action == 4:
			view_utilization_ports(tn, port,switch)
		elif action == 5:
 			view_mac_address_cisco(tn, company)
 		elif Action == 6:
 			leave_the_switch(tn)
			break