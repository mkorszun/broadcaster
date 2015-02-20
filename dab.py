from datetime import datetime


class DABSender(object):
    def send(self, broadcasts):
        for b in broadcasts:
            print 'Processing {0}'.format(b)
            if b.is_on_air():
                self.send_onairnow(b.pid, b.text)
            if b.is_on_air_next():
                self.send_onairnext(b.pid, b.text)

    def send_onairnow(self, pid, text):
        msg = 'On air now {0}:{1}'.format(pid, text)
        self.log_to_file(msg)
        print msg

    def send_onairnext(self, pid, text):
        msg = 'On air next {0}:{1}'.format(pid, text)
        self.log_to_file(msg)
        print msg

    def log_to_file(self, content):
        with open("results.log", "a") as results:
            results.write('\n{0} {1}'.format(datetime.now(), content))
