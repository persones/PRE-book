import argparse
#parser = argparse.ArgumentParser(description="Weather station")

#parser.add_argument('--fan-pin', nargs=2)
#parser.add_argument('--conf-file', nargs='?', 
#  default='conf.yml')
#parser.add_argument(['-v', '--verbose'],
#  action="store_true", default=False)

#args = parser.parse_args()


#parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description="Weather station")
parser.add_argument('--interval', type=int)
parser.add_argument('--fan-pin', nargs=2, action="append")
parser.add_argument('--conf-file', nargs='?', 
  default='conf.yml')
parser.add_argument('-v', '--verbose',
  action="store_true", default=False)
args = parser.parse_args()
print(args)
#print(str(args.interval+1))
print('Verbose mode: {}'.format(args.verbose))
if args.fan_pin:
  for fan_option in args.fan_pin:
    print('fan {} is using pin {}'.format(*fan_option))
print('configuration file: {}'.format(args.conf_file))

print(args.interval or 3)
