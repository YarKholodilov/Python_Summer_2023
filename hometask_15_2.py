import re
# letters = 'ETYOPAHKCBMXУКЕНХВАРОСМТ'

numbers = 'P070ТА178 A123УFУC178 A123RC178 A12GУC78 A123УC78'
regex = r'[ETYOPAHKCBMXУКЕНХВАРОСМТ]{1}\d{3}[ETYOPAHKCBMXУКЕНХВАРОСМТ]{2}178|[ETYOPAHKCBMXУКЕНХВАРОСМТ]{1}\d{3}[ETYOPAHKCBMXУКЕНХВАРОСМТ]{2}78'
auto = re.findall(regex, numbers)
print(*auto, sep='\n')
