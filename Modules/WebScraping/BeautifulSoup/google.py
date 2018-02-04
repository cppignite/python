#! /usr/bin/python3
'''
  Whenever people do Google searches, they search and open several new tabs
  by middle-clicking on the first few top links. That's a lot of work. I want
  to just type the search term on my command line and all the top links 
  automatically open on my computer. Let's do that

  What the program will do:
   * Gets search keywords from command line arguments
   * Retrieves the search results page
   * Opens the browser tab for each result
     
  This is done by:
   * Reads the command line arguments from sys.argv
   * Fetch the search results page with the requests moduls
   * Finds the links to each search result
   * Call the webbrowser.open() function to open the browser
'''

