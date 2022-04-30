##  An (almost) fully functional, but not yet complete implementation for scraping the results from [ProPokerTools](http://www.propokertools.com/pql) ##

Running PQL from the command line just got easier. This script will run your queries for you on the web version of [ProPokerTools](http://www.propokertools.com/pql).

Using BeautifulSoup, Requests and PIL, this script will take a string query and return a dictionary containing the results. In case the results are charts and histograms, this script will save it to the disk as a PNG image, and will return the path to the image, and open it for you.

I'm working on a Query Builder for this script as well. which would help you build your own queries.


### Usage ###

Import ```run_query``` function from propokertools module and supply it with your query. Some of the sample queries are shown in ```main.py``` file.

### Footnote ###

Please don't flood the website with incessant requests. It will get your IP blacklisted. It's a study tool, use it as such.

Star, fork, raise a PR or send me an [email](mailto:animpoker@gmail.com) if you have any questions or suggestions.
