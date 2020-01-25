import subprocess
import optparse
import re


def get_args():
	parser = optparse.OptionParser()
	parser.add_option('-i', '--interface', dest = 'interface', help = 'Interface to change its MAC address')
	parser.add_option('-m', '--mac', dest = 'new_mac', help = 'New Mac Address')
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error('[-] Please specify an interface, use --help for more info.')
	elif not options.new_mac:
		parser.error('[-] Please specify the new mac, use --help for more info.')
	else:
		return options


def run_terminal(interface,new_mac):
	print('[+] Changing Mac Address of interface ' + interface + ' to ' + new_mac)
	subprocess.call(["sudo", "ifconfig", interface, "down"])
	subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["sudo", "ifconfig", interface, "up"])


def return_mac(interface):
	ifconfig_output = subprocess.check_output(['ifconfig',interface])
	result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_output))
	return result.group(0)


def check(interface,mac):
	ifconfig_output = subprocess.check_output(['ifconfig',interface])		
	result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_output))
	result = result.group(0)
	if result:
		if result == mac:
			print('[+] Successfully changed.')

		else:
			print('[-] Couldn\'t change MAC Address.')
	
	else:
		print('[-] Cannot find MAC Address. Aborting...')


options = get_args()
initial_mac = return_mac(options.interface)
print("[+] Inital MAC address is ",initial_mac)
run_terminal(options.interface,options.new_mac)
check(options.interface,options.new_mac)
final_mac = return_mac(options.interface)
print("[+] Final MAC address is ",final_mac)
