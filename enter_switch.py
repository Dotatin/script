import telnetlib
import time
def identification_dlink(user, password, tn):
	tn.write(user + '\n')
	tn.write(password + '\n')

def identification_edgecore(user, password, tn):
	tn.read_until('Username:')
	tn.write(user + '\n')
	tn.read_until('Password:')
	tn.write(password + '\n')