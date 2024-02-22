from lxml import etree

doc = etree.parse('books.xml')  # Read books.xml file as tree (ElementTree).

authors = set()  # Empty sets of authors.
for author in doc.findall("./book/author"):
    authors.add(author.text)  # The record all authors in set. An extract repeat authors from the list.

sorted_authors = sorted(authors)  # The sort in alphabetical order all authors.

books = doc.findall("./book")  # An extract all <book> tags.

##########
page = etree.Element('html')  # Create a root element - <html> tag
headElt = etree.SubElement(page, 'head')  # Create a child element of the <html> - the <head> tag
bodyElt = etree.SubElement(page, 'body')  # Create a child element of the <html> tag - the <body> tag
catalogELT = etree.SubElement(bodyElt, 'catalog')  # Create a child element of the <body> tag - the <catalog> tag
##########

for author in sorted_authors:
    author_tag = etree.SubElement(catalogELT,
                                  'author')  # Create a child element of the <catalog> tag - the <author> tag
    author_name = etree.SubElement(author_tag, 'name')  # Create a child element of the <author> tag - the <name> tag
    author_name.text = author  # Add a text into author name tag

    for book in books:
        if book.find("author").text == author:  # Find all nodes(books) in xml tree
            book_tag = etree.SubElement(author_tag,
                                        'book')  # Create a child element of the <author> tag - the <book> tag
            title = etree.SubElement(book_tag, 'title')  # Create a child element of the <author> tag - the <name> tag
            title.text = book.find("title").text  # Add a text into author title tag
            purchased = etree.SubElement(book_tag,
                                         'purchased')  # Create a child element of the <book> tag - the <purchased> tag
            purchased.text = book.find("purchased").text  # Add a text into book purchased tag


def indent(elem, level=0):
    """
    HTML form creation method
    :param elem: _Element
    :param level: int
    :return: None
    """
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


indent(page)

xml_str = etree.tostring(page, encoding="utf-8", method="xml").decode()  # Refactor to string format
final_page = "<?xml version='1.0' encoding='UTF-8'?><?xml-stylesheet type='text/xsl' href='SimpleNSTest.xsl'?>" + xml_str

with open("output.xml", "w") as f:  # Record all created html
    f.write(final_page)
