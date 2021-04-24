# Generated by Django 3.0.5 on 2020-06-29 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('branches_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=100)),
                ('problem', models.CharField(max_length=100)),
                ('classes', models.CharField(max_length=100)),
                ('no_lectures', models.IntegerField(default=0)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.Login')),
            ],
        ),
        migrations.CreateModel(
            name='Institute_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('teachers_no', models.IntegerField()),
                ('college_open', models.CharField(max_length=5)),
                ('college_close', models.CharField(max_length=5)),
                ('details', models.CharField(default='False', max_length=10)),
                ('tdetails', models.CharField(max_length=10)),
                ('slots', models.PositiveIntegerField(default=0)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.Login')),
            ],
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=100)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institute.Login')),
            ],
        ),
    ]
