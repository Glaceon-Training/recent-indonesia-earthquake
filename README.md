# Recent (The Latter) Indonesia Earthquake
This package will get recent earthquake detected from 
Meteorological, Climatology and Geophysics Agency of Indonesia's website

## How it works
This package will scrape from BMKG Indonesia to get most recent earthquake happening
in Indonesia.

This package uses BeautifulSoup4 and Request to produce output in JSON form and ready
to be used in web application services.

## How to use
```
import recent_earthquake2

if __name__ == '__main__':
    result = recent_earthquake2.data_extraction()
    recent_earthquake2.show_data(result)
```

## Author
rynderi
