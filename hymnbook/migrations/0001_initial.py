# Generated by Django 4.2.3 on 2023-08-02 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arranger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('code', models.CharField(choices=[('aa', 'Afar'), ('ab', 'Abkhazian'), ('ae', 'Avestan'), ('af', 'Afrikaans'), ('ak', 'Akan'), ('am', 'Amharic'), ('an', 'Aragonese'), ('ar', 'Arabic'), ('as', 'Assamese'), ('av', 'Avaric'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('ba', 'Bashkir'), ('be', 'Belarusian'), ('bg', 'Bulgarian'), ('bh', 'Bihari languages'), ('bi', 'Bislama'), ('bm', 'Bambara'), ('bn', 'Bengali'), ('bo', 'Tibetan'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan; Valencian'), ('ce', 'Chechen'), ('ch', 'Chamorro'), ('co', 'Corsican'), ('cr', 'Cree'), ('cs', 'Czech'), ('cu', 'Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic'), ('cv', 'Chuvash'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dv', 'Divehi; Dhivehi; Maldivian'), ('dz', 'Dzongkha'), ('ee', 'Ewe'), ('el', 'Greek, Modern (1453-)'), ('en', 'English'), ('eo', 'Esperanto'), ('es', 'Español'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('ff', 'Fulah'), ('fi', 'Finnish'), ('fj', 'Fijian'), ('fo', 'Faroese'), ('fr', 'French'), ('fy', 'Western Frisian'), ('ga', 'Irish'), ('gd', 'Gaelic; Scomttish Gaelic'), ('gl', 'Galician'), ('gn', 'Guarani'), ('gu', 'Gujarati'), ('gv', 'Manx'), ('ha', 'Hausa'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('ho', 'Hiri Motu'), ('hr', 'Croatian'), ('ht', 'Haitian; Haitian Creole'), ('hu', 'Hungarian'), ('hy', 'Armenian'), ('hz', 'Herero'), ('ia', 'Interlingua (International Auxiliary Language Association)'), ('id', 'Indonesian'), ('ie', 'Interlingue; Occidental'), ('ig', 'Igbo'), ('ii', 'Sichuan Yi; Nuosu'), ('ik', 'Inupiaq'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('iu', 'Inuktitut'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('ka', 'Georgian'), ('kg', 'Kongo'), ('ki', 'Kikuyu; Gikuyu'), ('kj', 'Kuanyama; Kwanyama'), ('kk', 'Kazakh'), ('kl', 'Kalaallisut; Greenlandic'), ('km', 'Central Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('kr', 'Kanuri'), ('ks', 'Kashmiri'), ('ku', 'Kurdish'), ('kv', 'Komi'), ('kw', 'Cornish'), ('ky', 'Kirghiz; Kyrgyz'), ('la', 'Latin'), ('lb', 'Luxembourgish; Letzeburgesch'), ('lg', 'Ganda'), ('li', 'Limburgan; Limburger; Limburgish'), ('ln', 'Lingala'), ('lo', 'Lao'), ('lt', 'Lithuanian'), ('lu', 'Luba-Katanga'), ('lv', 'Latvian'), ('mg', 'Malagasy'), ('mh', 'Marshallese'), ('mi', 'Maori'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('ms', 'Malay'), ('mt', 'Maltese'), ('my', 'Burmese'), ('na', 'Nauru'), ('nb', 'Bokmål, Norwegian; Norwegian Bokmål'), ('nd', 'Ndebele, North; North Ndebele'), ('ne', 'Nepali'), ('ng', 'Ndonga'), ('nl', 'Dutch; Flemish'), ('nn', 'Norwegian Nynorsk; Nynorsk, Norwegian'), ('no', 'Norwegian'), ('nr', 'Ndebele, South; South Ndebele'), ('nv', 'Navajo; Navaho'), ('ny', 'Chichewa; Chewa; Nyanja'), ('oc', 'Occitan (post 1500)'), ('oj', 'Ojibwa'), ('om', 'Oromo'), ('or', 'Oriya'), ('os', 'Ossetian; Ossetic'), ('pa', 'Panjabi; Punjabi'), ('pi', 'Pali'), ('pl', 'Polish'), ('ps', 'Pushto; Pashto'), ('pt', 'Portuguese'), ('qu', 'Quechua'), ('rm', 'Romansh'), ('rn', 'Rundi'), ('ro', 'Romanian; Moldavian; Moldovan'), ('ru', 'Russian'), ('rw', 'Kinyarwanda'), ('sa', 'Sanskrit'), ('sc', 'Sardinian'), ('sd', 'Sindhi'), ('se', 'Northern Sami'), ('sg', 'Sango'), ('si', 'Sinhala; Sinhalese'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sm', 'Samoan'), ('sn', 'Shona'), ('so', 'Somali'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('ss', 'Swati'), ('st', 'Sotho, Southern'), ('su', 'Sundanese'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('tg', 'Tajik'), ('th', 'Thai'), ('ti', 'Tigrinya'), ('tk', 'Turkmen'), ('tl', 'Tagalog'), ('tn', 'Tswana'), ('to', 'Tonga (Tonga Islands)'), ('tr', 'Turkish'), ('ts', 'Tsonga'), ('tt', 'Tatar'), ('tw', 'Twi'), ('ty', 'Tahitian'), ('ug', 'Uighur; Uyghur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('ve', 'Venda'), ('vi', 'Vietnamese'), ('vo', 'Volapük'), ('wa', 'Walloon'), ('wo', 'Wolof'), ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('za', 'Zhuang; Chuang'), ('zh', 'Chinese'), ('zu', 'Zulu')], default='es', max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('code', models.CharField(choices=[('ADO', 'Adoración'), ('ADV', 'Advenimiento del Señor'), ('ALB', 'Alabanza Cristiana'), ('AMA', 'Amanecer Cristiano'), ('AMI', 'Amistad Divina'), ('AMO', 'Amor de Dios'), ('ANN', 'Año Nuevo'), ('AVI', 'Avivamiento Espiritual'), ('BAU', 'Bautismo en Agua'), ('BBL', 'Biblia Santa'), ('BNV', 'Bienvenida a los Santos'), ('COM', 'Comunión Espiritual'), ('CNF', 'Confianza en el Senor'), ('CNG', 'Consagración Cristiana'), ('COR', 'Coros de Alabanza'), ('DED', 'Dedicación del Templo'), ('DES', 'Despedida de los Santos'), ('DIV', 'Divinidad'), ('DUE', 'Duermen en el Señor'), ('ELE', 'Elección Apostolica'), ('EXH', 'Exhortación al Cristiano'), ('ESP', 'Esperanza'), ('EVA', 'Evangelización'), ('GOZ', 'Gozo Espiritual'), ('GRC', 'Gracia Divina'), ('GRT', 'Gratitud al Señor'), ('HON', 'Honra a sus Siervos'), ('IDO', 'Idolatría del Mundo'), ('INT', 'Intercesión Divina'), ('JUV', 'Juventud Cristiana'), ('LIB', 'Liberalidad Cristiana'), ('LCH', 'Luchar en el Señor'), ('LLA', 'Llamamiento del Señor'), ('MAT', 'Matrimonio Cristiano'), ('MED', 'Meditación'), ('NIC', 'Niñez Cristiana'), ('OBR', 'Obreros de Dios'), ('PAS', 'Pasión de Cristo'), ('PRD', 'Perdón Divino'), ('PRC', 'Persecución Cristiana'), ('PRV', 'Perseverancia'), ('REP', 'Reprensión del Señor'), ('RES', 'Restauración de la Iglesia'), ('SAL', 'Salmos'), ('SND', 'Sanidad Divina'), ('SNC', 'Santa Cena'), ('SUP', 'Súplica')], default='ADO', max_length=3, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Transcriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Hymn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('release_date', models.DateField()),
                ('pdf_file', models.FileField(upload_to='hymnbook/pdf-files/')),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('arrangers', models.ManyToManyField(blank=True, related_name='hymns', to='hymnbook.arranger')),
                ('authors', models.ManyToManyField(blank=True, related_name='hymns', to='hymnbook.author')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hymns', to='hymnbook.language')),
                ('topics', models.ManyToManyField(related_name='hymns', to='hymnbook.topic')),
                ('transcribers', models.ManyToManyField(blank=True, related_name='hymns', to='hymnbook.transcriber')),
                ('translators', models.ManyToManyField(blank=True, related_name='hymns', to='hymnbook.translator')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hymn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to='hymnbook.hymn')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voice_type', models.CharField(choices=[('S0', 'Soprano'), ('S1', 'Soprano 1'), ('S2', 'Soprano 2'), ('A0', 'Alto'), ('A1', 'Alto 1'), ('A2', 'Alto 2'), ('T0', 'Tenor'), ('T1', 'Tenor 1'), ('T2', 'Tenor 2'), ('B0', 'Bajo'), ('B1', 'Bajo 1'), ('B2', 'Bajo 2'), ('I0', 'Solista'), ('I1', 'Solista 1'), ('I2', 'Solista 2'), ('EV', 'SATB')], default='S0', max_length=2)),
                ('audio_file', models.FileField(upload_to='hymnbook/audio-files/')),
                ('hymn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audio_files', to='hymnbook.hymn')),
            ],
        ),
    ]
