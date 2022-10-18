Урок 6. Фреймворк Scrapy, pipelines, Splash
I вариант
1) Доработать паука в имеющемся проекте, чтобы он формировал item по структуре:
*Наименование вакансии
*Зарплата от
*Зарплата до
*Ссылку на саму вакансию
И складывал все записи в БД(любую)

2) Создать в имеющемся проекте второго паука по сбору вакансий с сайта superjob. Паук должен формировать item'ы по аналогичной структуре и складывать данные также в БД

#### 1) Паук - [hhru](https://github.com/elfobey/internet_data_collection/blob/lesson6/hhru.py)

#### 2) Паук - [sjru](https://github.com/elfobey/internet_data_collection/blob/lesson6/sj.py)

#### 3) Сохранение в структуру данных - [piplines](https://github.com/elfobey/internet_data_collection/blob/lesson6/pipeline.py) 
