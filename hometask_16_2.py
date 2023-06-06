import re
def abbreviatura(text):
    t = re.findall(r'\b\w', text)
    print(''.join(map(str, [i.title() for i in t])))

text = 'московский государственный университет'  # 'Институт точной механики оптики'
abbreviatura(text)
