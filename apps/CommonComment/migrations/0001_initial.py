# Generated by Django 2.1.5 on 2019-02-15 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('photo', models.ImageField(default='coreuser/default/tx3.jpg', max_length=200, upload_to='comment/', verbose_name='头像')),
                ('content', models.TextField(max_length=300, verbose_name='留言内容')),
                ('make_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '留言数据',
                'verbose_name_plural': '留言数据',
            },
        ),
    ]
