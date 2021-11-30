*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${expect}  ROBOT FRAME WORK/
${url}  https://anicheck-isp.herokuapp.com/
${Browser}  chrome
*** Keywords ***

*** Test Cases ***
1. Open google
   Open Browser  ${url}  ${Browser}
   Maximize Browser Window
   Set Selenium Speed   0.3
2. Open login page
   Click link  link:Please Login
3. Enter input text username and password
   Input Text  name=username  admin
   Input Text  name=password  admin!12345
4. Click submit button
   Click Button  xpath://button[@type='submit']