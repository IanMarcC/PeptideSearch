from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


num_tabs = 0
criteria = ["Homo sapiens (taxid:9606)", "Sus scrofa (taxid:9823)", "Mus musculus (taxid:10090)"]
data_file = open("peptides2.txt")
results_file = open("peptide_results.txt", 'w')
driver = webdriver.Chrome('C:\Python36\side_projects\chromedriver.exe')
'''
#for line in data_file:
driver.get("https://l.facebook.com/l.php?u=https%3A%2F%2Fblast.ncbi.nlm.nih.gov%2FBlast.cgi%3FPAGE%3DProteins%26fbclid%3DIwAR15CLmriyo6rTtdH5WLfBEKcQpL82gvCf-JLI79O0iX4g-mSuDRCujCCiw&h=AT01n6FeKK-OF-jnpVbiLGRmw1YrkNtD7NAIS6V_xmKaTnGfHB2vu0SVSlS5L-EkhQgIGTNjDPiJpXBBHejlKY40zSwBhkHz-YtsqRHDh_YASKIKaQDjwEPsLBskyB--3MDLtQ")
#assert "Google" in driver.title
elem = driver.find_element_by_name("QUERY")
elem.send_keys('ChromeDriver')
    elem.submit()
    driver.quit()
elem.clear()
elem.send_keys("shrekshrekshrek")
elem = driver.find_element_by_id("b1")
elem.send_keys(Keys.RETURN)
'''
test_line = data_file.readline()
for line in data_file:
    start = time.time()
    driver.get("https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins&fbclid=IwAR15CLmriyo6rTtdH5WLfBEKcQpL82gvCf-JLI79O0iX4g-mSuDRCujCCiw")
    elem = driver.find_element_by_xpath('//*[@id="addOrgIm"]')
    hov = ActionChains(driver).move_to_element(elem)
    hov.double_click()
    hov.perform()
    
    elem = driver.find_element_by_name("EQ_MENU")
    
    for x in range(0, len(criteria)):
        if x == 0:
            pass
        else:
            print('hi3')
            elem = driver.find_element_by_name("EQ_MENU"+str(x))
            
        elem.send_keys(criteria[x])
        elem = driver.find_element_by_xpath('//*[@id="addOrgIm"]')
        hov = ActionChains(driver).move_to_element(elem)
        hov.double_click()
        hov.perform()
        
    elem = driver.find_element_by_name("QUERY")
    elem.clear()
    elem.send_keys(line.strip())
    elem = driver.find_element_by_id("b1")
    elem.send_keys(Keys.RETURN)
    end = time.time()
    
    while end - start < 150:
        end = time.time()
        pass
    
    results_file.write(line+'\n')
    elem2 = driver.find_element_by_xpath('//*[@id="showGraphic"]/span[2]')
    hov2 = ActionChains(driver).move_to_element(elem2)
    hov2.double_click()
    hov2.perform()
    print('hi4')
    driver.execute_script("window.scrollTo(0,600)")
    time.sleep(20)
    driver.save_screenshot(line.strip()+'.png')
    

data_file.close()
results_file.close()
    
    
    

