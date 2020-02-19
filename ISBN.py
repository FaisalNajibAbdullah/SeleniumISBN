from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import XLUtils
import numpy as np

driver = webdriver.Chrome()
driver.get('https://isbn.perpusnas.go.id/')

username = driver.find_element_by_xpath('//*[@id="Username"]')
username.send_keys('awangga')

password = driver.find_element_by_xpath('//*[@id="Password"]')
password.send_keys('rollyganteng')

login = driver.find_element_by_xpath('//*[@id="btnLogin"]')
login.click()

wait = WebDriverWait(driver,100)
wait.until(EC.element_to_be_clickable((By.ID,'btnMod')))
close = driver.find_element_by_id("btnMod")
close.click()

daftarbuku = driver.find_element_by_xpath('//*[@id="topnavbar"]/div/div[2]/ul/li[2]/a')
daftarbuku.click()



path="C://Users/najib/Desktop/isbn.xlsx"

rows=XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    judul=XLUtils.readData(path,"Sheet1",r,1)
    kepengarangan=XLUtils.readData(path,"Sheet1",r,2)
    edisi=XLUtils.readData(path,"Sheet1",r,3)
    seri=XLUtils.readData(path,"Sheet1",r,4)
    tahun=XLUtils.readData(path,"Sheet1",r,5)
    halaman=XLUtils.readData(path,"Sheet1",r,6)
    tinggi=XLUtils.readData(path,"Sheet1",r,7)
    npm=XLUtils.readData(path,"Sheet1",r,8)

    driver.find_element_by_xpath('//*[@id="Judul"]').send_keys(judul)
    driver.find_element_by_xpath('//*[@id="Kepeng"]').send_keys(kepengarangan)
    driver.find_element_by_xpath('//*[@id="frDaftarIsbn"]/div[3]/div[1]/input').send_keys(edisi)
    driver.find_element_by_xpath('//*[@id="frDaftarIsbn"]/div[3]/div[2]/input').send_keys(seri)
    driver.find_element_by_xpath('//*[@id="frDaftarIsbn"]/div[4]/div/input').send_keys(tahun)
    driver.find_element_by_xpath('//*[@id="frDaftarIsbn"]/div[5]/div/input').send_keys(halaman)
    driver.find_element_by_xpath('//*[@id="frDaftarIsbn"]/div[6]/div/input').send_keys(tinggi)

    kategori = driver.find_element_by_xpath('//*[@id="frDaftarIsbn"]/div[7]/div/div/label[3]/span')
    kategori.click()

    uploadfile = driver.find_element_by_xpath('//*[@id="berkas[0]"]')
    uploadfile.send_keys("D://NAJIB/ISBN/file/"+str(npm)+".pdf")

    #kirim = driver.find_element_by_xpath('//*[@id="daftar"]')
    #kirim.click()

    daftarbuku = driver.find_element_by_xpath('//*[@id="topnavbar"]/div/div[2]/ul/li[2]/a')
    daftarbuku.click()
