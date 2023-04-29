
import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(title="**Please Drink Water Now!!",
                            message="Health should be your first priority!!Health experts commonly recommend eight 8-ounce glasses, which equals about 2 liters, or half a gallon a day",
                            app_icon=None,
                            timeout=10)
        time.sleep(180)


