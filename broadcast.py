import iso8601
from datetime import datetime
import pytz


class Broadcast(object):
    def __init__(self, pid, text, start, end):
        self.pid = pid
        self.text = text
        self.start = start
        self.end = end

    def __str__(self):
        return '{0}:{1}:[{2} - {3}]'.format(self.pid, self.text,
                                            self.start, self.end)

    def is_on_air(self):
        now = pytz.UTC.localize(datetime.utcnow())
        return self.start <= now <= self.end

    def is_on_air_next(self):
        now = pytz.UTC.localize(datetime.utcnow())
        return self.start > now

    @staticmethod
    def from_dictionary(dictionary):
        pid = dictionary['pid']
        title = dictionary['programme']['display_titles']['title']
        subtitle = dictionary['programme']['display_titles']['subtitle']
        start = iso8601.parse_date(dictionary['start'])
        end = iso8601.parse_date(dictionary['end'])

        # FIXME - some hard to debug unicode decoding problem
        try:
            text = '{0}:{1}'.format(title, subtitle)
        except:
            text = ''

        return Broadcast(pid, text, start, end)

