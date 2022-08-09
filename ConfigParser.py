import re
from Configuration import Configuration

def configParser(config_file):

	# Read file lines
	lines = config_file.readlines()

	argv = {}
	true_list = ['on', 'yes', 'true']
	false_list = ['off','no', 'false']

	for line in lines:

		# Filter out comments and ignore invalid lines (assuming valid lines include '=')
		if line.startswith('#') or '=' not in line : continue

		# Remove white spaces and new lines
		line = line.replace(' ','').strip()

		# Extract key value pairs
		key, value = line.split('=')

		# Check for boolean type
		if value.lower() in true_list: value = True
		elif value.lower() in false_list: value = False

		# Check for int and float values, considering negative values
		elif value.replace('-','').isnumeric(): value = int(value)
		elif value.replace('.','').replace('-','').isnumeric(): value = float(value)

		# Add to dictionary
		argv.update({key:value})

	# Create and return object
	return Configuration(argv)

if __name__ == '__main__':

	# Read config file
	# Example: C:\Folder\configFile.txt
	file_path = input('Please Enter Configuration File Path Including Name = ')
	config_file = open(file_path, 'r')

	# Call parser function
	config = configParser(config_file)

	# Print example attribute of the object
	print('Host = ', config.host)
	print('Server ID = ', config.server_id)
	print('Debug Mode = ', config.debug_mode)
