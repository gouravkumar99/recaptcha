import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from time import sleep

class fruitlab2:
    def __init__(self):
        obj = uc.ChromeOptions()
        c_op = obj.add_argument('--blink-settings=imagesEnabled=false')
        self.obj = uc.Chrome(c_op)
        self.obj.get("https://fruitlab.com/")
        self.obj.maximize_window()
        try:
            wait(self.obj,10).until(EC.presence_of_element_located((By.CLASS_NAME,'css-n2s0rs'))).click()
        except:
            pass
        self.get_all_links()
        
    def get_all_links(self):
        obj = self.obj
        all_links=[]
        all_swiper_slide = obj.find_element(By.ID,'games__outer_top_id').find_elements(By.CLASS_NAME,"games__outer--image")
        all_swiper_slide2 = obj.find_element(By.ID,'games__outer_id').find_elements(By.CLASS_NAME,"games__outer--image")
        for i in all_swiper_slide:
            all_links.append(i.find_element(By.CLASS_NAME,'videothumbnail').get_attribute('href'))
        for i in all_swiper_slide2:
            all_links.append(i.find_element(By.CLASS_NAME,'videothumbnail').get_attribute('href'))
        print(len(all_links))
        self.open_pages(all_links)
        
    def open_pages(self,all_links):
        obj=self.obj
        for i in all_links:
            obj.get(i)
            sleep(11)
        self.get_all_links()

run = fruitlab2()
