# Open using 'with'
with open('monitored.txt') as f:
    for service in f:
        print(service, end=' ')

to_monitor = ('httpd', 'dovecot', 'postfix')

# Existing file will be overwritten 
with open('monitored_new.txt', 'w') as f:
    for service in to_monitor:
        f.write(service)
        f.write('\n')

# Open to append 
with open('monitored.log', 'a') as f:
    f.write(f'Monitored: {to_monitor}\n')
