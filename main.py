import telnetlib
import time
import enter_switch
import edgecore
import dlink


print('Select company:')
print('Your Answer:')
company = int(raw_input())


print('\nSelect switch:')
print('1.D-link 3526\n2.D-link 3028\n3.D-link 3200-28F\n4.Edge-Core')
switch = int(raw_input())

print('\nIP switch:')
HOST=raw_input()
HOST=HOST.replace('\t','')
tn = telnetlib.Telnet(HOST)

if switch == 4:
	enter_switch.identification_edgecore(user, password, tn)
else:
    enter_switch.identification_dlink(user, password, tn)

if switch == 4:
	edgecore.switch_control_edgecore(tn, company)
else:
	dlink.switch_control_dlink(tn, company, switch)
