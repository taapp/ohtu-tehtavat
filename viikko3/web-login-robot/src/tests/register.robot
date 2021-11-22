*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Info
    Register Should Succeed
    

Register With Too Short Username And Valid Password
    Set Username  vi
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Info
    Register Should Fail With Message  Invalid username or password

Register With Valid Username And Too Short Password
    Set Username  ville
    Set Password  ville12
    Set Password Confirmation  ville12
    Submit Info
    Register Should Fail With Message  Invalid username or password

Register With Nonmatching Password And Password Confirmation
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville1234
    Submit Info
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Set Username  antti
    Set Password  antti123
    Set Password Confirmation  antti123
    Submit Info
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  antti
    Set Password  antti123
    Submit Credentials
    Main Page Should Be Open

Login After Failed Registration
    Set Username  pekka
    Set Password  pekka32
    Set Password Confirmation  pekka32
    Submit Info
    Click Link  Login
    Set Username  pekka
    Set Password  pekka32
    Submit Credentials
    Page Should Contain  Invalid username or password

*** Keywords ***
Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Info
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}

Submit Credentials
    Click Button  Login