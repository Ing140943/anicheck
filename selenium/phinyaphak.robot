*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${expect}  ROBOT FRAME WORK/
${url}  https://anicheck-isp.herokuapp.com/
${Browser}  chrome
*** Keywords ***

*** Test Cases ***
# From Banakorn Section because the create review required to login first
1. Open google
   Open Browser  ${url}  ${Browser}
   Maximize Browser Window
   Set Selenium Speed   0.3

2. Open login page
   Click link  link:Please Login

3. Click to the register link
    Click link  link:Create Account

4. Input the username
# Next time you have to change the username to selenium2 and next time ..3,...4,...
    Input Text  name=username  selenium

5. Input the password
    Input Text  name=password1  Abcd!1234
    Input Text  name=password2  Abcd!1234

6. Click regidter button
   Click Button  xpath://button[@type='submit']