*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${expect}  ROBOT FRAME WORK/
${url}  https://anicheck-isp.herokuapp.com/reviews
${Browser}  safari
*** Keywords ***

*** Test Cases ***
1. open anicheck websites
   Open Browser  ${url}  ${Browser}
   Set Selenium Speed   0.3


2. Input some source
    Input Text   name=keyword   Amagami
3. Press enter for searching
    Press Keys   None   RETURN

4. Direct to home
    Click Link    link:Home

5. Close remote browser
    Close Browser

