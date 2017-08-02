import ConfigParser
parser = ConfigParser.ConfigParser()
parser.read("settings.ini")

print "Sections: ", parser.sections()

print "Network:", parser.options('Network')
print "Network->Host:", parser.get('Network', 'Host')

parser.set('Network', 'Port', '40')
print "Network->Port:", parser.get('Network', 'Port')

# Writing our configuration file to 'settings.ini'
#with open('settings.ini', 'wb') as configfile:
with open('settings.ini', 'w') as configfile:
    parser.write(configfile)
