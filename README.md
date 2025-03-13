# MTG B&R Checker


## Requirements

- Python 3.10+.
  - This script makes use of a Match-Case statment which was introduced in Python 3.10.

- PyClip `pip install pyclip`
  - This is used to copy the B&R link to your clipboard automatically so you can paste it where needed quicker and easier.

- Requests `pip install requests`
  - This is use to pull the web page and specifically the response code

## What does this even do?
Instead of mashing F5 on Monday until the new B&R is released, this will automatically check until it's released and open a new tab to it the moment it goes up.

## Deprecated folder
This project consists of two scripts for the old version of this repo that is no longer maintained as of the Dec 4, 2023 B&R update

 - BRChecker.py

BRChecker will check the upcoming Monday(s) for a B&R. **UPDATE** After the past two B&Rs (Aug 7, and Oct 16, 2023) never going 403 early, this script may become deprecated if it's no longer able to provide a use.

 - BRWaiter.py

BRWaiter is used to check a B&R link on the morning of and will check every second until the B&R is released. When the B&R is released a new tab will be opened in your browser and the link copied to your clipboard.

 - BRFuncs.py

BRFuncs contains functions used by both of the main scripts
