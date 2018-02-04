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
# Step 1: Get the Command Line Arguments and Request the Search Page
# We notice that the google search url is 'http://google.com/search?q=SOMETHING
import requests, sys, webbrowser, bs4

print('Googling...') # Prints a message for the user
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result
# It looks like our search result links have an element "<h3 class="r">
linkElems = soup.select('.r a')

