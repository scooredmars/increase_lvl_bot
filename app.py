from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, datetime

# python app.py pipenv shell


class RustBot:
    def __init__(self, username, password):
        # for auto_bet and roulette_counter
        self.value_bet = "0.01"
        self.color = "blue"  # red / blue / gold
        # only for roulette_counter
        self.account = 50  # 10 == 0.10
        self.amount_bet = 1  # only int values
        self.counter_circle = 5
        # don't change !
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
        self.xp = 0
        self.counter = 0
        self.red_counter = 0
        self.blue_counter = 0
        self.gold_counter = 0

    def mute_sound(self):
        bot = self.bot
        bot.find_element_by_xpath(
            '//*[@id="app"]/div/div[5]/div/div/div[1]/div/div/div'
        ).click()

    def login(self):
        bot = self.bot
        bot.get("https://rustchance.com")
        time.sleep(2)
        bot.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/a').click()
        button_login = bot.find_element_by_id("imageLogin")

        if bot.find_element_by_id("steamAccountName"):
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
                code = input("Podaj kod weryfikacyjny: ").upper()
                twofactor.send_keys(code)
                twofactor.send_keys(Keys.RETURN)
                time.sleep(10)
                bot.find_element_by_xpath(
                    '//*[@id="app"]/div/div[4]/div/div[4]/a'
                ).click()
                time.sleep(3)
        else:
            button_login.click()
            time.sleep(1)
            bot.get("https://rustchance.com/roulette")
            time.sleep(5)

        data.mute_sound()

    def supply_event(self):
        bot = self.bot
        while True:
            try:
                if bot.find_element_by_class_name("supplydrops"):
                    join_btn = bot.find_element_by_xpath(
                        '//*[@id="app"]/div/div[2]/div[5]/div[1]/button/span'
                    ).text
                    if join_btn == "JOIN":
                        bot.find_element_by_xpath(
                            '//*[@id="app"]/div/div[2]/div[5]/div[1]/button'
                        ).click()
                    elif join_btn == "Joined":
                        time.sleep(60 * 2)
                    print(error_msg)

                    error_msg = bot.find_element_by_class_name("pt-toast-message").text
            except:
                pass
            time.sleep(4)

    def auto_bet(self):
        bot = self.bot
        bet = True
        title_number = int(
            bot.find_element_by_xpath(
                '//*[@id="app"]/div/div[5]/div/div/div[2]/div[2]/div[2]/div[2]/img[1]'
            ).get_attribute("title")
        )
        while bet == True:
            account_value = bot.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div[3]/div/div'
            ).text
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

                        if bot.find_element_by_class_name("supplydrops"):
                            join_btn = bot.find_element_by_xpath(
                                '//*[@id="app"]/div/div[2]/div[5]/div[1]/button/span'
                            ).text
                            if join_btn == "JOIN":
                                ot.find_element_by_xpath(
                                    '//*[@id="app"]/div/div[2]/div[5]/div[1]/button'
                                ).click()

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
                        title_number += 1
                        self.xp += 1
                except:
                    pass
            time.sleep(4)
            if account_value == "0.00":
                print("Gained Xp: ", self.xp)

    def roulette_counter(self):
        bot = self.bot
        bot.get("https://rustchance.com/roulette")
        time.sleep(1)
        account = self.account
        color = self.color
        amount_bet = self.amount_bet
        counter = self.counter
        red_counter = self.red_counter
        blue_counter = self.blue_counter
        gold_counter = self.gold_counter
        start_bot = datetime.datetime.now()

        data.mute_sound()

        while (counter < self.counter_circle) and (account >= 0):
            try:
                title_number = int(
                    bot.find_element_by_xpath(
                        '//*[@id="app"]/div/div[5]/div/div/div[2]/div[2]/div[2]/div[2]/img[1]'
                    ).get_attribute("title")
                )
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
            print("-------------------")
            time.sleep(25)

        stop_bot = datetime.datetime.now()
        print("Start", start_bot)
        print("Stop", stop_bot)
        print("red_counter", red_counter)
        print("blue_counter", blue_counter)
        print("gold_counter", gold_counter)
        print("account", account)
        print("-------------------")

    def exit(self):
        bot = self.bot
        bot.close()


steam_name = input("Enter steam username: ")
steam_password = input("Enter steam password: ")
option = input("1) bet & supply  2) counter  3) supply event:  ")
data = RustBot(steam_name, steam_password)
if option == "1":
    data.login()
    data.auto_bet()
    data.exit()
elif option == "2":
    data.roulette_counter()
    data.exit()
elif option == "3":
    data.login()
    data.supply_event()
    data.exit()
