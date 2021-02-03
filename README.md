# BotTelegram
Telegramm bot dla pracy ta modyfikacji grup.

Napisany za pomocą bibliotek:
  aiogram==2.11.2
  aiohttp>=3.6.2
  python-dotenv
  
 Ma taki funkcji jak :
        '/set_photo - Set the photo in the chat',
        '/set_title - Set the chat name',
        '/set_description - Set the description of the chat',
        '/ro - Enable Read Only mode',
        '/unro - Disable Read Only mode',
        '/ban - Ban user',
        '/unban - Unban user',
        '/help - Command list',
        '/riddles - Answer our riddles',
        '/products - products',
        '/gallery - This is a gallery',
        '/show_on_map - Place for eating',
        '/callback - We will call you'
        
Instaliacja / test:
 Pobrać bota,
 zainstlować requirements,
 zmienić BotToken w pliku .env BOT_TOKEN= /*your bot token from Bot Father*/,
 w pliku data/config.py zmienic 
 admins = [
    /*your telegram id witch can be getted
   @ShowJsonBot here*/,
]
 https://web.telegram.org/#/im?p=@ShowJsonBot tu możesz wyszukać swój id.  
 Uruchomić plik app.
 Dodać do grupy.
 Bot jest gotowy do wykorzystania.
 
 Linki :
 https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-telegram?view=azure-bot-service-4.0
 https://web.telegram.org/#/im?p=@BotFather
 
 
 
