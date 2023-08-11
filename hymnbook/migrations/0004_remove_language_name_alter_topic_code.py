# Generated by Django 4.2.3 on 2023-08-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hymnbook', '0003_alter_language_options_alter_topic_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='name',
        ),
        migrations.AlterField(
            model_name='topic',
            name='code',
            field=models.CharField(choices=[('ADO', 'Worship'), ('ADV', 'Advent of the Lord'), ('ALB', 'Praise'), ('AMA', 'Dawn'), ('AMO', 'Love'), ('ANN', 'New Year'), ('BAU', 'Baptism'), ('BNV', 'Welcoming'), ('COM', 'Communion'), ('CNF', 'Trust'), ('CNG', 'Consecration'), ('DES', 'Farewell'), ('DUE', 'Rest in the Lord'), ('ELE', 'Election'), ('ESP', 'Hope'), ('EVA', 'Evangelization'), ('EXH', 'Exhortation'), ('GLO', 'Glory'), ('GOZ', 'Joy'), ('GRC', 'Grace'), ('GRT', 'Gratitud'), ('HON', 'Honor'), ('ING', 'Inauguration'), ('INT', 'Intercession'), ('INV', 'Invitation'), ('JUV', 'Youth'), ('LIB', 'Liberality'), ('LCH', 'Battle'), ('MAT', 'Marriage'), ('OBR', 'Labor'), ('ORA', 'Prayer'), ('OAP', 'Apostolic Prayer'), ('PAS', 'Passion'), ('PET', 'Petition'), ('RST', 'Restoration'), ('RSU', 'Resurrection'), ('SNC', 'Holy Supper')], default='ADO', max_length=3, primary_key=True, serialize=False, verbose_name='topic'),
        ),
    ]
