from mrblitit import mrbilit
import time
with mrbilit(False,"jivhk","ilnhk",20) as bot:
    bot.choose_type("bus")
    # bot.implicitly_wait(10)
    time.sleep(5)
    bot.implicitly_wait(10)
    bot.choose_origin()
    time.sleep(2)
    bot.implicitly_wait(10)
    bot.choose_destination()
    bot.implicitly_wait(10)
    bot.choose_date()