## Approach

It's always the last resort to use scraping to get data. I tried reverse engineering the API from the website by using the Dev Tools and looking at the Network tab and seeing exactly what requests are being sent.

And mainly, I found that every alcohol's page is retrieved from a POST call to /api/single-liquor

Gotta remove the '&' characters from the XML file cause that messes up the parsing for some reason.
