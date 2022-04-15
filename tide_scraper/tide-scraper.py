from requests_html import HTMLSession

# create session
s = HTMLSession()


# create urls
query = { "HalfMoon": "Half-Moon-Bay-California/tides/latest", "Huntington": "Huntington-Beach/tides/latest", "Providence": "Providence-Rhode-Island/tides/latest","Wrightsville": "Wrightsville-Beach-North-Carolina/tides/latest" }
url = [f'https://www.tide-forecast.com/locations/{query["HalfMoon"]}', f'https://www.tide-forecast.com/locations/{query["Huntington"]}', f'https://www.tide-forecast.com/locations/{query["Providence"]}', f'https://www.tide-forecast.com/locations/{query["Wrightsville"]}']


# construction request to identify as a non-bot
pull = [s.get(url[0], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}),
s.get(url[1], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}),
s.get(url[2], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}),
s.get(url[3], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'})]


# gather the tide pools data from separate cities
HalfMoonBay = (pull[0].html.find('div.column', first=True).find('div.tide-day', first=True).text)

Huntington = (pull[1].html.find('div.column', first=True).find('div.tide-day', first=True).text)

Providence = (pull[2].html.find('div.column', first=True).find('div.tide-day', first=True).text)

Wrightsville = (pull[3].html.find('div.column', first=True).find('div.tide-day', first=True).text)


#HalfMoonBay = (pull2.html.find('div.tide_flex_start', first=True).find('div.tide-day', first=True).text)

print(HalfMoonBay,'\n''-----------------------------------------------------------------''\n',
      Huntington,'\n''-----------------------------------------------------------''\n', 
      Providence,'\n''-------------------------------------------------------------------''\n',
      Wrightsville)