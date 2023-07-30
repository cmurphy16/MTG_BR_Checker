# MTG B&R Checker


### Requirements

- Python 3.10+

This script makes use of a Match-Case statment which was introduced in Python 3.10.

- PyClip

`pip install pyclip`

This is used to copy the B&R link to your clipboard automatically so you can paste it where needed quicker and easier.

## What does this even do?
When Wizards of the Coast create a Banned & Restricted Announcement you'll be greeted with "You are not authorized the view this page." when you go to the link, because it hasn't been released yet.

That page has a response code of 403 Forbidden; and since every B&R is on a Monday, and the links are basically the same with a different date in them we can automatically create a link and check future Monday links for a 403 response code. If there is one we know there's a B&R planned that Monday.


## Contents
This project consists of two scripts
 - BRChecker.py

BRChecker will check the B&R links for the two upcoming Mondays.

 - BRWaiter.py

BRWaiter is used to check a known B&R link on the morning of and will check once a second until the B&R is released.

