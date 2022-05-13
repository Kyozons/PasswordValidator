#!/usr/bin/python3 python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, sys, time

with open('creds', 'r') as creds:
    data = creds.read()
user = data[:41]
passwd = data[42:]


br = webdriver.Chrome()
br.get('https://gmail.com')

user_box = WebDriverWait(br, 10).until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(user)
# br.find_element(By.NAME, 'identifier').send_keys(user)
br.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d').click()
pwd_box = WebDriverWait(br, 10).until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(passwd)
# br.find_element(By.NAME, 'password').send_keys(passwd)

msg_button = WebDriverWait(br, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'z0'))).click()
# br.find_element(By.CLASS_NAME, 'z0').click()

to = 'ticket@mundotelecomunicaciones.cl'
to_box = WebDriverWait(br, 10).until(EC.visibility_of_element_located((By.NAME, 'to')))
to_box.send_keys(to, Keys.TAB)
# to_box = br.find_element(By.NAME, 'to')
# to_box.click()

subject = 'Test Subject'
subject_box = WebDriverWait(br, 10).until(EC.visibility_of_element_located((By.NAME, 'subjectbox')))
# subject_box = br.find_element(By.ID, ':pw')
message = 'Test Message'
subject_box.send_keys(subject, Keys.TAB, message, Keys.TAB, Keys.ENTER)







