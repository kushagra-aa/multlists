# Mult Lists
<img src="https://user-images.githubusercontent.com/68841296/129093152-d40243b5-9e7e-43fb-8d53-d5ee7f707aea.png" alt="drawing" width="200"/>

[Click Here To Visit](https://github.com/kushagra-aa/multlists)

Fast craigslists web scrapper

A much cooler Interface to Craigslists

Scrape away right here faster!

Built with 🤍 For You!



## Screenshots

![App Screenshot](https://user-images.githubusercontent.com/68841296/129092327-be3faad7-6010-40ee-821c-34365e90534b.png)
![image](https://user-images.githubusercontent.com/68841296/129092655-f1c18467-84ef-4786-8d2e-cf34ead9f9b1.png)
![image](https://user-images.githubusercontent.com/68841296/129092744-296c32dd-d94c-4548-928c-deb3df71377a.png)

## Run Locally

Clone the project

```bash
  git clone https://github.com/kushagra-aa/multlists.git
```

Go to the project directory

```bash
  cd multlists
```

Install dependencies

```bash
  pip install -r requirements.txt
```

then run
```bash
python manage.py migrate
```
create admin account
```bash
python manage.py createsuperuser
```
then
```bash
python manage.py makemigrations
```
to makemigrations for the app

then again run
```bash
python manage.py migrate
```

to start the development server
```bash
python manage.py runserver
```
and open localhost:8000 on your browser to view the app.
