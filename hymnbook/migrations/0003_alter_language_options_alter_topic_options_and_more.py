# Generated by Django 4.2.3 on 2023-08-03 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hymnbook', '0002_alter_arranger_options_alter_audiofile_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['code'], 'verbose_name': 'language', 'verbose_name_plural': 'languages'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['code'], 'verbose_name': 'topic', 'verbose_name_plural': 'topics'},
        ),
        migrations.RemoveField(
            model_name='topic',
            name='title',
        ),
        migrations.AlterField(
            model_name='arranger',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='arranger',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='audio_file',
            field=models.FileField(upload_to='hymnbook/audio-files/', verbose_name='audio file'),
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='voice_type',
            field=models.CharField(choices=[('S0', 'Soprano'), ('S1', 'Soprano 1'), ('S2', 'Soprano 2'), ('A0', 'Alto'), ('A1', 'Alto 1'), ('A2', 'Alto 2'), ('T0', 'Tenor'), ('T1', 'Tenor 1'), ('T2', 'Tenor 2'), ('B0', 'Bass'), ('B1', 'Bass 1'), ('B2', 'Bass 2'), ('I0', 'Solo'), ('I1', 'Solo 1'), ('I2', 'Solo 2'), ('EV', 'SATB')], default='S0', max_length=2, verbose_name='voice type'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='hymn',
            name='arrangers',
            field=models.ManyToManyField(blank=True, related_name='hymns', to='hymnbook.arranger', verbose_name='arrangers'),
        ),
        migrations.AlterField(
            model_name='hymn',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='hymns', to='hymnbook.author', verbose_name='authors'),
        ),
        migrations.AlterField(
            model_name='hymn',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hymns', to='hymnbook.language', verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='hymn',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='notes'),
        ),
        migrations.AlterField(
            model_name='hymn',
            name='pdf_file',
            field=models.FileField(upload_to='hymnbook/pdf-files/', verbose_name='pdf file'),
        ),
        migrations.AlterField(
            model_name='hymn',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='hymn',
            name='topics',
            field=models.ManyToManyField(related_name='hymns', to='hymnbook.topic', verbose_name='topics'),
        ),
        migrations.AlterField(
            model_name='hymn',
            name='transcribers',
            field=models.ManyToManyField(blank=True, related_name='hymns', to='hymnbook.transcriber', verbose_name='transcribers'),
        ),
        migrations.AlterField(
            model_name='hymn',
            name='translators',
            field=models.ManyToManyField(blank=True, related_name='hymns', to='hymnbook.translator', verbose_name='traslators'),
        ),
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(choices=[('aa', 'Afar'), ('ab', 'Abkhazian'), ('ae', 'Avestan'), ('af', 'Afrikaans'), ('ak', 'Akan'), ('am', 'Amharic'), ('an', 'Aragonese'), ('ar', 'Arabic'), ('as', 'Assamese'), ('av', 'Avaric'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('ba', 'Bashkir'), ('be', 'Belarusian'), ('bg', 'Bulgarian'), ('bh', 'Bihari languages'), ('bi', 'Bislama'), ('bm', 'Bambara'), ('bn', 'Bengali'), ('bo', 'Tibetan'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan; Valencian'), ('ce', 'Chechen'), ('ch', 'Chamorro'), ('co', 'Corsican'), ('cr', 'Cree'), ('cs', 'Czech'), ('cu', 'Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic'), ('cv', 'Chuvash'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dv', 'Divehi; Dhivehi; Maldivian'), ('dz', 'Dzongkha'), ('ee', 'Ewe'), ('el', 'Greek, Modern (1453-)'), ('en', 'English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('ff', 'Fulah'), ('fi', 'Finnish'), ('fj', 'Fijian'), ('fo', 'Faroese'), ('fr', 'French'), ('fy', 'Western Frisian'), ('ga', 'Irish'), ('gd', 'Gaelic; Scomttish Gaelic'), ('gl', 'Galician'), ('gn', 'Guarani'), ('gu', 'Gujarati'), ('gv', 'Manx'), ('ha', 'Hausa'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('ho', 'Hiri Motu'), ('hr', 'Croatian'), ('ht', 'Haitian; Haitian Creole'), ('hu', 'Hungarian'), ('hy', 'Armenian'), ('hz', 'Herero'), ('ia', 'Interlingua (International Auxiliary Language Association)'), ('id', 'Indonesian'), ('ie', 'Interlingue; Occidental'), ('ig', 'Igbo'), ('ii', 'Sichuan Yi; Nuosu'), ('ik', 'Inupiaq'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('iu', 'Inuktitut'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('ka', 'Georgian'), ('kg', 'Kongo'), ('ki', 'Kikuyu; Gikuyu'), ('kj', 'Kuanyama; Kwanyama'), ('kk', 'Kazakh'), ('kl', 'Kalaallisut; Greenlandic'), ('km', 'Central Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('kr', 'Kanuri'), ('ks', 'Kashmiri'), ('ku', 'Kurdish'), ('kv', 'Komi'), ('kw', 'Cornish'), ('ky', 'Kirghiz; Kyrgyz'), ('la', 'Latin'), ('lb', 'Luxembourgish; Letzeburgesch'), ('lg', 'Ganda'), ('li', 'Limburgan; Limburger; Limburgish'), ('ln', 'Lingala'), ('lo', 'Lao'), ('lt', 'Lithuanian'), ('lu', 'Luba-Katanga'), ('lv', 'Latvian'), ('mg', 'Malagasy'), ('mh', 'Marshallese'), ('mi', 'Maori'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('ms', 'Malay'), ('mt', 'Maltese'), ('my', 'Burmese'), ('na', 'Nauru'), ('nb', 'Bokmål, Norwegian; Norwegian Bokmål'), ('nd', 'Ndebele, North; North Ndebele'), ('ne', 'Nepali'), ('ng', 'Ndonga'), ('nl', 'Dutch; Flemish'), ('nn', 'Norwegian Nynorsk; Nynorsk, Norwegian'), ('no', 'Norwegian'), ('nr', 'Ndebele, South; South Ndebele'), ('nv', 'Navajo; Navaho'), ('ny', 'Chichewa; Chewa; Nyanja'), ('oc', 'Occitan (post 1500)'), ('oj', 'Ojibwa'), ('om', 'Oromo'), ('or', 'Oriya'), ('os', 'Ossetian; Ossetic'), ('pa', 'Panjabi; Punjabi'), ('pi', 'Pali'), ('pl', 'Polish'), ('ps', 'Pushto; Pashto'), ('pt', 'Portuguese'), ('qu', 'Quechua'), ('rm', 'Romansh'), ('rn', 'Rundi'), ('ro', 'Romanian; Moldavian; Moldovan'), ('ru', 'Russian'), ('rw', 'Kinyarwanda'), ('sa', 'Sanskrit'), ('sc', 'Sardinian'), ('sd', 'Sindhi'), ('se', 'Northern Sami'), ('sg', 'Sango'), ('si', 'Sinhala; Sinhalese'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sm', 'Samoan'), ('sn', 'Shona'), ('so', 'Somali'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('ss', 'Swati'), ('st', 'Sotho, Southern'), ('su', 'Sundanese'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('tg', 'Tajik'), ('th', 'Thai'), ('ti', 'Tigrinya'), ('tk', 'Turkmen'), ('tl', 'Tagalog'), ('tn', 'Tswana'), ('to', 'Tonga (Tonga Islands)'), ('tr', 'Turkish'), ('ts', 'Tsonga'), ('tt', 'Tatar'), ('tw', 'Twi'), ('ty', 'Tahitian'), ('ug', 'Uighur; Uyghur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('ve', 'Venda'), ('vi', 'Vietnamese'), ('vo', 'Volapük'), ('wa', 'Walloon'), ('wo', 'Wolof'), ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('za', 'Zhuang; Chuang'), ('zh', 'Chinese'), ('zu', 'Zulu')], default='es', max_length=2, primary_key=True, serialize=False, verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='code',
            field=models.CharField(choices=[('ADO', 'Adoración'), ('ADV', 'Advenimiento del Señor'), ('ALB', 'Alabanza Cristiana'), ('AMA', 'Amanecer Cristiano'), ('AMI', 'Amistad Divina'), ('AMO', 'Amor de Dios'), ('ANN', 'Año Nuevo'), ('AVI', 'Avivamiento Espiritual'), ('BAU', 'Bautismo en Agua'), ('BBL', 'Biblia Santa'), ('BNV', 'Bienvenida a los Santos'), ('COM', 'Comunión Espiritual'), ('CNF', 'Confianza en el Senor'), ('CNG', 'Consagración Cristiana'), ('COR', 'Coros de Alabanza'), ('DED', 'Dedicación del Templo'), ('DES', 'Despedida de los Santos'), ('DIV', 'Divinidad'), ('DUE', 'Duermen en el Señor'), ('ELE', 'Elección Apostolica'), ('EXH', 'Exhortación al Cristiano'), ('ESP', 'Esperanza'), ('EVA', 'Evangelización'), ('GOZ', 'Gozo Espiritual'), ('GRC', 'Gracia Divina'), ('GRT', 'Gratitud al Señor'), ('HON', 'Honra a sus Siervos'), ('IDO', 'Idolatría del Mundo'), ('INT', 'Intercesión Divina'), ('JUV', 'Juventud Cristiana'), ('LIB', 'Liberalidad Cristiana'), ('LCH', 'Luchar en el Señor'), ('LLA', 'Llamamiento del Señor'), ('MAT', 'Matrimonio Cristiano'), ('MED', 'Meditación'), ('NIC', 'Niñez Cristiana'), ('OBR', 'Obreros de Dios'), ('PAS', 'Pasión de Cristo'), ('PRD', 'Perdón Divino'), ('PRC', 'Persecución Cristiana'), ('PRV', 'Perseverancia'), ('REP', 'Reprensión del Señor'), ('RES', 'Restauración de la Iglesia'), ('SAL', 'Salmos'), ('SND', 'Sanidad Divina'), ('SNC', 'Santa Cena'), ('SUP', 'Súplica')], default='ADO', max_length=3, primary_key=True, serialize=False, verbose_name='topic'),
        ),
        migrations.AlterField(
            model_name='transcriber',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='transcriber',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='translator',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='translator',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='last name'),
        ),
    ]
