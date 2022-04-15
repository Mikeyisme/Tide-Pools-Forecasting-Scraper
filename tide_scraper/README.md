# Tide-Pools Forecast Scraper Description

A Python script that web-scrapes tides from https://www.tide-forecast.com/ using locations: Half Moon Bay, California Huntington Beach, California Providence, Rhode Island Wrightsville Beach, North Carolina.

The forecast page for each location is loaded, and information on low tides (date, time, height) that occur after sunrise and before sunset is extracted.

# Setup application

1. git clone the repo: https://github.com/Mikeyisme/Tide-Pools-Forecasting-Scraper.git

2. Setup Environment:
   ``` 
   cd /tide-scraper`
   pip install requests

   ```

# Running the application

Simply run the file and watch as information is diplayed in your terminal.

``` 

Python tide-scraper.py

```

# Data Extracted and Displayed

The tide scraper contains a set of events: 
 * sunrise
 * moonrise
 * sunset
 * low-tide
 * high-tide

 # Optimizing The Application

 This application could be extended to do more.
  * ideally an API could be used to generate such data 
  * organize data differently and support different output formats
  * scrape more data from the sites per location
  * support more queries
     * specific dates
 
