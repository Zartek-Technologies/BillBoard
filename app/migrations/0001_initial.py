# Generated by Django 2.2.3 on 2019-08-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_tble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BillBoardId', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=50)),
                ('Emailaddress', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Message', models.CharField(max_length=50)),
            ],
        ),
    ]
