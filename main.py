from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import threading
import time


def convert_duration_to_seconds(duration: str) -> int:
    # Split the input string into minutes and seconds
    minutes, seconds = map(int, duration.split(':'))

    # Calculate total seconds
    total_seconds = minutes * 60 + seconds

    return int(total_seconds)

EMAIL=""
PASSWORD=""
print("hello")
chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_experimental_option(name="detach", value=True)
driver=webdriver.Chrome(options=chromeoptions)
print("cjkdvb")
driver.get("https://open.spotify.com/")
driver.maximize_window()
time.sleep(10)

close=driver.find_element(By.XPATH,'/html/body/div[18]/div[2]/div/div[2]/button')
close.click()
time.sleep(3)
loginbut=driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[3]/header/div[2]/div[3]/div[1]/button[2]')
loginbut.click()
time.sleep(5)
emailinp=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[1]/input')
emailinp.click()
emailinp.send_keys(EMAIL)
passwordinp=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/input')
passwordinp.click()
passwordinp.send_keys(PASSWORD)
time.sleep(5)
loog=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[4]/button')
loog.click()
time.sleep(20)
searchbut=driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[1]/nav/div[1]/ul/li[2]/a')
searchbut.click()
time.sleep(10)
mainserach=driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[3]/header/div[2]/div[2]/div/div/form/input')
mainserach.click()
mainserach.send_keys("gurbani")
time.sleep(10)
mainbox=driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/div[2]/div/div/section[1]/div[2]/div/div/div/div[4]')
mainbox.click()
time.sleep(10)
onoff=driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/section/div[3]/div[2]/div/div/div/button')
onoff.click()
time.sleep(10)


timedurationofthesong=driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/main/section/div[1]/div[3]/div[3]/div/span[3]')
duration=timedurationofthesong.text
mainduration=convert_duration_to_seconds(duration)

print(mainduration,"sbhjvbhsbhjdbhjdcbhjdbchdbchdhhdchvdghcvghvsghghsdvh")
starttime=30
finishtime=50
startfraction=(starttime/mainduration)
finishfraction=(finishtime/mainduration)

time.sleep(10)


timeline=driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[2]/div[2]/div/div')
driver.execute_script("arguments[0].scrollIntoView();", timeline)

time.sleep(10)
location = timeline.location  # Returns a dictionary with 'x' and 'y'
size = timeline.size  # Returns a dictionary with 'width' and 'height'

# Calculate offsets
x_start = location['x']
y_start = location['y']
x_end = x_start + size['width']
y_end = y_start + size['height']
mainwidth=size['width']
mainheight=size['height']
print(mainwidth,"jfcbhfvbhbvuhrfuv")
print(mainheight,"nxdhhdhchuehbcuruvfrur")

# Calculate the click position relative to the element's top-left corner
clickx = int(startfraction * mainwidth)
clicky = 0  # Assuming you want to click at the same vertical level as the element's center

finisherx=int(finishfraction*mainwidth)
finishy=0

# Adjust clickx to ensure it is within the bounds of the element
clickx = min(max(clickx, 0), mainwidth - 1)
print(x_start,"bdshbbhjbhjbdj")
print(x_end,"bdshbbhjbhjbdj")
print(y_start,"bdshbbhjbhjbdj")
print(y_end,"bdshbbhjbhjbdj")
print(clickx,"hbjhbjbjjjbvhjfhjbvjfb")
print(clicky,"nbhjbchjbhjsbbhjsbhjbd")
actions = ActionChains(driver)
actions.move_to_element_with_offset(timeline, clickx - (mainwidth / 2), clicky).click().perform()


def run_loop():
    global stop_loop
    while not stop_loop:
        timer = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[2]/div[1]')
        timertime = timer.text
        if convert_duration_to_seconds(timertime) >= finishtime:
            actions.move_to_element_with_offset(timeline, clickx - (mainwidth / 2), clicky).click().perform()
        time.sleep(1)  # Add a delay to prevent excessive CPU usage



# Variable to control the loop
stop_loop = False

# Start the loop in a separate thread
thread = threading.Thread(target=run_loop)
thread.start()


# Wait for user input to stop the loop
input("Press Enter to stop the loop...\n")
stop_loop = True

# Wait for the thread to finish
thread.join()

# actions.move_to_element_with_offset(timeline, finisherx - (mainwidth / 2), finishy).click().perform()
# time.sleep(5)
# onoff.click()
print("cdsfjvdfjjkvf")
time.sleep(mainduration-starttime)
print("dbjhjhbjhasb")
print("cjkjksjkj")
driver.close()