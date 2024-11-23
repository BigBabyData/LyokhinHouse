# LyokhinHouse🏠
[Web-site](https://lyokhinhouse.up.railway.app/) for LyokhinHouse pet shelter🐈.

# FlaskAPI
*API URL*: ```https://lyokhinhouse-api.up.railway.app```

***Запросы:***

* ```/get-cats-in-shelter``` **[GET]** на получение всех котов, которые уже живут в приюте. Структура ответа JSON:
```
{
  "cats_in_shelter": [
    {
      "arrival_date": "ДАТА ПРИБЫТИЯ В ПРИЮТ",
      "cat_age": <ВОЗРАСТ КОТА В ГОДАХ>,
      "cat_name": "ИМИ КОТА",
      "description": "ОПИСАНИЕ КОТА",
      "id": UniqueID,
      "image_url": "ССЫЛКА НА ФОТОКАРТОЧКУ КОТА",
      "time_at_shelter": <ВРЕМЯ НАХОЖДЕНИЯ В ПРИЮТЕ В МЕСЯЦАХ>
    }
  ]
}
```

* ```/get-cat-in-shelter/<int:cat_id>``` **[GET]** на получение одного конкретного кота, который живёт в приюте, по его UID, тут угловые скобки целиком заменяются на число — UID кота. Ответ JSON:
```
{
  "arrival_date": "ДАТА ПРИБЫТИЯ В ПРИЮТ",
  "cat_age": <ВОЗРАСТ КОТА В ГОДАХ>,
  "cat_name": "ИМИ КОТА",
  "description": "ОПИСАНИЕ КОТА",
  "id": UniqueID,
  "image_url": "ССЫЛКА НА ФОТОКАРТОЧКУ КОТА",
  "time_at_shelter": <ВРЕМЯ НАХОЖДЕНИЯ В ПРИЮТЕ В МЕСЯЦАХ>
}
```

* ```/get-new-cats``` **[GET]** на получение потенциальных новых котов (их заявок), которых хотят сдать на заселение в приют. Структура JSON:
```
{
  "new_cats": [
    {
      "breed": "ПОРОДА",
      "cat_name": "ИМЯ КОТА",
      "cat_type": "ТИП КОТА: УЛИЧНЫЙ/ДОМАШНИЙ",
      "gender": "ПОЛ КОТА",
      "id": UniqueID,
      "owner_name": "ФИО владельца",
      "phone_number": "НОМЕР ТЕЛЕФОНА ВЛАДЕЛЬЦА",
      "reason_to_give_to_shelter": "ПРИЧИНА ОТДАВАТЬ КОТА",
      "where_found": "МЕСТО, ГДЕ НАШЛИ КОТА"
    }
  ]
}
```

* ```/submit-application``` **[POST]** на *ЗАПИСЬ* заявки на *СДАЧУ* кота в приют, она требует JSON вот такого вида (без указания UID, база данных сама укажет новый UID), OPTIONS.json:
```
{
  "owner_name": "Ваше имя",
  "phone_number": "Ваш номер телефона",
  "cat_type": "Тип кошки",
  "where_found": "Место нахождения",
  "reason_to_give_to_shelter": "Причина передачи в приют",
  "breed": "Порода",
  "gender": "Пол",
  "cat_name": "Имя кошки"
}
```

* ```/submit-take-cat``` **[POST]** на *ЗАПИСЬ* заявки на то, чтобы *ЗАБРАТЬ* кота из приюта, требует JSON в таком виде (так же без указаний айдишника), OPTIONS.json:
```
{
  "id": UniqueID,
  "full_name": "ИМЯ",
  "phone_number": "НОМЕР ТЕЛЕФОНА",
  "when_pick_up": "КОГДА УДОБНО ЗАБРАТЬ"
}
```

# Architecture
![Untitled](https://github.com/user-attachments/assets/39c540ba-8054-4b0f-894a-5240b40332ab)
![Снимок экрана 2024-11-21 231625](https://github.com/user-attachments/assets/fe655123-3e4d-4948-98aa-986f7f67bfdc)
