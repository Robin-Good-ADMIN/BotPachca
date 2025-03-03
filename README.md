# 🚀 Pachca Bot
[![Telegram Community](https://img.shields.io/badge/Telegram-Join%20Channel-blue?logo=telegram)](https://t.me/robgud)
[![YouTube Tutorials](https://img.shields.io/badge/YouTube-Subscribe-red?logo=youtube)](https://www.youtube.com/@Robin_Good_Admin)

Python-обертка для работы с API мессенджера Pachca. Поддержка сообщений, кнопок и истории чатов.


## 📦 Установка зависимостий
```python
# Установите зависимости
pip install requests # Для Web запросов
# Зависимости для лога
pip install colorama #Для Красивого отображения лога


```
## 🛠️ Использование

```python
from web_request import Web_Request

bot = Web_Request(
    tocen_API="ВАШ_API_ТОКЕН", 
    content_Type="application/json; charset=utf-8" # Не безательно
)
```
## 📨 Отправка сообщения
```python
bot.send_message(
    id_group=123456789, 
    message="Привет, это тестовое сообщение!"
)
```

## 🔘 Сообщение с кнопками
```python
buttons = [
    '{"text": "✅ Подтвердить", "data": "confirm"}',
    '{"text": "🚫 Отмена", "data": "cancel"}',
    '{"text": "⏱️ Отложить", "data": "delay"}'
]

bot.send_button(
    id_group=123456789,
    message="Выберите действие:",
    buttons=buttons
)
```
## 📜 Получение истории чата
```python
history = bot.return_message(
    id_group=123456789,
    num_parameters=50,  # Количество сообщений
    page=1              # Страница
)
print(history)
```

## 💬 Поддержка и обсуждение
Присоединяйтесь к нашим сообществам для любых вопросов:


[Telegram Chat](https://t.me/ChatRobinGood)

Что можно обсудить:

+ **🐞 Сообщения об ошибках**

+ **💡 Идеи для улучшения**

+ **🛠️ Помощь в реализации**

+ **🤝 Совместные проекты**