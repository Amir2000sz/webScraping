from mrblitit import mrbilit
import time
with mrbilit(False,"ilnhk","jivhk",27) as bot:
    bot.implicitly_wait(10)
    bot.choose_type("bus")
    # bot.implicitly_wait(10)
    time.sleep(2.5)
    bot.implicitly_wait(10)
    bot.choose_origin()
    time.sleep(1)
    bot.implicitly_wait(10)
    bot.choose_destination()
    bot.implicitly_wait(10)
    bot.choose_date()
    bot.search()
    bot.checkAvailable()