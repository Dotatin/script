import telnetlib
import time


def show_interface_brief(tn):
	tn.write('terminal length 35 \n')
	tn.write('show int bri\n')
	tn.read_until('show int bri', timeout =1)
	time.sleep(1)
	result = tn.read_very_eager()
	print(result)

def show_log(tn):
	print ('Enter the number of lines (min=35) (max=200):')
	number_of_lines = raw_input()
	if int(number_of_lines) <= 200:
		tn.write('terminal length ' + number_of_lines + '\n')
		tn.write('show log ram \n')
		time.sleep(1)
		tn.read_until('show log ram')
		result = tn.read_very_eager()
		print(result)
	else:
		print('The number of lines is more than 200')

def disable_port_security(tn, port):
	tn.write('configure\n')
	tn.write('int eth 1/' + port + '\n' )
	tn.write('no port security\n')
	time.sleep(1)
	tn.write('exit \n')
	tn.write('exit \n')
	time.sleep(1)
	print('Success')

def Port_Utilization(tn, port):
	tn.write('terminal length 0 \n')
	tn.write('show int cou eth 1/'+ port + '\n')
	time.sleep(1)
	tn.read_until('Port Utilization (recent 300 seconds)', timeout =1)
	result = tn.read_very_eager()
	print(result)

def review_mac_address(tn, company):
	if company == 1:#Proline
		mac_address = '00-1E-F7-41-C3-C0'
		tn.write('show mac-address-table address'+ mac_address + '\n')
		time.sleep(1) 
		tn.read_until('show mac-address-table address 00-1E-F7-41-C3-C0', timeout =1)
		result = tn.read_very_eager()
		print(result)
	elif company == 2:#Delta
		mac_address = '00-1B-0D-E4-79-00'
		tn.write('show mac-address-table address'+ mac_address + '\n')
		time.sleep(1) 
		tn.read_until('show mac-address-table address 00-1B-0D-E4-79-00', timeout =1)
		result = tn.read_very_eager()
		print(result)
	elif company == 3:#Rusanovka
		mac_address = '00-24-14-2C-E8-80'
		tn.write('show mac-address-table address'+ mac_address + '\n')
		time.sleep(1) 
		tn.read_until('show mac-address-table address 00-24-14-2C-E8-80', timeout =1)
		result = tn.read_very_eager()
		print(result)
	elif company == 4:#Sunline
		mac_address = '00-1D-70-82-CC-C0'
		tn.write('show mac-address-table address '+ mac_address + '\n')
		time.sleep(1) 
		tn.read_until('show mac-address-table address 00-1D-70-82-CC-C0', timeout =1)
		result = tn.read_very_eager()
	elif company == 5:#Bereznyaki
		mac_address = '00-18-74-2D-EF-C0'
		tn.write('show mac-address-table address'+ mac_address + '\n')
		time.sleep(1) 
		tn.read_until('show mac-address-table address 00-18-74-2D-EF-C0', timeout =1)
		result = tn.read_very_eager()
		print(result)

def switch_control_edgecore(telnet_host, company):
	tn = telnet_host
	print('\nWrite port:')
	port = raw_input()
	while True:
		print('\nAction:\n1. View interfaces\n')
		print('2. Disable port security\n')
		print('3. View log\n')
		print('4. View utilization ports\n')
		print('5. View mac-address cisco\n')
		print('6. Leave the switch\n')
		print('Your Answer:')

		action = int(raw_input())
		if action == 1:
			show_interface_brief(tn)
		elif action == 2:
			disable_port_security(tn, port)
		elif action == 3:
			show_log(tn)
		elif action == 4:
			Port_Utilization(tn, port)
		elif action == 5:
			review_mac_address(tn, company)
		elif action == 6:
			leave_the_switch(tn)
			break
