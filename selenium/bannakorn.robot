*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${expect}  ROBOT FRAME WORK/
${url}  https://anicheck-isp.herokuapp.com/
${Browser}  chrome
*** Keywords ***

*** Test Cases ***
1. เปิดเว็บไซต์ google
   Open Browser  ${url}  ${Browser}
   Maximize Browser Window
   Set Selenium Speed   0.3

2. คลิ๊กไปที่ Robot Framework
   Click link  link:Please Login

3. กรอกคำว่า Robot Framework
   Input Text  name=username  admin
   Input Text  name=password  admin!12345
4. submit
   Click Button  xpath://button[@type='submit']