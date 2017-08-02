import ConfigParser
parser = ConfigParser.ConfigParser()
parser.read("settings.ini")

print "Sections: ", parser.sections()

print "Network:", parser.options('Network')
print "Network->Host:", parser.get('Network', 'Host')
