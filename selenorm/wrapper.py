from selenium import webdriver

#need folder with all drivers
#need to access that folder 
#then call this class

class Browser:
    chrome = 1
    def __init__(self):
        pass
    def set_driver(self,driver_id):
        if driver_id == 1:
            driver = webdriver.Chrome()

        else:
            raise "Couldn't find that browser"
        
