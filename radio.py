import urllib2
import json
from broadcast import Broadcast
from dab import DABSender


class Radio(object):
    def __init__(self, url):
        self.url = url

    def get_schedule(self, date):
        response = urllib2.urlopen(self.build_url(date)).read()
        return json.loads(response)

    def build_url(self, date):
        if date:
            return '{0}/{1}.json'.format(self.url, date)
        else:
            return '{0}.json'.format(self.url)


class RadioScanner(object):
    DEFAULT_RADIOS = [
        Radio('http://www.bbc.co.uk/radio2/programmes/schedules'),
        Radio('http://www.bbc.co.uk/5livesportsextra/programmes/schedules'),
        Radio('http://www.bbc.co.uk/worldserviceradio/programmes/schedules')
    ]

    def __init__(self, radios=None, sender=None, date=None):
        self.radios = radios if radios else self.DEFAULT_RADIOS
        self.sender = sender if sender else DABSender()
        self.date = date

    def scan(self):
        for radio in self.radios:
            broadcasts = radio.get_schedule(self.date)['schedule']['day']['broadcasts']
            broadcast_objects = [Broadcast.from_dictionary(b) for b in broadcasts]
            self.sender.send(broadcast_objects)



