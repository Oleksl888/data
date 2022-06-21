'''Создайте XML файл с вложенными элементами и воспользуйтесь языком поиска XPATH.
Попробуйте осуществить поиск содержимого по созданному документу XML, усложняя свои запросы
и добавляя новые элементы, если потребуется.'''

from xml.etree import ElementTree as ET


root = ET.Element('pets')
root.set('somekey', str(True))

for num in range(3):
    child = ET.SubElement(root, 'pet')
    child.set('id', str(num))
    for i in range(3):
        subchild = ET.SubElement(child, 'characteristic'+str(i))
        subchild.text = 'value' + str(i)
print(ET.dump(root))
tree = ET.ElementTree(root)
tree.write('pets.xml', encoding='utf8')

contents = ET.parse('pets.xml')
root = contents.getroot()
print(root.tag)
for elem in root.findall('./pet'):
    print(elem.attrib, elem.tag, elem.text)

for elem in root.findall('./pet'):
    for item in elem:
        print(item.attrib, item.tag, item.text)

elem = root.findall('./pet[@id][1]')[0]
for item in elem:
    print(item.text)

elem = root.findall('./pet[@id="2"]/characteristic1')


