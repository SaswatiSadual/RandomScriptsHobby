## Get the link to The Hindu epaper:
## Format: https://epaper.thehindu.com/pdf/Year/Month/Date/YearMonthDateEditionTypeofpaper.zip
## Edition of the epapers:
## Delhi : 03, Mumbai: 12, Bengaluru: 04
## Type of paper: Regular = A

##### wget Python 3 package supports downloads:
import wget

import datetime

## Get today's date and time. You will require the year, month and the date.
now = datetime.datetime.now() 

## Convert it into string to make concatenation easy
nowYear = str(now.year)

## If a number is less than 10, then the number will have 0 before it. For example: '8' will become '08'
nowMonth = '{:02d}'.format(now.month)
nowMonth = str(nowMonth)

nowDate = '{:02d}'.format(now.day)

YearMonthDateEditionType = nowYear+nowMonth+nowDate+'3'+'A'

url_of_epaper = "https://epaper.thehindu.com/pdf/"+nowYear+"/"+nowMonth+"/"+nowDate+"/"+YearMonthDateEditionType+'.zip'

## Download the ePaper:
wget.download(url_of_epaper)


## Note: This code works only because of some bug in The Hindu epaper. This will stop working if it is corrected. 
