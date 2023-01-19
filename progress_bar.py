import time, random

def progressBar(bar, filled, lenght, refreshTime = 0.5):

    bar = bar * lenght 

    # to calculate the progress of the bar
    counter = 1

    for character in bar:
        
        # progress of the bar
        percent = round((counter / lenght) * 100, 1)

        # Refreshing the bar
        bar = bar.replace(character, f"{filled}", 1)

        # overwrite the previous line to give the animated effect
        print(f"current progress: [{bar}] {percent}%", end="\r")
        
        counter = counter + 1
        
        time.sleep(random.uniform(0, refreshTime))
    
    print("\nFineshed!")
