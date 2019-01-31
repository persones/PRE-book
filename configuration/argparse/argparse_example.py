import argparse
import yaml

parser = argparse.ArgumentParser(description="Weather station")
parser.add_argument('--interval', type=int)
parser.add_argument('--fan-pin', nargs=2, type=int, action="append")
parser.add_argument('--conf-file', nargs='?', 
  default='config.yaml')
parser.add_argument('-v', '--verbose',
  action="store_true", default=False)
args = parser.parse_args()

print('configuration file: {}'.format(args.conf_file))
with open(args.conf_file, 'r') as f:
  config = yaml.load(f)

if args.fan_pin:
  for fan_option in args.fan_pin:
    print('overriding fan {}: now using pin {}'.format(*fan_option))
    print('ss', config.fans[fan_option[[0]])

print('Verbose mode: {}'.format(args.verbose))


print(args.interval or 3)
