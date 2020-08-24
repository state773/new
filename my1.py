import telebot

bot = telebot.TeleBot('1397379259:AAHAySIECvo6kXDY7FC90vbNXQ6U9HIVcQ4')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBJl9BRka-FxE7B6fgRW1MgcesGCuFAAKkGgACxmsIUlA6N-NeyjRnGwQ')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if 'керамбит лучший' in message.text.lower():
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAM9X0D-8g1U6SrnlpsuzYPILuYWap8AAmQAA-vBSCI9FLoYlMphRBsE')
    if 'люблю керамбита' in message.text.lower():
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAM9X0D-8g1U6SrnlpsuzYPILuYWap8AAmQAA-vBSCI9FLoYlMphRBsE')
    if 'керамбит я тебя люблю' in message.text.lower():
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAM9X0D-8g1U6SrnlpsuzYPILuYWap8AAmQAA-vBSCI9FLoYlMphRBsE')
    if 'керамбит прекрасен' in message.text.lower():
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBtV9BlCk4q3OsU3VdrZSR7M8L1JPeAAJRAAPrwUgilx6LeWxOtuIbBA')
    if 'привет керамбит' in message.text.lower():
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBI19BRbv_hdX0sgKX61QO8Bo658J1AALnGgACxmsIUmXP-jyYDXT4GwQ')
    if 'добрый вечер' in message.text.lower():
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBJl9BRka-FxE7B6fgRW1MgcesGCuFAAKkGgACxmsIUlA6N-NeyjRnGwQ')
    if 'керамбит спой' in message.text.lower():
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBMF9BR-_4qLuZZ1xsBaf-gjfG7GEZAALTGgACxmsIUnkgRIAod1s5GwQ')
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBMV9BSK6BLd0mW5Jz4No34kxhow15AALUHAACxmsIUgebJO4nDxenGwQ')

    if 'ебля' in message.text.lower():
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBSV9Baw7tga3C-2msnksjKh-7uJo7AAKIJwACxmsIUuEX_BXEXqAqGwQ')
    if 'секс' in message.text.lower():
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBSV9Baw7tga3C-2msnksjKh-7uJo7AAKIJwACxmsIUuEX_BXEXqAqGwQ')
    if 'ебаться' in message.text.lower():
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBSV9Baw7tga3C-2msnksjKh-7uJo7AAKIJwACxmsIUuEX_BXEXqAqGwQ')
    if 'трахаться' in message.text.lower():
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBSV9Baw7tga3C-2msnksjKh-7uJo7AAKIJwACxmsIUuEX_BXEXqAqGwQ')
    if 'хуй' in message.text.lower():
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBWF9Ba_aY4J5d0ttRIbYMES-5c3nOAALQJwACxmsIUsmkSIbwVYGlGwQ')
    if 'пизда' in message.text.lower():
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBWF9Ba_aY4J5d0ttRIbYMES-5c3nOAALQJwACxmsIUsmkSIbwVYGlGwQ')
    if 'говно' in message.text.lower():
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBWF9Ba_aY4J5d0ttRIbYMES-5c3nOAALQJwACxmsIUsmkSIbwVYGlGwQ')
    if 'моча' in message.text.lower():
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBWF9Ba_aY4J5d0ttRIbYMES-5c3nOAALQJwACxmsIUsmkSIbwVYGlGwQ')
    words = ['керамбоськ']
    if any(word in message.text.lower() for word in words):
        bot.send_message(message.chat.id, '>керамбоська')
        bot.send_video(message.chat.id, "BAACAgIAAxkBAANyX0ETHhQWYyMY0Agnat6CAxElym0AApAHAAKRJglKCWHl_GYVGYIbBA")
    words = ['ужасно']
    if any(word in message.text.lower() for word in words):
        bot.send_video(message.chat.id, "BAACAgIAAxkBAANWX0EM4pPwlrOXE9zhOL3sYZcn--QAAooHAAKRJglKc91hxfWd5uYbBA")
    words = ['оксимирон']
    if any(word in message.text.lower() for word in words):
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBh19BgaOe7uXFIgK4Y62zzvZPrmtGAAKbLQACxmsIUs3ffPUWb6b6GwQ')
    words = ['аха']
    if any(word in message.text.lower() for word in words):
        bot.send_video(message.chat.id, 'BAACAgIAAxkBAAIBmV9BjFFo2oYoLesZu5r9nFl2K5WsAAJDCAACkSYJSgSpcF91YDCzGwQ')


@bot.message_handler(content_types=['sticker'])
def handling_sticker(message):
    sticker_id = 'drxn3y0LicbBA'
    current_sticker_id = message.sticker.file_id.split('-')[-1]
    if current_sticker_id == sticker_id:
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIDQl9C6ySA-9Vmyl4RmAPfUwbt5ODjAAJYKAACxmsIUhjGWZGD1OABGwQ')
    sticker_id = 'ccInofledbAfAbBA'
    current_sticker_id = message.sticker.file_id.split('-')[-1]
    if current_sticker_id == sticker_id:
        bot.send_voice(message.chat.id, 'AwACAgQAAxkBAAIBh19BgaOe7uXFIgK4Y62zzvZPrmtGAAKbLQACxmsIUs3ffPUWb6b6GwQ')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


@bot.message_handler(content_types=['video'])
def sticker_id(message):
    print(message)


@bot.message_handler(content_types=['voice'])
def sticker_id(message):
    print(message)


if __name__ == '__main__':
    bot.polling(none_stop=True)
