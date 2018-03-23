import schedule
import functionsFile
import time
def run_schedule():
    schedule.every(180).seconds.do(functionsFile.deactShopJob)
    while True:
        schedule.run_pending()
        time.sleep(150)
run_schedule()
