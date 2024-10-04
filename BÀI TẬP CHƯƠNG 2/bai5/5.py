import xml.dom.minidom
def main():
    doc = xml.dom.minidom.parse("bai4\\sample.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    staff=doc.getElementsByTagName("staff")
    print("%d staff :"% staff.length)
    for id in staff:
        print(id.getAttribute("id"))
if __name__=="__main__":
    main();