class LogEntry(object):
    def __init__(self, line):
        self.line = line
        self.info = line.split(' ', 5)

    def printline(self):
        print(self.line)
        for entry in self.info:
            print(entry)
        print()

s = 'Mar 26 15:17:01 steve CRON[13135]: (root) CMD ( cd / && run-parts --report/etc/cron.hourly)' 
log = LogEntry(s)
log.printline() 

s = 'Mar 26 16:07:46 steve systemd[1]: Started Network Manager Script Dispatcher Service.' 
nextlog = LogEntry(s)
nextlog.printline()
