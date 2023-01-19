# Progress bar
## How does it work?

Argument 1 receive a string and represent the bar before load, argument 2 receive a string and represent the bar onload, argument 3 receive a integer which is the length of the the bar and Argument 4 receives an integer and this is the maximum refresh time between the argument and 0 in seconds, 
the default value of this is 0.5 seconds.


```python
from progress_bar import *

BAR = "."
FILLED = "#"
BAR_LENGHT = 30
REFRESH_TIME = 1 #seconds

progressBar(BAR, FILLED, BAR_LENGHT, REFRESH_TIME)
```
### output
```
current progress: [##############################...] 90.0%
Fineshed!
```

## Author
Github -  [@migueweb](https://github.com/migueweb)