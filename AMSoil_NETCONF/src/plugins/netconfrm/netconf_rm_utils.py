__author__ = 'zanetworker'

import xml.etree.ElementTree as ET
from xml.dom.minidom import Document

def parseXML(xml_string, parameter_to_filter):
        """
        Filter important parameters from the device config

        args:
            xml_string: the whole xml tree string
            parameter_to_filter:

        return:
            The filtered sub tree
        """
        root = ET.fromstring(xml_string)
        for child in root:
            return ET.tostring(child) if parameter_to_filter in child.tag else None




class dict2xml(object):
    doc = Document()

    def __init__(self, structure):
        if len(structure) == 1:
            rootName    = str(structure.keys()[0])
            self.root   = self.doc.createElement(rootName)

            self.doc.sappendChild(self.root)
            self.build(self.root, structure[rootName])

    def build(self, father, structure):
        if type(structure) == dict:
            for k in structure:
                tag = self.doc.createElement(k)
                father.appendChild(tag)
                self.build(tag, structure[k])

        elif type(structure) == list:
            grandFather = father.parentNode
            tagName     = father.tagName
            grandFather.removeChild(father)
            for l in structure:
                tag = self.doc.createElement(tagName)
                self.build(tag, l)
                grandFather.appendChild(tag)

        else:
            data    = str(structure)
            tag     = self.doc.createTextNode(data)
            father.appendChild(tag)

    def display(self):
        return self.doc.toprettyxml(indent="  ")
