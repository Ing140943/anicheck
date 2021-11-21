*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${expect}  ROBOT FRAME WORK/
${url}  https://anicheck-isp.herokuapp.com/
${Browser}  chrome
*** Keywords ***

*** Test Cases ***
1. Open the anichek in google chrome browser
   Open Browser  ${url}  ${Browser}
   Maximize Browser Window
   Set Selenium Speed   0.3
2. Input the Naruto to the search tab
   Input Text  name=keyword  Naruto
3. Search for the result
   Click Button  xpath://input[@type='submit']
4. Click to the first link which is Naruto Title
   Click link  link:Naruto
