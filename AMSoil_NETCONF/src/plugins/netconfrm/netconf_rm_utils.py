
from xml.dom.minidom import Document


def parseXML(xml_string, parameter_to_filter):
    """
    Filter important parameters from the device config
    args:
        xml_string: the whole xml tree stringc
        parameter_to_filter
    return:
    The filtered sub tree
    """
    root = ET.fromstring(xml_string)
    for child in root:
        return ET.tostring(child) if parameter_to_filter in child.tag else None


def dictToXML(dict_to_convert, name_spaces):
    """
    convert a python dictionary to a NETCONF compatible xml
    args:
        dict_to_convert: the python dictionary containing the configuration values to convert
        name_spaces: the namespaces that will be used
    return:
    An open ended xml tree that will be used as an input for the xml wrapper
    """
    assert isinstance(dict_to_convert, dict), "Input is not a dictionary"
    assert len(dict_to_convert) > 0, "size of dictionary is zero "

    outputxml = ""
    list_of_tags = []

    for key, value in dict_to_convert.iteritems():
        if key == 'a':
            outputxml += "<%s xmlns=\"%s\">" % (value, name_spaces[0])
            list_of_tags.append(value)
        else:
            if isinstance(value, list):
                outputxml += "<%s xmlns=\"%s\">" % (key, value[0])
                list_of_tags.append(key)

                for value in value[1:]:
                    outputxml += dictToXML(value, None)[0]

            elif isinstance(value, dict):
                outputxml += "<%s>" % (value.keys()[0])
                list_of_tags.append(key)

                for key, item in value.keys(), value.values():
                    if isinstance(item, dict):
                        outputxml += dictToXML(item, None)[0]
                    else:
                        outputxml += "<%s>" % key + "<%s>" % value + "</%s>" % key
            else:
                outputxml += "<%s>" % key + "%s" % value + "</%s>" % key

    return outputxml, list_of_tags


def wrap_tags(xml_to_wrap, tags):
    """
    wraps the rest of the xml taps for producing the final xml configuration string
    args:
        xml_to_wrap: the xml tree produced from dict2xml
        tags: the rest of the tags to wrap around the open ended xml
    return:
    The final xml tree that will be used for configuration
    """

    if xml_to_wrap is not None:
        for index in range(len(tags)):
            xml_to_wrap += "</%s>" % tags.pop()

    return xml_to_wrap



# if __name__ == "__main__":
#     example = {'root': 'one', 'two': ['ns2', {'three': None}, {'four': 'four!'}]}
#     xml, tags = dictToXML(example, ['ns1', 'ns2'])
#     final_xml = wrap_tags(xml, tags)
#     print final_xml




