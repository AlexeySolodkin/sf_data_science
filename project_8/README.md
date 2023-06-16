# Проект 8. Итоговый проект первого года обучения. Государственные деньги у НКО.

## Оглавление
[1. Описание проекта](https://github.com/AlexeySolodkin/sf_data_science/tree/main/project_8/README.md#Описание-проекта)    
[2. Какой кейс решаем](https://github.com/AlexeySolodkin/sf_data_science/tree/main/project_8/README.md#Какой-кейс-решаем)         
[3. Краткая информация о данных](https://github.com/AlexeySolodkin/sf_data_science/tree/main/project_8/README.md#Краткая-информация-о-данных)             
[4. Этапы работы над проектом](https://github.com/AlexeySolodkin/sf_data_science/tree/main/project_8/README.md#Этапы-работы-над-проектом)               
[5. Резыльтаты](https://github.com/AlexeySolodkin/sf_data_science/tree/main/project_8/README.md#Результаты)
[6. Выводы](https://github.com/AlexeySolodkin/sf_data_science/tree/main/project_8/README.md#Выводы)

### Описание проекта
Проверить, есть ли зависимость вероятности получения грантов от государства/госконтрактов от региона регистрации организации, возраста организации и экономической деятельности организации.

:arrow_up:[к оглавлению](https://github.com/AlexeySolodkin/sf_data_science/tree/main/project_8/README.md#Оглавление)


### Какой кейс решаем
Необходимо продемострировать комплексные знания и навыки при решение самостоятельной задачи, использую полученные в ходе обучения знания.


**Что практикуем**
- Загрузка и обработка данных.
- Применение различных алгоритмов ML для решения практических кейсов.
- Подготовка модели для публикации в ПРОД.


### Краткая информация о данных
В нашем распоряжении есть [дамп базы данных](https://drive.google.com/file/d/1PQweRjt7uX00mWva0_goaj8JLz1tiTLx/view?usp=sharing) обо всех НКО России(источник данных - проект "[Открытые НКО](https://openngo.ru/)"), в котором содержится информация о получении государственных грантов, госконтрактов и субсидий, регионе и дате регистрации, а также ОКВЭД. Исходные данные представлены в формате json.
[Описание полей](https://github.com/infoculture/openngo-data-reference/wiki/%D0%A5%D0%B0%D1%80%D0%B0%D0%BA%D1%82%D0%B5%D1%80%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B8-%D0%B8-%D1%80%D0%B0%D1%81%D1%88%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D0%BA%D0%B8-%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D1%82%D1%8B%D1%85-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85).
Структура данных:
{
    "minjustRegNum": "7814061218", 
    "regionName": "Санкт-Петербург", 
    "logo": null, 
    "statusDetail": {
        "name": null, 
        "code": null, 
        "shortName": "Действующая"
    }, 
    "fullName": "МЕЖРЕГИОНАЛЬНАЯ АНТРОПОСОФСКАЯ МЕДИЦИНСКАЯ АССОЦИАЦИЯ", 
    "dateReg": null, 
    "minjustForm": "Объединения (союз, ассоциация) юридических лиц", 
    "charter": null, 
    "minjustStatus": "Зарегистрирована", 
    "ogrn": "1207800141790", 
    "opf": {
        "name": "Ассоциации (союзы)", 
        "code": "20600", 
        "version": "okopf"
    }, 
    "oktmo": {
        "name": null, 
        "code": null
    }, 
    "egrulStatus": "Действует", 
    "mainOkved": {
        "name": "Деятельность профессиональных членских организаций", 
        "code": "94.12", 
        "version": "ОК 029-2014 (КДЕС Ред. 2)"
    }, 
    "regionCode": "78", 
    "incomeTotal": 0, 
    "email": null, 
    "incomeDetail": {
        "grants": {
            "totalCount": 0, 
            "totalSum": 0
        }, 
        "fedSubsidies": {
            "totalCount": 0, 
            "totalSum": 0
        }, 
        "contracts44": {
            "totalCount": 0, 
            "totalSum": 0
        }, 
        "contracts223": {
            "totalCount": 0, 
            "totalSum": 0
        }, 
        "contracts94": {
            "totalCount": 0, 
            "totalSum": 0
        }
    }, 
    "administrators": [
        {
            "name": "КОШЕЧКИН ДЕНИС ВИКТОРОВИЧ", 
            "title": "ПРЕДСЕДАТЕЛЬ ПРАВЛЕНИЯ"
        }
    ], 
    "inn": "7841091168", 
    "okpo": null, 
    "originDate": {"$date": "2020-10-30T00:00:00.000Z"}, 
    "website": null, 
    "dateLiquid": null, 
    "address": "191186, ГОРОД САНКТ-ПЕТЕРБУРГ, УЛИЦА ИТАЛЬЯНСКАЯ, ДОМ 10/5, ЛИТЕР А, ПОМЕЩЕНИЕ 8-Н", 
    "successors": [], 
    "okogu": {
        "name": null, 
        "code": null
    }, 
    "kpp": "784101001", 
    "hasRegionalSupport": false, 
    "addOkved": [], 
    "okato": {
        "name": null, 
        "code": null
    }, 
    "okfs": {
        "name": null, 
        "code": null
    }, 
    "website_punycode": null, 
    "shortName": "\"АМА\"", 
    "dateOgrn": {"$date": "2020-10-30T00:00:00.000Z"}, 
    "predecessors": [], 
    "socialMedia": {
        "youtube": null, 
        "vk": null,
        "facebook": null, 
        "twitter": null, 
        "instagram": null, 
        "ok": null
    }, 
    "reports": []
}

:arrow_up:[к оглавлению](https://github.com/AlexeySolodkin/sf_data_science/tree/main/project_8/README.md#Оглавление)


### Этапы работы над проектом  
1. Загрузка и объединение данных в один датафрейм.
2. Извлечение необходимой информации из первичных данных.
3. Создание необходимых признаков, анализ и обработка данных.
4. Обучение базовых алгоритмов классификации ML.
5. Выбор наилучшего базового алгоритма и подпор гиперпараметров для улучшения модели.
6. Обучение ансамблевых алгоритмов ML.
7. Подготовка модели в публикации в ПРОД.
8. Подготовлена документация.
9. Проект выложен на GitHub.

:arrow_up:[к оглавлению](https://github.com/AlexeySolodkin/sf_data_science/tree/main/project_8/README.md#Оглавление)


### Результаты:  
* Кейс обработан, модель обучена.
* Модель подготовлена для публикации в ПРОД.
* Подготовлена документация по проекту.
* Проект выложен на GitHub.

:arrow_up:[к оглавлению](https://github.com/AlexeySolodkin/sf_data_science/tree/main/project_8/README.md#Оглавление)


### Выводы:  
Есть слабая зависимость вероятности получения грантов от государства/госконтрактов от региона регистрации организации, возраста организации и экономической деятельности организации.

:arrow_up:[к оглавлению](https://github.com/AlexeySolodkin/sf_data_science/tree/main/project_8/README.md#Оглавление)
