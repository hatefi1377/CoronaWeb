# Generated by Django 3.0.3 on 2020-03-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoronaCase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casedetail',
            name='case_address',
            field=models.TextField(blank=True, default='Unknown', null=True),
        ),
        migrations.AlterField(
            model_name='casedetail',
            name='case_image',
            field=models.ImageField(default='default.jpeg', upload_to='cases_pics'),
        ),
        migrations.AlterField(
            model_name='casedetail',
            name='case_last_seen',
            field=models.TextField(blank=True, default='Unknown', null=True),
        ),
        migrations.AlterField(
            model_name='casedetail',
            name='case_name',
            field=models.CharField(blank=True, default='Unknown', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='casedetail',
            name='case_number',
            field=models.CharField(blank=True, default='Unknown', max_length=10, null=True),
        ),
    ]
