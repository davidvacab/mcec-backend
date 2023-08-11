from django.utils.translation import gettext_lazy as _

def jsonToTuppleList(json_data: list, search_key_1: str, search_key_2: str):
    results = []
    for dict_object in json_data:
        for key, value in dict_object.items():
            if key == search_key_1:
                value_1 = value
            elif key == search_key_2:
                value_2 = value
        results.append((value_1, value_2))
    return results

language_list = [
  { "key": "aa", "name": _("Afar" ) },
  { "key": "ab", "name": _("Abkhazian" ) },
  { "key": "ae", "name": _("Avestan" ) },
  { "key": "af", "name": _("Afrikaans" ) },
  { "key": "ak", "name": _("Akan" ) },
  { "key": "am", "name": _("Amharic" ) },
  { "key": "an", "name": _("Aragonese" ) },
  { "key": "ar", "name": _("Arabic" ) },
  { "key": "as", "name": _("Assamese" ) },
  { "key": "av", "name": _("Avaric" ) },
  { "key": "ay", "name": _("Aymara" ) },
  { "key": "az", "name": _("Azerbaijani" ) },
  { "key": "ba", "name": _("Bashkir" ) },
  { "key": "be", "name": _("Belarusian" ) },
  { "key": "bg", "name": _("Bulgarian" ) },
  { "key": "bh", "name": _("Bihari languages" ) },
  { "key": "bi", "name": _("Bislama" ) },
  { "key": "bm", "name": _("Bambara" ) },
  { "key": "bn", "name": _("Bengali" ) },
  { "key": "bo", "name": _("Tibetan" ) },
  { "key": "br", "name": _("Breton" ) },
  { "key": "bs", "name": _("Bosnian" ) },
  { "key": "ca", "name": _("Catalan; Valencian" ) },
  { "key": "ce", "name": _("Chechen" ) },
  { "key": "ch", "name": _("Chamorro" ) },
  { "key": "co", "name": _("Corsican" ) },
  { "key": "cr", "name": _("Cree" ) },
  { "key": "cs", "name": _("Czech" ) },
  { "key": "cu", "name": _("Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic" ) },
  { "key": "cv", "name": _("Chuvash" ) },
  { "key": "cy", "name": _("Welsh" ) },
  { "key": "da", "name": _("Danish" ) },
  { "key": "de", "name": _("German") },
  { "key": "dv", "name": _("Divehi; Dhivehi; Maldivian" ) },
  { "key": "dz", "name": _("Dzongkha" ) },
  { "key": "ee", "name": _("Ewe" ) },
  { "key": "el", "name": _("Greek, Modern (1453-)" ) },
  { "key": "en", "name": _("English") },
  { "key": "eo", "name": _("Esperanto" ) },
  { "key": "es", "name": _("Spanish") },
  { "key": "et", "name": _("Estonian" ) },
  { "key": "eu", "name": _("Basque" ) },
  { "key": "fa", "name": _("Persian" ) },
  { "key": "ff", "name": _("Fulah" ) },
  { "key": "fi", "name": _("Finnish" ) },
  { "key": "fj", "name": _("Fijian" ) },
  { "key": "fo", "name": _("Faroese" ) },
  { "key": "fr", "name": _("French") },
  { "key": "fy", "name": _("Western Frisian" ) },
  { "key": "ga", "name": _("Irish" ) },
  { "key": "gd", "name": _("Gaelic; Scomttish Gaelic" ) },
  { "key": "gl", "name": _("Galician" ) },
  { "key": "gn", "name": _("Guarani" ) },
  { "key": "gu", "name": _("Gujarati" ) },
  { "key": "gv", "name": _("Manx" ) },
  { "key": "ha", "name": _("Hausa" ) },
  { "key": "he", "name": _("Hebrew" ) },
  { "key": "hi", "name": _("Hindi" ) },
  { "key": "ho", "name": _("Hiri Motu" ) },
  { "key": "hr", "name": _("Croatian" ) },
  { "key": "ht", "name": _("Haitian; Haitian Creole" ) },
  { "key": "hu", "name": _("Hungarian" ) },
  { "key": "hy", "name": _("Armenian" ) },
  { "key": "hz", "name": _("Herero" ) },
  { "key": "ia", "name": _("Interlingua (International Auxiliary Language Association)") },
  { "key": "id", "name": _("Indonesian" ) },
  { "key": "ie", "name": _("Interlingue; Occidental" ) },
  { "key": "ig", "name": _("Igbo" ) },
  { "key": "ii", "name": _("Sichuan Yi; Nuosu" ) },
  { "key": "ik", "name": _("Inupiaq" ) },
  { "key": "io", "name": _("Ido" ) },
  { "key": "is", "name": _("Icelandic" ) },
  { "key": "it", "name": _("Italian" ) },
  { "key": "iu", "name": _("Inuktitut" ) },
  { "key": "ja", "name": _("Japanese" ) },
  { "key": "jv", "name": _("Javanese" ) },
  { "key": "ka", "name": _("Georgian" ) },
  { "key": "kg", "name": _("Kongo" ) },
  { "key": "ki", "name": _("Kikuyu; Gikuyu" ) },
  { "key": "kj", "name": _("Kuanyama; Kwanyama" ) },
  { "key": "kk", "name": _("Kazakh" ) },
  { "key": "kl", "name": _("Kalaallisut; Greenlandic" ) },
  { "key": "km", "name": _("Central Khmer" ) },
  { "key": "kn", "name": _("Kannada" ) },
  { "key": "ko", "name": _("Korean" ) },
  { "key": "kr", "name": _("Kanuri" ) },
  { "key": "ks", "name": _("Kashmiri" ) },
  { "key": "ku", "name": _("Kurdish" ) },
  { "key": "kv", "name": _("Komi" ) },
  { "key": "kw", "name": _("Cornish" ) },
  { "key": "ky", "name": _("Kirghiz; Kyrgyz" ) },
  { "key": "la", "name": _("Latin" ) },
  { "key": "lb", "name": _("Luxembourgish; Letzeburgesch" ) },
  { "key": "lg", "name": _("Ganda" ) },
  { "key": "li", "name": _("Limburgan; Limburger; Limburgish" ) },
  { "key": "ln", "name": _("Lingala" ) },
  { "key": "lo", "name": _("Lao" ) },
  { "key": "lt", "name": _("Lithuanian" ) },
  { "key": "lu", "name": _("Luba-Katanga" ) },
  { "key": "lv", "name": _("Latvian" ) },
  { "key": "mg", "name": _("Malagasy" ) },
  { "key": "mh", "name": _("Marshallese" ) },
  { "key": "mi", "name": _("Maori" ) },
  { "key": "mk", "name": _("Macedonian" ) },
  { "key": "ml", "name": _("Malayalam" ) },
  { "key": "mn", "name": _("Mongolian" ) },
  { "key": "mr", "name": _("Marathi" ) },
  { "key": "ms", "name": _("Malay" ) },
  { "key": "mt", "name": _("Maltese" ) },
  { "key": "my", "name": _("Burmese" ) },
  { "key": "na", "name": _("Nauru" ) },
  { "key": "nb", "name": _("Bokmål, Norwegian; Norwegian Bokmål") },
  { "key": "nd", "name": _("Ndebele, North; North Ndebele" ) },
  { "key": "ne", "name": _("Nepali" ) },
  { "key": "ng", "name": _("Ndonga" ) },
  { "key": "nl", "name": _("Dutch; Flemish" ) },
  { "key": "nn", "name": _("Norwegian Nynorsk; Nynorsk, Norwegian" ) },
  { "key": "no", "name": _("Norwegian" ) },
  { "key": "nr", "name": _("Ndebele, South; South Ndebele" ) },
  { "key": "nv", "name": _("Navajo; Navaho" ) },
  { "key": "ny", "name": _("Chichewa; Chewa; Nyanja" ) },
  { "key": "oc", "name": _("Occitan (post 1500)" ) },
  { "key": "oj", "name": _("Ojibwa" ) },
  { "key": "om", "name": _("Oromo" ) },
  { "key": "or", "name": _("Oriya" ) },
  { "key": "os", "name": _("Ossetian; Ossetic" ) },
  { "key": "pa", "name": _("Panjabi; Punjabi" ) },
  { "key": "pi", "name": _("Pali" ) },
  { "key": "pl", "name": _("Polish" ) },
  { "key": "ps", "name": _("Pushto; Pashto" ) },
  { "key": "pt", "name": _("Portuguese" ) },
  { "key": "qu", "name": _("Quechua" ) },
  { "key": "rm", "name": _("Romansh" ) },
  { "key": "rn", "name": _("Rundi" ) },
  { "key": "ro", "name": _("Romanian; Moldavian; Moldovan" ) },
  { "key": "ru", "name": _("Russian" ) },
  { "key": "rw", "name": _("Kinyarwanda" ) },
  { "key": "sa", "name": _("Sanskrit" ) },
  { "key": "sc", "name": _("Sardinian" ) },
  { "key": "sd", "name": _("Sindhi" ) },
  { "key": "se", "name": _("Northern Sami" ) },
  { "key": "sg", "name": _("Sango" ) },
  { "key": "si", "name": _("Sinhala; Sinhalese" ) },
  { "key": "sk", "name": _("Slovak" ) },
  { "key": "sl", "name": _("Slovenian" ) },
  { "key": "sm", "name": _("Samoan" ) },
  { "key": "sn", "name": _("Shona" ) },
  { "key": "so", "name": _("Somali" ) },
  { "key": "sq", "name": _("Albanian" ) },
  { "key": "sr", "name": _("Serbian" ) },
  { "key": "ss", "name": _("Swati" ) },
  { "key": "st", "name": _("Sotho, Southern" ) },
  { "key": "su", "name": _("Sundanese" ) },
  { "key": "sv", "name": _("Swedish" ) },
  { "key": "sw", "name": _("Swahili" ) },
  { "key": "ta", "name": _("Tamil" ) },
  { "key": "te", "name": _("Telugu" ) },
  { "key": "tg", "name": _("Tajik" ) },
  { "key": "th", "name": _("Thai" ) },
  { "key": "ti", "name": _("Tigrinya" ) },
  { "key": "tk", "name": _("Turkmen" ) },
  { "key": "tl", "name": _("Tagalog" ) },
  { "key": "tn", "name": _("Tswana" ) },
  { "key": "to", "name": _("Tonga (Tonga Islands)" ) },
  { "key": "tr", "name": _("Turkish" ) },
  { "key": "ts", "name": _("Tsonga" ) },
  { "key": "tt", "name": _("Tatar" ) },
  { "key": "tw", "name": _("Twi" ) },
  { "key": "ty", "name": _("Tahitian" ) },
  { "key": "ug", "name": _("Uighur; Uyghur" ) },
  { "key": "uk", "name": _("Ukrainian" ) },
  { "key": "ur", "name": _("Urdu" ) },
  { "key": "uz", "name": _("Uzbek" ) },
  { "key": "ve", "name": _("Venda" ) },
  { "key": "vi", "name": _("Vietnamese" ) },
  { "key": "vo", "name": _("Volapük" ) },
  { "key": "wa", "name": _("Walloon" ) },
  { "key": "wo", "name": _("Wolof" ) },
  { "key": "xh", "name": _("Xhosa" ) },
  { "key": "yi", "name": _("Yiddish" ) },
  { "key": "yo", "name": _("Yoruba" ) },
  { "key": "za", "name": _("Zhuang; Chuang" ) },
  { "key": "zh", "name": _("Chinese" ) },
  { "key": "zu", "name": _("Zulu" ) }
]

