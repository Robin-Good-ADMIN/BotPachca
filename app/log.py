import time
import datetime
from colorama import *
#region Private param
_failName = "" #Имя файла 
_attempts = 5 # Количество попыток
_timeError = 1 #Время между попытками (в секундах)

_clearLog = False # Нужно ли чистить лог после использования
_isTime = True # писать ли время

_current_datetime = ''#Внутренне время
#endregion


class Log:
    def __init__(self, failName=None, attempts=None, timeError=None, clearLog = None,isTime = None):
        """Зарегистрируйте лог"""
        
        # используем переданные попытки или по умолчанию
        self._failName = failName if failName is not None else _failName
        self._attempts = attempts if attempts is not None else _attempts
        self._timeError = timeError if timeError is not None else _timeError
        self._clearLog = clearLog if clearLog is not None else _clearLog
        self._isTime = isTime if isTime is not None else _isTime

        if self._clearLog == True: 
            with open(self._failName + '.Log', 'w'): pass
        # Получаем текущую дату и время, если это нужно
        if self._isTime:
            self._current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    def log(self, text=None, log_type="INFO"):
        try:
            current_time = self._current_datetime if self._isTime else ''
        
            with open(self._failName + ".log", 'a', encoding='utf-8') as file:
                if current_time:
                    file.write(f'{current_time} {log_type}:{text}\n')
                else:
                    file.write(f'{log_type}:{text}\n')
                    

        except Exception as e:
            if self._attempts > 0:
                print(Fore.RED + Style.BRIGHT + f"[ ERROR ] Ошибка в логе иду на перезапуск. ({e}) time:{self._current_datetime}.{Fore.YELLOW} Попытка %{self._attempts} " + Style.RESET_ALL)
                self._attempts = self._attempts - 1
                self.log(text,log_type)
                time.sleep(self._timeError)
            else:
                print("================================================================")
                print(Fore.RED + Style.BRIGHT + f"[ Fatal ERROR ] Ошибка в логе. ({e}) time:{self._current_datetime}.{Fore.YELLOW} Попытка %{self._attempts} " + Style.RESET_ALL)
                print("================================================================")
                print(Fore.CYAN + "Остановка лога фатальная ошибка" + Style.RESET_ALL)


