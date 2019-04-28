import urllib.request
import urllib.parse
MY_KEY = 'nWwXuR2SarCqzc07Rcq10Ou8SC-7fw8UDA1g2fEZ2A0'
ALERT_EVENT = 'alert1'

params = urllib.parse.urlencode({'value1': 'project lost power'})
data = params.encode('ascii')
url = 'https://maker.ifttt.com/trigger/{}/with/key/{}'
url = url.format(ALERT_EVENT, MY_KEY)
with urllib.request.urlopen(url, data) as f:
	print(f.read().decode('utf-8'))