class ServiceInfo(object):
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    # Default arguments for omitting calling arguments
    def alter(self, id, name=None, description=None):
        self.id = id
        if name != None:
            self.name = name
        if description != None:
            self.description = description

    # String representation for printing
    def __str__(self):
        return f'{self.id} {self.name}: {self.description}'

s = ServiceInfo(1021, 'synchronization-job', 'File synchronization process.')
print(s)
s.alter(1021, 'sync-job', 'File sync.')
print(s)
s.alter(1050)
print(s)
