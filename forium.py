# script.py
from telethon.sync import TelegramClient, events
import time

api_id = '26272268'
api_hash = '0cddc3341e2f747985b780938cff8f9f'
phone_number = '+4915155861179'

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()
    print("Бот успешно запущен!")

    me = await client.get_me()
    print(f'Авторизован как {me.username}')

    @client.on(events.NewMessage(pattern=r'(?i)%Config'))
    async def handle_config(event):
        await event.edit('-successfuly!')

    # Ожидание завершения программы вручную (не завершится, пока не будет принудительно остановлено)
    await client.run_until_disconnected()

if __name__ == "__main__":
    # Запуск основной функции в цикле
    while True:
        try:
            client.loop.run_until_complete(main())
        except Exception as e:
            print(f"Ошибка: {e}")
            # В случае ошибки ждем некоторое время перед повторным запуском
            time.sleep(60)