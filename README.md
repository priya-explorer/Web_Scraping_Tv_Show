# Web Scraping of the top 250 IMDb tv shows
 
## The web scraping is done using Python 

Web Scraping or Data Scraping is a technique used to extract content and data from the website. This collected information is then exported into a format that is useful for user.

## Steps involved in web scraping using Beautiful Soup in Python
   ### 1) Find the URL that you want to scraped
   
   ### 2) Inspect the page
   
        To inspect the page, just right click on the element and click on “Inspect”. 
        
   ### 3) Find the tags/elements to extract data.
   
   ### 4) Write and run the code to extract data - 
      
        a) Create a python file
        
        b) Install the neccessary libraries such as, requests, BeautifulSoup and pandas for web scraping. 
             
           i) requests - It is a Python HTTP library. The HTTP request returns a response Object with all the response data (content, encoding,                                  status,..). 
    
                To Install Requests - 
          
                      pip install requests
    
                Syntax - 
          
                      requests.method(parameters)
    
               This module has several built-in methods to make a HTTP requests to a specific URL using GET, POST, PUT, PATCH or HEAD. The get() is                    used to retrieve information from the given URL.
                  
                 Syntax -
                      requests.get(url, params={key: value}, args)
           
           ii) BeautifulSoup - Beautiful Soup is a Python library for pulling data out of HTML/XML files. It transforms a complex HTML file into a                                    tree of Python objects.
      
                 To install Beautiful Soup
          
                     pip install beautifulsoup4
          
          iii) Pandas - Is used for working with datasets. It has functions for analyzing, cleaning, exploring, and manipulating data. We will use it,                         to show the extracted data, in the form of a dataframe and export it to a csv file.
          
      
      c) Write a code to open the URL using the "get()" method. Check if the code was run successfully using  "status_code".
      
      d) Extract the data and store it in a variable using find(), find_all() method from BeautifulSoup.
      
  ### 5) Store the extracted data in the required format.
  
         A data frame is created and exported into a csv(comma seperated values) file.
           
