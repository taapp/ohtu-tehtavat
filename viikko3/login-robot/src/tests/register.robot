*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  ville  ville123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  vi  ville123
    Output Should Contain  Invalid username or password

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  viille  ville12
    Output Should Contain  Invalid username or password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  ville  villeABCD
    Output Should Contain  Invalid username or password

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  kalle  kalle123
    

