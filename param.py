import os, sys, re, argparse
def get_args():
	print ("\033[91m")
	os.system('cat banner')
	print ("\033[0m")
	parser = argparse.ArgumentParser()
	parser.add_argument('-f','--filename',dest='urls',help='Specify your urls file.')
	args = parser.parse_args()
	if not args.urls:
		sys.exit(parser.print_help())
	else:
		return args
def main():
	args = get_args()
	file = args.urls
	lis = []
	urls = open(file,'r')
	for url in urls:
		if "?" in url and "=" in url:
			x = re.findall('[?].*=',url)
			if x not in lis:
				lis.append(x)
	return lis
if __name__ == '__main__':
	param = main()
	for i in param:
		for x in i :
			print (x)
