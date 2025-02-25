В данном репозитории находится реализация курсовой работы по теме "Серверная часть приложения для планирования личного бюджета с аналитикой расходов".

Реализация написана на python с использованием фреймворка Django.

Чтобы запустить проект, необходимо перейти в корневую папку проекта (core) и использовать команду python manage.py runserver.

Первая страница, которая видна при запуске сервера – страница входа в систему, откуда можно перейти на страницу админа/регистрации.

Зарегистрировавшись и войдя в аккаунт, вы попадете на страницу с таблицами. Таблицы – основа группировки вводимых финансовых данных. Можно вести таблицы по месяцам, по годам, по десятилетиям – как душе угодно.
Т.к. ничего ещё не было создано, то список будет пустой.

Чтобы создать таблицу нужно нажать соответствующую кнопку и указать название таблицы.

Чтобы перейти в таблицу, необходимо нажать на её название. При необходимости, можно переименовать таблицу или удалить её (удалятся и все связанные с ней данные!!!).

Внутри таблицы первым делом следует добавить сбережения (страница "Сбережения") и категории (страница "Планы").

В сбережениях вы указываете ваши "счета", на которых находятся деньги – вам необходимо указать сумму на счете на момент добавления, система будет динамически высчитывать актуальную сумму в зависимости от введенных данных.

На странице планов вы указываете ожидаемые расходы и ожидаемые доходы. Система будет подсчитывать, на какую сумму набралось транзакций в каждой из категорий. 
Если вы не хотите учитывать категорию при анализе (например, не хотите чтобы в распределении трат учитывались ваши переводы между своими сбережениями), то не отмечаете пункт, связанный с анализом.
В случае с ожидаемыми расходами, система также будет расчитывать и показывать сколько денег вам осталось потратить в категории прежде чем вы выйдете за рамки бюджета данной категории.

На странице трат вы указываете транзакции типа "трата", которые отнимают деньги с указанного вами счета.
На странице доходов вы указываете транзакции типа "доход", которые прибавляют деньги на указанный вами счет.
Вы также можете указывать учитывать ли те или иные транзакции при анализе или нет.

Вы не можете создавать транзакции, категории/сбережения которых не существует.

Приятного использования!
