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
2. กรอกคำว่า Robot Framework
   Input Text  name=keyword  Naruto

3. กดค้นหา
   SeleniumLibrary.Click Button 	 locator=webelement 	 modifier=False
