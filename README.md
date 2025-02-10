![Django Logo](https://www.djangoproject.com/m/img/logos/django-logo-positive.png)

# راهنمای اجرای پروژه

این پروژه با استفاده از جنگو (Django) توسعه داده شده است. برای اجرای پروژه، مراحل زیر را دنبال کنید.

## پیش‌نیازها

- پایتون (Python) نسخه 3.x
- pip (برای نصب بسته‌های مورد نیاز)

## نصب و راه‌اندازی

1. **ساخت Migrations**:  
   برای ایجاد فایل‌های migrations از دستور زیر استفاده کنید:

   ```bash
   python manage.py makemigrations

2. **ساخت migrate**:  
   پس از ایجاد migrations، آن‌ها را با دستور زیر اعمال کنید:

   ```bash
   python manage.py migrate

3. **جمع‌آوری فایل‌های استاتیک**:  
   برای جمع‌آوری فایل‌های استاتیک (static files) از دستور زیر استفاده کنید:

   ```bash
   python manage.py collectstatic

4. **اجرای سرور توسعه**:  
   پس از انجام مراحل بالا، می‌توانید سرور توسعه جنگو را با دستور زیر اجرا کنید:

   ```bash
   python manage.py runserver

5. **نکات اضافی**:  
   اطمینان حاصل کنید که تمامی بسته‌های مورد نیاز در فایل requirements.txt نصب شده‌اند. برای نصب آن‌ها از دستور زیر استفاده کنید

   ```bash
   pip install -r requirements.txt
