# LyokhinHouse🏠 API Документация

**Описание:**  
Данный API предоставляет доступ к данным о котах, содержащихся в приюте, а также к заявкам на добавление и забирание котов. С его помощью можно получать информацию о котах, добавлять новые заявки и просматривать заявки, требующие административного доступа.

**Базовый URL:**  
```
https://lyokhinhouse-api.up.railway.app
```

----------------------------------------
## Маршруты для публичного доступа

### 1. Проверка статуса сервера

**Эндпоинт:**  
```GET /```

**Описание:**  
Позволяет проверить работоспособность сервера.

**Пример ответа (JSON):**  
```json
{
  "status": "LyokhinHouse API is now running!"
}
```

----------------------------------------
### 2. Получение всех котов в приюте

**Эндпоинт:**  
```GET /get_cats_in_shelter```

**Описание:**  
Возвращает список всех котов, содержащихся в приюте.

**Пример ответа (JSON):**  
```json
{
  "cats_in_shelter": [
    {
      "id": 123,
      "cat_name": "Барсик",
      "cat_age": 3,
      "description": "Дружелюбный рыжий кот",
      "image_url": "https://example.com/barsik.jpg",
      "time_at_shelter": 5,
      "arrival_date": "2024-01-10"
    }
  ]
}
```

**Пояснения к полям:**
- **id (int)**: Уникальный идентификатор кота.
- **cat_name (string)**: Имя кота.
- **cat_age (int)**: Возраст кота в годах.
- **description (string)**: Краткое описание кота.
- **image_url (string)**: Ссылка на изображение кота.
- **time_at_shelter (int)**: Время нахождения в приюте (в месяцах).
- **arrival_date (string, формат YYYY-MM-DD)**: Дата прибытия кота в приют.

----------------------------------------
### 3. Получение конкретного кота по ID

**Эндпоинт:**  
```GET /get_cat_in_shelter/<int:cat_id>```

**Описание:**  
Возвращает данные о конкретном коте, находящемся в приюте, по его уникальному ID.

**Пример ответа (JSON):**  
```json
{
  "id": 123,
  "cat_name": "Барсик",
  "cat_age": 3,
  "description": "Дружелюбный рыжий кот",
  "image_url": "https://example.com/barsik.jpg",
  "time_at_shelter": 5,
  "arrival_date": "2024-01-10"
}
```

Если кот с указанным ID не найден, возвращается ошибка:
```json
{
  "error": "Cat not found"
}
```

----------------------------------------
### 4. Отправка заявки на добавление кота в приют

**Эндпоинт:**  
```POST /submit_application```

**Описание:**  
Принимает заявку на добавление нового кота в приют. Отправитель заполняет форму с данными о коте, а также контактные данные.

**Тело запроса (JSON):**  
```json
{
  "owner_name": "Имя владельца",
  "phone_number": "Номер телефона",
  "cat_type": "Домашний или уличный",
  "where_found": "Место, где кот был найден",
  "reason_to_give_to_shelter": "Причина передачи кота в приют",
  "breed": "Порода кота",
  "gender": "Пол кота",
  "cat_name": "Имя кота"
}
```

**Ответ при успешной отправке заявки (JSON):**  
```json
{
  "message": "Application added successfully!",
  "id": 456
}
```

При некорректных данных или ошибке БД:
```json
{
  "error": "Описание ошибки"
}
```

**Примечание:** ID заявки генерируется автоматически при добавлении в базу данных.

----------------------------------------
### 5. Отправка заявки на забор кота из приюта

**Эндпоинт:**  
```POST /submit_take_cat```

**Описание:**  
Принимает заявку от человека, желающего забрать кота из приюта.

**Тело запроса (JSON):**  
```json
{
  "full_name": "Имя и Фамилия",
  "phone_number": "Номер телефона",
  "when_pick_up": "Удобное время для забора кота"
}
```

**Ответ при успешной отправке заявки (JSON):**  
```json
{
  "message": "Application added successfully!",
  "id": 789
}
```

При ошибках:
```json
{
  "error": "Описание ошибки"
}
```

----------------------------------------
## Маршруты, требующие админ-токен

Для доступа к данным о заявках на добавление или забор кота, а также для удаления заявок, необходим администраторский токен.  
В каждый запрос необходимо передать заголовок `Token: <ADMIN_TOKEN>`.

----------------------------------------
### 6. Получение всех заявок на добавление новых котов

**Эндпоинт:**  
```GET /get_new_cats_applications```

**Описание:**  
Возвращает список всех заявок на добавление котов в приют. Требуется админ-токен.

**Пример ответа (JSON):**  
```json
{
  "new_cats": [
    {
      "id": 456,
      "owner_name": "Иван Иванов",
      "phone_number": "+7 (999) 123-45-67",
      "cat_type": "Домашний",
      "where_found": "Подъезд дома",
      "reason_to_give_to_shelter": "Нет возможности содержать",
      "breed": "Британская короткошёрстная",
      "gender": "Мальчик",
      "cat_name": "Гарри"
    }
  ]
}
```

----------------------------------------
### 7. Получение всех заявок на забор кота

**Эндпоинт:**  
```GET /get_take_cats_applications```

**Описание:**  
Возвращает список всех заявок на забор кота из приюта. Требуется админ-токен.

**Пример ответа (JSON):**  
```json
{
  "take_cats_applications": [
    {
      "id": 789,
      "full_name": "Петров Петр",
      "phone_number": "+7 (912) 345-67-89",
      "when_pick_up": "2024-02-15 14:00"
    }
  ]
}
```

----------------------------------------
### 8. Удаление заявки на нового кота

**Эндпоинт:**  
```DELETE /delete_new_cat_application/<int:app_id>```

**Описание:**  
Удаляет заявку на добавление кота по ее уникальному идентификатору. Требуется админ-токен.

**Пример успешного ответа:**  
```json
{
  "message": "Application deleted successfully"
}
```

Если заявка не найдена:
```json
{
  "error": "Application not found"
}
```

При ошибках базы данных:
```json
{
  "error": "Описание ошибки"
}
```

----------------------------------------
### 9. Удаление заявки на забор кота

**Эндпоинт:**  
```DELETE /delete_take_cat_application/<int:app_id>```

**Описание:**  
Удаляет заявку на забор кота из приюта по ее уникальному идентификатору. Требуется админ-токен.

**Пример успешного ответа:**  
```json
{
  "message": "Application deleted successfully"
}
```

Если заявка не найдена:
```json
{
  "error": "Application not found"
}
```

При ошибках базы данных:
```json
{
  "error": "Описание ошибки"
}
```

----------------------------------------
# Архитектура

Ниже приведены схемы архитектуры приложения для наглядного понимания взаимодействия компонентов:

![Схема архитектуры 1](https://github.com/user-attachments/assets/39c540ba-8054-4b0f-894a-5240b40332ab)

![Схема архитектуры 2](https://github.com/user-attachments/assets/fe655123-3e4d-4948-98aa-986f7f67bfdc)

----------------------------------------

**Примечание:**  
- Перед тем, как начать работу с админскими маршрутами, убедитесь, что у вас есть корректный `ADMIN_TOKEN` и что он передается в заголовках запросов.
- Формат дат для полей `arrival_date` и `when_pick_up` может отличаться в зависимости от интеграции.
