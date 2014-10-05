import xml.etree.ElementTree as etree

def ReadXml(xmlstr):
	root = etree.fromstring(xmlstr)
	print_xml(root)

def print_xml(root):
	if root.text is None:
		print(root.tag)
	else:
		print("%s: %s" % (root.tag, root.text))
	for child in root:
		print_xml(child)

if __name__ == "__main__":
	xmlstr = '<Address><to>James</to><from>Jani</from><heading>Reminder</heading><body>Please check your mail.</body></Address>'
	ReadXml(xmlstr)