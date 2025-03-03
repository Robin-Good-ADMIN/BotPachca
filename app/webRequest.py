import log as lg
import json
import requests

# region Private params
_tocen_API = ''
_content_Type = 'application/json; charset=utf-8'
# endregion


class Web_Request:
    lG = lg.Log("MaqinLog", 5, 1, True)
    _headers = {}
    lG.log('Start Class Web_Request ...', 'Message')

    def __init__(self, tocen_API: str, content_Type: str = 'application/json; charset=utf-8'):
        '''Укажите данные при создании класса\n
        tocen_API - токен API
        '''
        try:
            self._tocen_API = tocen_API
            self._content_Type = content_Type

            self._headers["Authorization"] = str('Bearer ' + tocen_API)
            self._headers["Content-Type"] = str(content_Type)
            self.lG.log(f'Class created successfully')

        except Exception as e:
            self.lG.log(f'Ошибка при создании класса __init__ ==> [{e}]', 'FatalError')
            print(e)

    def send_message(self, id_group: int, message="Hello World"):
        '''
        Отправляет сообщение в группу в кодировке utf-8
        id_group - ID группы
        message - Текст сообщения
        '''
        try:
            data = {
                "message": {
                    "entity_id": int(id_group),
                    "content": message,
                }}
            response = requests.post('https://api.pachca.com/api/shared/v1/messages', headers=self._headers, json=data)
            self.lG.log(f'Сообщение создано и отправлено успешно', 'GoodProcess')

        except Exception as e:
            self.lG.log(f'Ошибка при отправке сообщения ==> [{e}]', 'FatalError')
            print(e)

    def send_button(self, id_group: int, message: str = '', buttons: list = None):
        """
        Создание сообщения с кнопками\n
        id_group - ID группы\n
        message - Текст сообщения\n
        buttons - Массив кнопок, например:\n
        buttons = [\n
            '{"text": "👍 Согласиться", "data": "vote_yes"}',\n
            '{"text": "❌ Отказаться", "data": "vote_no"}',\n
            '{"text": "🕒 Перенести на неделю", "data": "pause_week"}'\n
        ]
        """
        try:
            data = {
                "message": {
                    "entity_id": int(id_group),
                    "content": message,
                    "buttons": []
                }
            }
            
            # Преобразование и группировка кнопок
            formatted_buttons = []
            for i in range(0, len(buttons), 2):
                row = [
                    json.loads(btn.strip().rstrip(','))
                    for btn in buttons[i:i+2]
                ]
                formatted_buttons.append(row)
            
            data["message"]["buttons"] = formatted_buttons
            
            response = requests.post('https://api.pachca.com/api/shared/v1/messages', headers=self._headers, json=data)
            self.lG.log(f'Кнопки созданы и отправлены успешно')

        except Exception as e:
            self.lG.log(f'Ошибка при отправке кнопок ==> [{e}]', 'FatalError')
            print(e)

    def return_message(self, id_group: int, num_parameters: int = 25, page: int = 1):
        '''
        Метод возвращает сообщения из группы\n
        id_group - ID группы\n
        num_parameters - Количество сообщений\n
        page - Номер страницы
        '''
        try:
            data = {
                "chat_id": int(id_group),
                "per": int(num_parameters),
                "page": int(page)
            }
            response = requests.get(
                'https://api.pachca.com/api/shared/v1/messages',
                headers=self._headers,
                params=data
            )
            print((response.content).decode('utf-8'))
            return (response.content).decode('utf-8')

        except Exception as e:
            self.lG.log(f'Ошибка при получении сообщений чата ==> [{e}]', 'FatalError')
            print(e)


buttons = [
    '{"text": "👍 Согласиться", "data": "vote_yes"}',
    '{"text": "❌ Отказаться", "data": "vote_no"}',
    '{"text": "🕒 Перенести на неделю", "data": "pause_week"}'
]


if __name__ == "__main__":
    print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
████ ▄▄▀█▀▄▄▀█ ▄▄▀██▄██ ▄▄▀████ ▄▄ █▀▄▄▀█▀▄▄▀█ ▄▀███ ▄▄▀█ ▄▀█ ▄▀▄ ██▄██ ▄▄▀████
████ ▀▀▄█ ██ █ ▄▄▀██ ▄█ ██ ████ █▀▀█ ██ █ ██ █ █ ███ ▀▀ █ █ █ █▄█ ██ ▄█ ██ ████
████ ██ ██▄▄██▄▄▄▄█▄▄▄█▄██▄████ ▀▀▄██▄▄███▄▄██▄▄████ ██ █▄▄██▄███▄█▄▄▄█▄██▄████
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀""")

    buttons = [
        '{"text": "👍 Согласиться", "data": "vote_yes"}',
        '{"text": "❌ Отказаться", "data": "vote_no"}',
        '{"text": "🕒 Перенести на неделю", "data": "pause_week"}'
    ]

    bot = Web_Request("MyToken")  # Создание экземпляра класса
    bot.send_message("GrupId", "Hello World")  # Отправка сообщения
    bot.send_button("GrupId", "Message Text", buttons)  # Отправка сообщения с кнопками
    bot.return_message("GrupId")  # Получение данных из чата