audio_voice_type_list = [
  { "key": "S0", "value": "Soprano" },
  { "key": "S1", "value": "Soprano 1" },
  { "key": "S2", "value": "Soprano 2" },
  { "key": "A0", "value": "Alto" },
  { "key": "A1", "value": "Alto 1" },
  { "key": "A2", "value": "Alto 2" },
  { "key": "T0", "value": "Tenor" },
  { "key": "T1", "value": "Tenor 1" },
  { "key": "T2", "value": "Tenor 2" },
  { "key": "B0", "value": _("Bass") },
  { "key": "B1", "value": f'{_("Bass")} {"1"}' },
  { "key": "B2", "value": f'{_("Bass")} {"2"}' },
  { "key": "I0", "value": _("Solo") },
  { "key": "I1", "value": f'{_("Solo")} {"1"}' },
  { "key": "I2", "value": f'{_("Solo")} {"2"}' },
  { "key": "EV", "value": "SATB" },
]

topic_list = [
  {"key": "ADO", "value": _("Worship") },
  {"key": "ADV", "value": _("Advent of the Lord") },
  {"key": "ALB", "value": _("Praise") },
  {"key": "AMA", "value": _("Dawn") },
  {"key": "AMO", "value": _("Love") },
  {"key": "ANN", "value": _("New Year") },
  {"key": "BAU", "value": _("Baptism") },
  {"key": "BNV", "value": _("Welcoming") },
  {"key": "COM", "value": _("Communion") },
  {"key": "CNF", "value": _("Trust") },
  {"key": "CNG", "value": _("Consecration") },
  {"key": "DES", "value": _("Farewell") },
  {"key": "DUE", "value": _("Rest in the Lord") },
  {"key": "ELE", "value": _("Election") },
  {"key": "ESP", "value": _("Hope") },
  {"key": "EVA", "value": _("Evangelization") },
  {"key": "EXH", "value": _("Exhortation") },
  {"key": "GLO", "value": _("Glory") },
  {"key": "GOZ", "value": _("Joy") },
  {"key": "GRC", "value": _("Grace") },
  {"key": "GRT", "value": _("Gratitud") },
  {"key": "HON", "value": _("Honor") },
  {"key": "ING", "value": _("Inauguration") },
  {"key": "INT", "value": _("Intercession") },
  {"key": "INV", "value": _("Invitation") },
  {"key": "JUV", "value": _("Youth") },
  {"key": "LIB", "value": _("Liberality") },
  {"key": "LCH", "value": _("Battle") },
  {"key": "MAT", "value": _("Marriage") },
  {"key": "OBR", "value": _("Labor") },
  {"key": "ORA", "value": _("Prayer") },
  {"key": "OAP", "value": _("Apostolic Prayer") },
  {"key": "PAS", "value": _("Passion") },
  {"key": "PET", "value": _("Petition") },
  {"key": "RST", "value": _("Restoration") },
  {"key": "RSU", "value": _("Resurrection") },
  {"key": "SNC", "value": _("Holy Supper") },
]

LANGUAGES = jsonToTuppleList(language_list, 'key', 'name')

AUDIO_VOICE_TYPES = jsonToTuppleList(audio_voice_type_list, 'key', 'value')

TOPICS = jsonToTuppleList(topic_list, 'key', 'value')