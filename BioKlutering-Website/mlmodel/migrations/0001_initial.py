# Generated by Django 3.0.3 on 2020-02-26 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filepath', models.FileField('File', upload_to="userfiles/", help_text="Select a file here" )),
                ('kmer', models.CharField('Kmer size', max_length=200, blank=True, null=True, help_text = "Enter one or more kmer sizes here if you want to train the model with specific kmer size. Please separate each kmer size by a comma.")),    
                ('email', models.EmailField('Email', max_length = 254, blank=True, null=True, help_text="If you want to send the result to email, please enter an email address here."))
            ],
        ),
    ]


