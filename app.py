from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime

# Bot was created for purely testing purpose.
# It aims to increase the lvl by automatic betting
# Using the script at your own risk.


class RustBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
        self.value_bet = "0.01"
        self.color = "red"  # red / blue / gold
        self.title_number = 984050  # change numer current color
        self.account = 50  # 10 == 0.10
        self.counter_circle = 200  # maximum number of bets

    def login(self):
        bot = self.bot
        bot.get("https://rustchance.com")
        time.sleep(2)
        bot.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/a').click()
        button_login = bot.find_element_by_id("imageLogin")
        if not bot.find_element_by_id("steamAccountName"):
            button_login.click()
            time.sleep(1)
            bot.get("https://rustchance.com/roulette")
        else:
            username = bot.find_element_by_id("steamAccountName")
            password = bot.find_element_by_id("steamPassword")
            username.clear()
            password.clear()
            username.send_keys(self.username)
            password.send_keys(self.password)
            button_login.click()
            time.sleep(1)

            if bot.find_element_by_id("twofactorcode_entry"):
                twofactor = bot.find_element_by_id("twofactorcode_entry")
                code = input("Enter the steam verification code: ").upper()
                twofactor.send_keys(code)
                twofactor.send_keys(Keys.RETURN)
                time.sleep(10)
                bot.find_element_by_xpath(
                    '//*[@id="app"]/div/div[4]/div/div[4]/a'
                ).click()
                time.sleep(3)

    def auto_bet(self):
        bot = self.bot
        account_value = bot.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div'
        ).text
        title_number = self.title_number
        if account_value != "0.00":
            bet = True
        else:
            bet = False

        title_number = self.title_number
        while bet == True:
            timer_bet = bot.find_element_by_xpath(
                '//*[@id="app"]/div/div[5]/div/div/div[2]/div[1]/div[1]/div/div[2]'
            ).text
            if timer_bet != "0.00":
                try:
                    if bot.find_element_by_xpath("//*[@title='%s']" % title_number):
                        input_bet = bot.find_element_by_class_name(
                            "Roulette__bett_input-field"
                        )
                        input_bet.clear()
                        input_bet.send_keys(self.value_bet)

                        if self.color == "red":
                            bot.find_element_by_xpath(
                                '//*[@id="app"]/div/div[5]/div/div/div[2]/div[3]/div[2]/div[3]/button'
                            ).click()
                        if self.color == "blue":
                            bot.find_element_by_xpath(
                                '//*[@id="app"]/div/div[5]/div/div/div[2]/div[3]/div[2]/div[1]/button'
                            ).click()
                        if self.color == "gold":
                            bot.find_element_by_xpath(
                                '//*[@id="app"]/div/div[5]/div/div/div[2]/div[3]/div[2]/div[2]/button'
                            ).click()
                        else:
                            print("Error: Wrong color!")
                            bet == False
                        title_number += 1
                except:
                    pass
            else:
                pass
            time.sleep(4)

    def roulette_counter(self):
        bot = self.bot
        bot.get("https://rustchance.com/roulette")
        time.sleep(1)
        title_number = self.title_number
        account = self.account
        color = self.color
        amount_bet = 1
        counter = 0
        red_counter = 0
        blue_counter = 0
        gold_counter = 0
        start_bot = datetime.datetime.now()

        while (counter < self.counter_circle) and (account >= 0):
            try:
                if bot.find_element_by_xpath(
                    "//*[@title='%s'][@src='/static/media/roulette_red.f539c611.png']"
                    % title_number
                ):
                    red_counter += 1
                    account -= amount_bet
                    if color == "red":
                        account += amount_bet * 2
            except:
                try:
                    if bot.find_element_by_xpath(
                        "//*[@title='%s'][@src='/static/media/roulette_blue.4ce873b0.png']"
                        % title_number
                    ):
                        blue_counter += 1
                        account -= amount_bet
                        if color == "blue":
                            account += amount_bet * 2
                except:
                    try:
                        if bot.find_element_by_xpath(
                            "//*[@title='%s'][@src='/static/media/roulette_gold.55fd1e82.png']"
                            % title_number
                        ):
                            gold_counter += 1
                            account -= amount_bet
                            if color == "gold":
                                account += amount_bet * 14
                    except:
                        pass

            counter += 1
            print("counter", counter)
            print("title_number", title_number)
            print("red_counter", red_counter)
            print("blue_counter", blue_counter)
            print("gold_counter", gold_counter)
            print("account", account)
            print("-------------------")
            title_number += 1
            time.sleep(25)

        stop_bot = datetime.datetime.now()
        print("start", start_bot)
        print("stop", stop_bot)

    def exit(self):
        bot = self.bot
        bot.close()


option = input("1) Bet  2) Counter:  ")
if option == "1" or "":
    ed = RustBot("Your Steam Username", "Your Steam Password")
    ed.login()
    ed.auto_bet()
    ed.exit()
elif option == "2":
    ed = RustBot("Your Steam Username", "Your Steam Password")
    ed.roulette_counter()
    ed.exit()

