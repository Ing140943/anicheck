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

