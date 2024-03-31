from mrblitit import mrbilit
import time
with mrbilit(False,"jivhk","advhc") as bot:
    bot.choose_type("bus")
    # bot.implicitly_wait(10)
    time.sleep(1)
    bot.choose_origin()
    bot.choose_destination()