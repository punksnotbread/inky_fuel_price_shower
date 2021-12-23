This is a simple script to show fuel prices
scraped & parsed from pricer and display them on the Pimoroni InkyPhat.

Usable simply via crontab:
```
0 6 * * * cd /home/pi/fuel_prices/ && ./main.py
```

TODO:
* Multiple fuel types
* Display graph for changing prices
* Scraping nearest/relevant locations?