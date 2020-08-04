# Increase your account level on rustchance.com
The bot was written for purely testing purposes, it is not recommended to use it on the website mentioned above. You use the script at your own risk !


## Configuration
Script uses firefox for everything to work properly you must have it installed.

Before starting the script you need to set the current or future title_number.
Where to find the title_number?
  - Go to the roulette tab
  - Right-click on the first icon next to "Previous rolls" and click inspect
  - You will see the code fragment in which the number in title will be given, e.g. title = "984103"
  - Copy and paste this number into self.title_number, it's best to add +10 to this number, e.g. your number is 984103 and you enter 984113, because before the bot starts it may start a few bets which may cause an error
  
  - If you want to use auto_bet you need to enter your steam details at the bottom of the code in "ed = RustBot (" Your Steam Username "," Your Steam Password ")"

### Auto Bet

Change betting color:
  - Set self.color = "your color" option(red / blue / gold)

Change betting value:
  - Set self.value_bet = "your value"

### Counter

Change  account value:
  - The account is used to check what profit / loss will be after making a certain number of bets
  - Set self.account = "your value"  (10 == 0.10 flames)

Change counter_circle:
  - Its used to determine the amount of bets
  - Set self.counter_circle = "your value"
  
 ## How to start
 - You need selenium installed
 - I recommend using a virtual environment
 - To start, write "python.app"
