*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${expect}  ROBOT FRAME WORK/
${url}  https://www.google.co.th/
${Browser}  chrome
*** Keywords ***

*** Test Cases ***
1. เปิดเว็บไซต์ google
   Open Browser  ${url}  ${Browser}
   Maximize Browser Window
   Set Selenium Speed   0.3
2. กรอกคำว่า Robot Framework
   Input Text  name=q  Robot Framework
3. กดค้นหา
   Click Button  name=btnK
4. คลิ๊กไปที่ Robot Framework
   Click Element  //h3[@class="LC20lb"]
5. เช็คหน้าเว็บ
   ${result}  Get Text  //h1[@class="main-header"]
   Log To Console  ${result}
   Should Be Equal  ${result}  ${expect} 

   