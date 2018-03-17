from xml.etree import ElementTree

tree = ElementTree.parse("example_modified.xml")
root = tree.getroot()

greg = root[0]
# module1 = next(greg.iter("module1"))
# print(module1, module1.text)
# print(type(module1))
# module1.text = str(float(module1.text) + 30)

# certificate = greg[2]
# certificate.set("type", "with distinction")

# description = ElementTree.Element("description")
# description.text = "Showed excellent skills during the course"
# greg.append(description)

description = greg.find("description")
greg.remove(description)

tree.write("example_modified.xml")