# XSLT test
## Description
XSLT, which from the book database, where the titles and ISBN code are indicated, displays the database as a tree in HTML format:
- Authors in alphabetical order,
- Under each author there are his alphabetical books in alphabetical order with the number of sales
  <ul>
      <li>books.xml - initial data base of books</li> 
      <li>book.py - skript which refactor books.xml to output.xml file</li>
      <li>SimpleNSTest.xsl - file for rendered and transformed XML file</li>
  </ul>



**How to start**
<p>Use following commands to start refactoring xml file:</p>

<br><b>/start</b> - the structure of the request will be:
<div><em>General request [LowPrice/HighPrice].</em></div>
    <ul>
        <li>City</li>
        <li>Date</li>
        <li>Mode[LowPrice/HighPrice]</li>
        <li>Number of hotels</li>
        <li>Show pictures</li>
        <li>Show pictures</li>
        <li>Show pictures[Yes/No]</li>
            <ul>
                <li>Number of pictures</li>
            </ul>
        <li>Location(Region)</li>
    </ul>

<div><em>Example:</em></div>


