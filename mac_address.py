import subprocess
import optparse

def get_args():
	parser = optparse.OptionParser()
	parser.add_option('-i', '--interface', dest = 'interface', help = 'Interface to change its MAC address')
	parser.add_option('-m', '--mac', dest = 'mac', help = 'New Mac Address')
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error('[-] Please specify an interface, use --help for more info.')
	elif not options.mac:
		parser.error('[-] Please specify the new mac, use --help for more info.')
	else:
		return options

def run_terminal(interface,mac):
	print('[+] Changing Mac Address of interface ' + interface + ' to ' + mac)
	subprocess.call(f"sudo ifconfig {interface} down && sudo ifconfig {interface} hw ether {mac} && sudo ifconfig {interface} up", shell = True)

options = get_args()
run_terminal(options.interface,options.mac)

