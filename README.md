# XSLT test
## Description
XSLT, which from the book database, where the titles and ISBN code are indicated, displays the database as a tree in HTML format:
- Authors in alphabetical order,
- Under each author there are his alphabetical books in alphabetical order with the number of sales

## Structer
  <ul>
      <li>books.xml - initial data base of books</li> 
      <li>book.py - skript which refactor books.xml to output.xml file</li>
      <li>output.xml - output.xml file with ready sorted data by author</li>
      <li>SimpleNSTest.xsl - file for rendered and transformed XML file</li>
  </ul>



**How to start**
<p>Use following commands to start refactoring xml file:</p>

<br><b>start</b> - the structure of the request will be:
<div><em>Run book.py using any IDE</em></div>
<div><em>Use your browser, copy the local address of your folder with the output .xml file and put it in the browser.</em></div>


**Result**

<h1>Found books</h1>
<pAuthor: Corets, Eva</p>
  <ul>
    <li >Book title: Oberon's Legacy | was soled - 14</li>
    <li >Book title: The Sundered Grail | was soled - 75</li>
  </ul>


Author: Galos, Mike
Book title: Visual Studio 7: A Comprehensive Guide | was soled - 25
Author: Gambardella, Matthew
Book title: XML Developer's Guide | was soled - 4
Author: Garcia, Debra
Book title: Maeve Ascendant | was soled - 32
Author: Garghentini, Davide
Book title: Midnight Rain | was soled - 134
Author: Knorr, Stefan
Book title: Creepy Crawlies | was soled - 63
Author: Kress, Peter
Book title: Paradox Lost | was soled - 16
Author: O'Brien, Tim
Book title: Microsoft .NET: The Programming Bible | was soled - 35
Book title: MSXML3: A Comprehensive Guide | was soled - 53
Author: Randall, Cynthia
Book title: Lover Birds | was soled - 22
Author: Thurman, Paula
Book title: Splish Splash | was soled - 76





