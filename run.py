from mrblitit import mrbilit
import time
from sqlfile import sql
with mrbilit(False,"ilnhk","hwtihk",30) as bot:
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
    for i in range(bot.checkAvailable()):
        sql.add(bot.extract()[2][i],bot.extract()[3][i],bot.extract()[4][i])
    
