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

country_list = [
  {
    "code": "AD",
    "name": "Andorra",
    "native": "Andorra",
    "phone": "+376",
    "continent": "EU",
    "capital": "Andorra la Vella",
    "currency": ["EUR"],
    "languages": ["ca"]
  },
  {
    "code": "AE",
    "name": "United Arab Emirates",
    "native": "دولة الإمارات العربية المتحدة",
    "phone": "+971",
    "continent": "AS",
    "capital": "Abu Dhabi",
    "currency": ["AED"],
    "languages": ["ar"]
  },
  {
    "code": "AF",
    "name": "Afghanistan",
    "native": "افغانستان",
    "phone": "+93",
    "continent": "AS",
    "capital": "Kabul",
    "currency": ["AFN"],
    "languages": ["ps", "uz", "tk"]
  },
  {
    "code": "AG",
    "name": "Antigua and Barbuda",
    "native": "Antigua and Barbuda",
    "phone": "+1268",
    "continent": "NA",
    "capital": "Saint John's",
    "currency": ["XCD"],
    "languages": ["en"]
  },
  {
    "code": "AI",
    "name": "Anguilla",
    "native": "Anguilla",
    "phone": "+1264",
    "continent": "NA",
    "capital": "The Valley",
    "currency": ["XCD"],
    "languages": ["en"]
  },
  {
    "code": "AL",
    "name": "Albania",
    "native": "Shqipëria",
    "phone": "+355",
    "continent": "EU",
    "capital": "Tirana",
    "currency": ["ALL"],
    "languages": ["sq"]
  },
  {
    "code": "AM",
    "name": "Armenia",
    "native": "Հայաստան",
    "phone": "+374",
    "continent": "AS",
    "capital": "Yerevan",
    "currency": ["AMD"],
    "languages": ["hy", "ru"]
  },
  {
    "code": "AO",
    "name": "Angola",
    "native": "Angola",
    "phone": "+244",
    "continent": "AF",
    "capital": "Luanda",
    "currency": ["AOA"],
    "languages": ["pt"]
  },
  {
    "code": "AQ",
    "name": "Antarctica",
    "native": "Antarctica",
    "phone": "+672",
    "continent": "AN",
    "capital": "",
    "currency": [],
    "languages": []
  },
  {
    "code": "AR",
    "name": "Argentina",
    "native": "Argentina",
    "phone": "+54",
    "continent": "SA",
    "capital": "Buenos Aires",
    "currency": ["ARS"],
    "languages": ["es", "gn"]
  },
  {
    "code": "AS",
    "name": "American Samoa",
    "native": "American Samoa",
    "phone": "+1684",
    "continent": "OC",
    "capital": "Pago Pago",
    "currency": ["USD"],
    "languages": ["en", "sm"]
  },
  {
    "code": "AT",
    "name": "Austria",
    "native": "Österreich",
    "phone": "+43",
    "continent": "EU",
    "capital": "Vienna",
    "currency": ["EUR"],
    "languages": ["de"]
  },
  {
    "code": "AU",
    "name": "Australia",
    "native": "Australia",
    "phone": "+61",
    "continent": "OC",
    "capital": "Canberra",
    "currency": ["AUD"],
    "languages": ["en"]
  },
  {
    "code": "AW",
    "name": "Aruba",
    "native": "Aruba",
    "phone": "+297",
    "continent": "NA",
    "capital": "Oranjestad",
    "currency": ["AWG"],
    "languages": ["nl", "pa"]
  },
  {
    "code": "AX",
    "name": "Aland",
    "native": "Åland",
    "phone": "+358",
    "continent": "EU",
    "capital": "Mariehamn",
    "currency": ["EUR"],
    "languages": ["sv"]
  },
  {
    "code": "AZ",
    "name": "Azerbaijan",
    "native": "Azərbaycan",
    "phone": "+994",
    "continent": "AS",
    "continents": ["AS", "EU"],
    "capital": "Baku",
    "currency": ["AZN"],
    "languages": ["az"]
  },
  {
    "code": "BA",
    "name": "Bosnia and Herzegovina",
    "native": "Bosna i Hercegovina",
    "phone": "+387",
    "continent": "EU",
    "capital": "Sarajevo",
    "currency": ["BAM"],
    "languages": ["bs", "hr", "sr"]
  },
  {
    "code": "BB",
    "name": "Barbados",
    "native": "Barbados",
    "phone": "+1246",
    "continent": "NA",
    "capital": "Bridgetown",
    "currency": ["BBD"],
    "languages": ["en"]
  },
  {
    "code": "BD",
    "name": "Bangladesh",
    "native": "Bangladesh",
    "phone": "+880",
    "continent": "AS",
    "capital": "Dhaka",
    "currency": ["BDT"],
    "languages": ["bn"]
  },
  {
    "code": "BE",
    "name": "Belgium",
    "native": "België",
    "phone": "+32",
    "continent": "EU",
    "capital": "Brussels",
    "currency": ["EUR"],
    "languages": ["nl", "fr", "de"]
  },
  {
    "code": "BF",
    "name": "Burkina Faso",
    "native": "Burkina Faso",
    "phone": "+226",
    "continent": "AF",
    "capital": "Ouagadougou",
    "currency": ["XOF"],
    "languages": ["fr", "ff"]
  },
  {
    "code": "BG",
    "name": "Bulgaria",
    "native": "България",
    "phone": "+359",
    "continent": "EU",
    "capital": "Sofia",
    "currency": ["BGN"],
    "languages": ["bg"]
  },
  {
    "code": "BH",
    "name": "Bahrain",
    "native": "‏البحرين",
    "phone": "+973",
    "continent": "AS",
    "capital": "Manama",
    "currency": ["BHD"],
    "languages": ["ar"]
  },
  {
    "code": "BI",
    "name": "Burundi",
    "native": "Burundi",
    "phone": "+257",
    "continent": "AF",
    "capital": "Bujumbura",
    "currency": ["BIF"],
    "languages": ["fr", "rn"]
  },
  {
    "code": "BJ",
    "name": "Benin",
    "native": "Bénin",
    "phone": "+229",
    "continent": "AF",
    "capital": "Porto-Novo",
    "currency": ["XOF"],
    "languages": ["fr"]
  },
  {
    "code": "BL",
    "name": "Saint Barthelemy",
    "native": "Saint-Barthélemy",
    "phone": "+590",
    "continent": "NA",
    "capital": "Gustavia",
    "currency": ["EUR"],
    "languages": ["fr"]
  },
  {
    "code": "BM",
    "name": "Bermuda",
    "native": "Bermuda",
    "phone": "+1441",
    "continent": "NA",
    "capital": "Hamilton",
    "currency": ["BMD"],
    "languages": ["en"]
  },
  {
    "code": "BN",
    "name": "Brunei",
    "native": "Negara Brunei Darussalam",
    "phone": "+673",
    "continent": "AS",
    "capital": "Bandar Seri Begawan",
    "currency": ["BND"],
    "languages": ["ms"]
  },
  {
    "code": "BO",
    "name": "Bolivia",
    "native": "Bolivia",
    "phone": "+591",
    "continent": "SA",
    "capital": "Sucre",
    "currency": ["BOB", "BOV"],
    "languages": ["es", "ay", "qu"]
  },
  {
    "code": "BQ",
    "name": "Bonaire",
    "native": "Bonaire",
    "phone": "+5997",
    "continent": "NA",
    "capital": "Kralendijk",
    "currency": ["USD"],
    "languages": ["nl"]
  },
  {
    "code": "BR",
    "name": "Brazil",
    "native": "Brasil",
    "phone": "+55",
    "continent": "SA",
    "capital": "Brasília",
    "currency": ["BRL"],
    "languages": ["pt"]
  },
  {
    "code": "BS",
    "name": "Bahamas",
    "native": "Bahamas",
    "phone": "+1242",
    "continent": "NA",
    "capital": "Nassau",
    "currency": ["BSD"],
    "languages": ["en"]
  },
  {
    "code": "BT",
    "name": "Bhutan",
    "native": "ʼbrug-yul",
    "phone": "+975",
    "continent": "AS",
    "capital": "Thimphu",
    "currency": ["BTN", "INR"],
    "languages": ["dz"]
  },
  {
    "code": "BV",
    "name": "Bouvet Island",
    "native": "Bouvetøya",
    "phone": "+47",
    "continent": "AN",
    "capital": "",
    "currency": ["NOK"],
    "languages": ["no", "nb", "nn"]
  },
  {
    "code": "BW",
    "name": "Botswana",
    "native": "Botswana",
    "phone": "+267",
    "continent": "AF",
    "capital": "Gaborone",
    "currency": ["BWP"],
    "languages": ["en", "tn"]
  },
  {
    "code": "BY",
    "name": "Belarus",
    "native": "Белару́сь",
    "phone": "+375",
    "continent": "EU",
    "capital": "Minsk",
    "currency": ["BYN"],
    "languages": ["be", "ru"]
  },
  {
    "code": "BZ",
    "name": "Belize",
    "native": "Belize",
    "phone": "+501",
    "continent": "NA",
    "capital": "Belmopan",
    "currency": ["BZD"],
    "languages": ["en", "es"]
  },
  {
    "code": "CA",
    "name": "Canada",
    "native": "Canada",
    "phone": "+1",
    "continent": "NA",
    "capital": "Ottawa",
    "currency": ["CAD"],
    "languages": ["en", "fr"]
  },
  {
    "code": "CC",
    "name": "Cocos (Keeling) Islands",
    "native": "Cocos (Keeling) Islands",
    "phone": "+61",
    "continent": "AS",
    "capital": "West Island",
    "currency": ["AUD"],
    "languages": ["en"]
  },
  {
    "code": "CD",
    "name": "Democratic Republic of the Congo",
    "native": "République démocratique du Congo",
    "phone": "+243",
    "continent": "AF",
    "capital": "Kinshasa",
    "currency": ["CDF"],
    "languages": ["fr", "ln", "kg", "sw", "lu"]
  },
  {
    "code": "CF",
    "name": "Central African Republic",
    "native": "Ködörösêse tî Bêafrîka",
    "phone": "+236",
    "continent": "AF",
    "capital": "Bangui",
    "currency": ["XAF"],
    "languages": ["fr", "sg"]
  },
  {
    "code": "CG",
    "name": "Republic of the Congo",
    "native": "République du Congo",
    "phone": "+242",
    "continent": "AF",
    "capital": "Brazzaville",
    "currency": ["XAF"],
    "languages": ["fr", "ln"]
  },
  {
    "code": "CH",
    "name": "Switzerland",
    "native": "Schweiz",
    "phone": "+41",
    "continent": "EU",
    "capital": "Bern",
    "currency": ["CHE", "CHF", "CHW"],
    "languages": ["de", "fr", "it"]
  },
  {
    "code": "CI",
    "name": "Ivory Coast",
    "native": "Côte d'Ivoire",
    "phone": "+225",
    "continent": "AF",
    "capital": "Yamoussoukro",
    "currency": ["XOF"],
    "languages": ["fr"]
  },
  {
    "code": "CK",
    "name": "Cook Islands",
    "native": "Cook Islands",
    "phone": "+682",
    "continent": "OC",
    "capital": "Avarua",
    "currency": ["NZD"],
    "languages": ["en"]
  },
  {
    "code": "CL",
    "name": "Chile",
    "native": "Chile",
    "phone": "+56",
    "continent": "SA",
    "capital": "Santiago",
    "currency": ["CLF", "CLP"],
    "languages": ["es"]
  },
  {
    "code": "CM",
    "name": "Cameroon",
    "native": "Cameroon",
    "phone": "+237",
    "continent": "AF",
    "capital": "Yaoundé",
    "currency": ["XAF"],
    "languages": ["en", "fr"]
  },
  {
    "code": "CN",
    "name": "China",
    "native": "中国",
    "phone": "+86",
    "continent": "AS",
    "capital": "Beijing",
    "currency": ["CNY"],
    "languages": ["zh"]
  },
  {
    "code": "CO",
    "name": "Colombia",
    "native": "Colombia",
    "phone": "+57",
    "continent": "SA",
    "capital": "Bogotá",
    "currency": ["COP"],
    "languages": ["es"]
  },
  {
    "code": "CR",
    "name": "Costa Rica",
    "native": "Costa Rica",
    "phone": "+506",
    "continent": "NA",
    "capital": "San José",
    "currency": ["CRC"],
    "languages": ["es"]
  },
  {
    "code": "CU",
    "name": "Cuba",
    "native": "Cuba",
    "phone": "+53",
    "continent": "NA",
    "capital": "Havana",
    "currency": ["CUC", "CUP"],
    "languages": ["es"]
  },
  {
    "code": "CV",
    "name": "Cape Verde",
    "native": "Cabo Verde",
    "phone": "+238",
    "continent": "AF",
    "capital": "Praia",
    "currency": ["CVE"],
    "languages": ["pt"]
  },
  {
    "code": "CW",
    "name": "Curacao",
    "native": "Curaçao",
    "phone": "+5999",
    "continent": "NA",
    "capital": "Willemstad",
    "currency": ["ANG"],
    "languages": ["nl", "pa", "en"]
  },
  {
    "code": "CX",
    "name": "Christmas Island",
    "native": "Christmas Island",
    "phone": "+61",
    "continent": "AS",
    "capital": "Flying Fish Cove",
    "currency": ["AUD"],
    "languages": ["en"]
  },
  {
    "code": "CY",
    "name": "Cyprus",
    "native": "Κύπρος",
    "phone": "+357",
    "continent": "EU",
    "capital": "Nicosia",
    "currency": ["EUR"],
    "languages": ["el", "tr", "hy"]
  },
  {
    "code": "CZ",
    "name": "Czech Republic",
    "native": "Česká republika",
    "phone": "+420",
    "continent": "EU",
    "capital": "Prague",
    "currency": ["CZK"],
    "languages": ["cs"]
  },
  {
    "code": "DE",
    "name": "Germany",
    "native": "Deutschland",
    "phone": "+49",
    "continent": "EU",
    "capital": "Berlin",
    "currency": ["EUR"],
    "languages": ["de"]
  },
  {
    "code": "DJ",
    "name": "Djibouti",
    "native": "Djibouti",
    "phone": "+253",
    "continent": "AF",
    "capital": "Djibouti",
    "currency": ["DJF"],
    "languages": ["fr", "ar"]
  },
  {
    "code": "DK",
    "name": "Denmark",
    "native": "Danmark",
    "phone": "+45",
    "continent": "EU",
    "continents": ["EU", "NA"],
    "capital": "Copenhagen",
    "currency": ["DKK"],
    "languages": ["da"]
  },
  {
    "code": "DM",
    "name": "Dominica",
    "native": "Dominica",
    "phone": "+1767",
    "continent": "NA",
    "capital": "Roseau",
    "currency": ["XCD"],
    "languages": ["en"]
  },
  {
    "code": "DO",
    "name": "Dominican Republic",
    "native": "República Dominicana",
    "phone": "+1809",
    "continent": "NA",
    "capital": "Santo Domingo",
    "currency": ["DOP"],
    "languages": ["es"]
  },
  {
    "code": "DZ",
    "name": "Algeria",
    "native": "الجزائر",
    "phone": "+213",
    "continent": "AF",
    "capital": "Algiers",
    "currency": ["DZD"],
    "languages": ["ar"]
  },
  {
    "code": "EC",
    "name": "Ecuador",
    "native": "Ecuador",
    "phone": "+593",
    "continent": "SA",
    "capital": "Quito",
    "currency": ["USD"],
    "languages": ["es"]
  },
  {
    "code": "EE",
    "name": "Estonia",
    "native": "Eesti",
    "phone": "+372",
    "continent": "EU",
    "capital": "Tallinn",
    "currency": ["EUR"],
    "languages": ["et"]
  },
  {
    "code": "EG",
    "name": "Egypt",
    "native": "مصر‎",
    "phone": "+20",
    "continent": "AF",
    "continents": ["AF", "AS"],
    "capital": "Cairo",
    "currency": ["EGP"],
    "languages": ["ar"]
  },
  {
    "code": "EH",
    "name": "Western Sahara",
    "native": "الصحراء الغربية",
    "phone": "+212",
    "continent": "AF",
    "capital": "El Aaiún",
    "currency": ["MAD", "DZD", "MRU"],
    "languages": ["es"]
  },
  {
    "code": "ER",
    "name": "Eritrea",
    "native": "ኤርትራ",
    "phone": "+291",
    "continent": "AF",
    "capital": "Asmara",
    "currency": ["ERN"],
    "languages": ["ti", "ar", "en"]
  },
  {
    "code": "ES",
    "name": "Spain",
    "native": "España",
    "phone": "+34",
    "continent": "EU",
    "capital": "Madrid",
    "currency": ["EUR"],
    "languages": ["es", "eu", "ca", "gl", "oc"]
  },
  {
    "code": "ET",
    "name": "Ethiopia",
    "native": "ኢትዮጵያ",
    "phone": "+251",
    "continent": "AF",
    "capital": "Addis Ababa",
    "currency": ["ETB"],
    "languages": ["am"]
  },
  {
    "code": "FI",
    "name": "Finland",
    "native": "Suomi",
    "phone": "+358",
    "continent": "EU",
    "capital": "Helsinki",
    "currency": ["EUR"],
    "languages": ["fi", "sv"]
  },
  {
    "code": "FJ",
    "name": "Fiji",
    "native": "Fiji",
    "phone": "+679",
    "continent": "OC",
    "capital": "Suva",
    "currency": ["FJD"],
    "languages": ["en", "fj", "hi", "ur"]
  },
  {
    "code": "FK",
    "name": "Falkland Islands",
    "native": "Falkland Islands",
    "phone": "+500",
    "continent": "SA",
    "capital": "Stanley",
    "currency": ["FKP"],
    "languages": ["en"]
  },
  {
    "code": "FM",
    "name": "Micronesia",
    "native": "Micronesia",
    "phone": "+691",
    "continent": "OC",
    "capital": "Palikir",
    "currency": ["USD"],
    "languages": ["en"]
  },
  {
    "code": "FO",
    "name": "Faroe Islands",
    "native": "Føroyar",
    "phone": "+298",
    "continent": "EU",
    "capital": "Tórshavn",
    "currency": ["DKK"],
    "languages": ["fo"]
  },
  {
    "code": "FR",
    "name": "France",
    "native": "France",
    "phone": "+33",
    "continent": "EU",
    "capital": "Paris",
    "currency": ["EUR"],
    "languages": ["fr"]
  },
  {
    "code": "GA",
    "name": "Gabon",
    "native": "Gabon",
    "phone": "+241",
    "continent": "AF",
    "capital": "Libreville",
    "currency": ["XAF"],
    "languages": ["fr"]
  },
  {
    "code": "GB",
    "name": "United Kingdom",
    "native": "United Kingdom",
    "phone": "+44",
    "continent": "EU",
    "capital": "London",
    "currency": ["GBP"],
    "languages": ["en"]
  },
  {
    "code": "GD",
    "name": "Grenada",
    "native": "Grenada",
    "phone": "+1473",
    "continent": "NA",
    "capital": "St. George's",
    "currency": ["XCD"],
    "languages": ["en"]
  },
  {
    "code": "GE",
    "name": "Georgia",
    "native": "საქართველო",
    "phone": "+995",
    "continent": "AS",
    "continents": ["AS", "EU"],
    "capital": "Tbilisi",
    "currency": ["GEL"],
    "languages": ["ka"]
  },
  {
    "code": "GF",
    "name": "French Guiana",
    "native": "Guyane française",
    "phone": "+594",
    "continent": "SA",
    "capital": "Cayenne",
    "currency": ["EUR"],
    "languages": ["fr"]
  },
  {
    "code": "GG",
    "name": "Guernsey",
    "native": "Guernsey",
    "phone": "+44",
    "continent": "EU",
    "capital": "St. Peter Port",
    "currency": ["GBP"],
    "languages": ["en", "fr"]
  },
  {
    "code": "GH",
    "name": "Ghana",
    "native": "Ghana",
    "phone": "+233",
    "continent": "AF",
    "capital": "Accra",
    "currency": ["GHS"],
    "languages": ["en"]
  },
  {
    "code": "GI",
    "name": "Gibraltar",
    "native": "Gibraltar",
    "phone": "+350",
    "continent": "EU",
    "capital": "Gibraltar",
    "currency": ["GIP"],
    "languages": ["en"]
  },
  {
    "code": "GL",
    "name": "Greenland",
    "native": "Kalaallit Nunaat",
    "phone": "+299",
    "continent": "NA",
    "capital": "Nuuk",
    "currency": ["DKK"],
    "languages": ["kl"]
  },
  {
    "code": "GM",
    "name": "Gambia",
    "native": "Gambia",
    "phone": "+220",
    "continent": "AF",
    "capital": "Banjul",
    "currency": ["GMD"],
    "languages": ["en"]
  },
  {
    "code": "GN",
    "name": "Guinea",
    "native": "Guinée",
    "phone": "+224",
    "continent": "AF",
    "capital": "Conakry",
    "currency": ["GNF"],
    "languages": ["fr", "ff"]
  },
  {
    "code": "GP",
    "name": "Guadeloupe",
    "native": "Guadeloupe",
    "phone": "+590",
    "continent": "NA",
    "capital": "Basse-Terre",
    "currency": ["EUR"],
    "languages": ["fr"]
  },
  {
    "code": "GQ",
    "name": "Equatorial Guinea",
    "native": "Guinea Ecuatorial",
    "phone": "+240",
    "continent": "AF",
    "capital": "Malabo",
    "currency": ["XAF"],
    "languages": ["es", "fr"]
  },
  {
    "code": "GR",
    "name": "Greece",
    "native": "Ελλάδα",
    "phone": "+30",
    "continent": "EU",
    "capital": "Athens",
    "currency": ["EUR"],
    "languages": ["el"]
  },
  {
    "code": "GS",
    "name": "South Georgia and the South Sandwich Islands",
    "native": "South Georgia",
    "phone": "+500",
    "continent": "AN",
    "capital": "King Edward Point",
    "currency": ["GBP"],
    "languages": ["en"]
  },
  {
    "code": "GT",
    "name": "Guatemala",
    "native": "Guatemala",
    "phone": "+502",
    "continent": "NA",
    "capital": "Guatemala City",
    "currency": ["GTQ"],
    "languages": ["es"]
  },
  {
    "code": "GU",
    "name": "Guam",
    "native": "Guam",
    "phone": "+1671",
    "continent": "OC",
    "capital": "Hagåtña",
    "currency": ["USD"],
    "languages": ["en", "ch", "es"]
  },
  {
    "code": "GW",
    "name": "Guinea-Bissau",
    "native": "Guiné-Bissau",
    "phone": "+245",
    "continent": "AF",
    "capital": "Bissau",
    "currency": ["XOF"],
    "languages": ["pt"]
  },
  {
    "code": "GY",
    "name": "Guyana",
    "native": "Guyana",
    "phone": "+592",
    "continent": "SA",
    "capital": "Georgetown",
    "currency": ["GYD"],
    "languages": ["en"]
  },
  {
    "code": "HK",
    "name": "Hong Kong",
    "native": "香港",
    "phone": "+852",
    "continent": "AS",
    "capital": "City of Victoria",
    "currency": ["HKD"],
    "languages": ["zh", "en"]
  },
  {
    "code": "HM",
    "name": "Heard Island and McDonald Islands",
    "native": "Heard Island and McDonald Islands",
    "phone": "+61",
    "continent": "AN",
    "capital": "",
    "currency": ["AUD"],
    "languages": ["en"]
  },
  {
    "code": "HN",
    "name": "Honduras",
    "native": "Honduras",
    "phone": "+504",
    "continent": "NA",
    "capital": "Tegucigalpa",
    "currency": ["HNL"],
    "languages": ["es"]
  },
  {
    "code": "HR",
    "name": "Croatia",
    "native": "Hrvatska",
    "phone": "+385",
    "continent": "EU",
    "capital": "Zagreb",
    "currency": ["EUR"],
    "languages": ["hr"]
  },
  {
    "code": "HT",
    "name": "Haiti",
    "native": "Haïti",
    "phone": "+509",
    "continent": "NA",
    "capital": "Port-au-Prince",
    "currency": ["HTG", "USD"],
    "languages": ["fr", "ht"]
  },
  {
    "code": "HU",
    "name": "Hungary",
    "native": "Magyarország",
    "phone": "+36",
    "continent": "EU",
    "capital": "Budapest",
    "currency": ["HUF"],
    "languages": ["hu"]
  },
  {
    "code": "ID",
    "name": "Indonesia",
    "native": "Indonesia",
    "phone": "+62",
    "continent": "AS",
    "capital": "Jakarta",
    "currency": ["IDR"],
    "languages": ["id"]
  },
  {
    "code": "IE",
    "name": "Ireland",
    "native": "Éire",
    "phone": "+353",
    "continent": "EU",
    "capital": "Dublin",
    "currency": ["EUR"],
    "languages": ["ga", "en"]
  },
  {
    "code": "IL",
    "name": "Israel",
    "native": "יִשְׂרָאֵל",
    "phone": "+972",
    "continent": "AS",
    "capital": "Jerusalem",
    "currency": ["ILS"],
    "languages": ["he", "ar"]
  },
  {
    "code": "IM",
    "name": "Isle of Man",
    "native": "Isle of Man",
    "phone": "+44",
    "continent": "EU",
    "capital": "Douglas",
    "currency": ["GBP"],
    "languages": ["en", "gv"]
  },
  {
    "code": "IN",
    "name": "India",
    "native": "भारत",
    "phone": "+91",
    "continent": "AS",
    "capital": "New Delhi",
    "currency": ["INR"],
    "languages": ["hi", "en"]
  },
  {
    "code": "IO",
    "name": "British Indian Ocean Territory",
    "native": "British Indian Ocean Territory",
    "phone": "+246",
    "continent": "AS",
    "capital": "Diego Garcia",
    "currency": ["USD"],
    "languages": ["en"]
  },
  {
    "code": "IQ",
    "name": "Iraq",
    "native": "العراق",
    "phone": "+964",
    "continent": "AS",
    "capital": "Baghdad",
    "currency": ["IQD"],
    "languages": ["ar", "ku"]
  },
  {
    "code": "IR",
    "name": "Iran",
    "native": "ایران",
    "phone": "+98",
    "continent": "AS",
    "capital": "Tehran",
    "currency": ["IRR"],
    "languages": ["fa"]
  },
  {
    "code": "IS",
    "name": "Iceland",
    "native": "Ísland",
    "phone": "+354",
    "continent": "EU",
    "capital": "Reykjavik",
    "currency": ["ISK"],
    "languages": ["is"]
  },
  {
    "code": "IT",
    "name": "Italy",
    "native": "Italia",
    "phone": "+39",
    "continent": "EU",
    "capital": "Rome",
    "currency": ["EUR"],
    "languages": ["it"]
  },
  {
    "code": "JE",
    "name": "Jersey",
    "native": "Jersey",
    "phone": "+44",
    "continent": "EU",
    "capital": "Saint Helier",
    "currency": ["GBP"],
    "languages": ["en", "fr"]
  },
  {
    "code": "JM",
    "name": "Jamaica",
    "native": "Jamaica",
    "phone": "+1876",
    "continent": "NA",
    "capital": "Kingston",
    "currency": ["JMD"],
    "languages": ["en"]
  },
  {
    "code": "JO",
    "name": "Jordan",
    "native": "الأردن",
    "phone": "+962",
    "continent": "AS",
    "capital": "Amman",
    "currency": ["JOD"],
    "languages": ["ar"]
  },
  {
    "code": "JP",
    "name": "Japan",
    "native": "日本",
    "phone": "+81",
    "continent": "AS",
    "capital": "Tokyo",
    "currency": ["JPY"],
    "languages": ["ja"]
  },
  {
    "code": "KE",
    "name": "Kenya",
    "native": "Kenya",
    "phone": "+254",
    "continent": "AF",
    "capital": "Nairobi",
    "currency": ["KES"],
    "languages": ["en", "sw"]
  },
  {
    "code": "KG",
    "name": "Kyrgyzstan",
    "native": "Кыргызстан",
    "phone": "+996",
    "continent": "AS",
    "capital": "Bishkek",
    "currency": ["KGS"],
    "languages": ["ky", "ru"]
  },
  {
    "code": "KH",
    "name": "Cambodia",
    "native": "Kâmpŭchéa",
    "phone": "+855",
    "continent": "AS",
    "capital": "Phnom Penh",
    "currency": ["KHR"],
    "languages": ["km"]
  },
  {
    "code": "KI",
    "name": "Kiribati",
    "native": "Kiribati",
    "phone": "+686",
    "continent": "OC",
    "capital": "South Tarawa",
    "currency": ["AUD"],
    "languages": ["en"]
  },
  {
    "code": "KM",
    "name": "Comoros",
    "native": "Komori",
    "phone": "+269",
    "continent": "AF",
    "capital": "Moroni",
    "currency": ["KMF"],
    "languages": ["ar", "fr"]
  },
  {
    "code": "KN",
    "name": "Saint Kitts and Nevis",
    "native": "Saint Kitts and Nevis",
    "phone": "+1869",
    "continent": "NA",
    "capital": "Basseterre",
    "currency": ["XCD"],
    "languages": ["en"]
  },
  {
    "code": "KP",
    "name": "North Korea",
    "native": "북한",
    "phone": "+850",
    "continent": "AS",
    "capital": "Pyongyang",
    "currency": ["KPW"],
    "languages": ["ko"]
  },
  {
    "code": "KR",
    "name": "South Korea",
    "native": "대한민국",
    "phone": "+82",
    "continent": "AS",
    "capital": "Seoul",
    "currency": ["KRW"],
    "languages": ["ko"]
  },
  {
    "code": "KW",
    "name": "Kuwait",
    "native": "الكويت",
    "phone": "+965",
    "continent": "AS",
    "capital": "Kuwait City",
    "currency": ["KWD"],
    "languages": ["ar"]
  },
  {
    "code": "KY",
    "name": "Cayman Islands",
    "native": "Cayman Islands",
    "phone": "+1345",
    "continent": "NA",
    "capital": "George Town",
    "currency": ["KYD"],
    "languages": ["en"]
  },
  {
    "code": "KZ",
    "name": "Kazakhstan",
    "native": "Қазақстан",
    "phone": "+76",
    "continent": "AS",
    "continents": ["AS", "EU"],
    "capital": "Astana",
    "currency": ["KZT"],
    "languages": ["kk", "ru"]
  },
  {
    "code": "LA",
    "name": "Laos",
    "native": "ສປປລາວ",
    "phone": "+856",
    "continent": "AS",
    "capital": "Vientiane",
    "currency": ["LAK"],
    "languages": ["lo"]
  },
  {
    "code": "LB",
    "name": "Lebanon",
    "native": "لبنان",
    "phone": "+961",
    "continent": "AS",
    "capital": "Beirut",
    "currency": ["LBP"],
    "languages": ["ar", "fr"]
  },
  {
    "code": "LC",
    "name": "Saint Lucia",
    "native": "Saint Lucia",
    "phone": "+1758",
    "continent": "NA",
    "capital": "Castries",
    "currency": ["XCD"],
    "languages": ["en"]
  },
  {
    "code": "LI",
    "name": "Liechtenstein",
    "native": "Liechtenstein",
    "phone": "+423",
    "continent": "EU",
    "capital": "Vaduz",
    "currency": ["CHF"],
    "languages": ["de"]
  },
  {
    "code": "LK",
    "name": "Sri Lanka",
    "native": "śrī laṃkāva",
    "phone": "+94",
    "continent": "AS",
    "capital": "Colombo",
    "currency": ["LKR"],
    "languages": ["si", "ta"]
  },
  {
    "code": "LR",
    "name": "Liberia",
    "native": "Liberia",
    "phone": "+231",
    "continent": "AF",
    "capital": "Monrovia",
    "currency": ["LRD"],
    "languages": ["en"]
  },
  {
    "code": "LS",
    "name": "Lesotho",
    "native": "Lesotho",
    "phone": "+266",
    "continent": "AF",
    "capital": "Maseru",
    "currency": ["LSL", "ZAR"],
    "languages": ["en", "st"]
  },
  {
    "code": "LT",
    "name": "Lithuania",
    "native": "Lietuva",
    "phone": "+370",
    "continent": "EU",
    "capital": "Vilnius",
    "currency": ["EUR"],
    "languages": ["lt"]
  },
  {
    "code": "LU",
    "name": "Luxembourg",
    "native": "Luxembourg",
    "phone": "+352",
    "continent": "EU",
    "capital": "Luxembourg",
    "currency": ["EUR"],
    "languages": ["fr", "de", "lb"]
  },
  {
    "code": "LV",
    "name": "Latvia",
    "native": "Latvija",
    "phone": "+371",
    "continent": "EU",
    "capital": "Riga",
    "currency": ["EUR"],
    "languages": ["lv"]
  },
  {
    "code": "LY",
    "name": "Libya",
    "native": "‏ليبيا",
    "phone": "+218",
    "continent": "AF",
    "capital": "Tripoli",
    "currency": ["LYD"],
    "languages": ["ar"]
  },
  {
    "code": "MA",
    "name": "Morocco",
    "native": "المغرب",
    "phone": "+212",
    "continent": "AF",
    "capital": "Rabat",
    "currency": ["MAD"],
    "languages": ["ar"]
  },
  {
    "code": "MC",
    "name": "Monaco",
    "native": "Monaco",
    "phone": "+377",
    "continent": "EU",
    "capital": "Monaco",
    "currency": ["EUR"],
    "languages": ["fr"]
  },
  {
    "code": "MD",
    "name": "Moldova",
    "native": "Moldova",
    "phone": "+373",
    "continent": "EU",
    "capital": "Chișinău",
    "currency": ["MDL"],
    "languages": ["ro"]
  },
  {
    "code": "ME",
    "name": "Montenegro",
    "native": "Црна Гора",
    "phone": "+382",
    "continent": "EU",
    "capital": "Podgorica",
    "currency": ["EUR"],
    "languages": ["sr", "bs", "sq", "hr"]
  },
  {
    "code": "MF",
    "name": "Saint Martin",
    "native": "Saint-Martin",
    "phone": "+590",
    "continent": "NA",
    "capital": "Marigot",
    "currency": ["EUR"],
    "languages": ["en", "fr", "nl"]
  },
  {
    "code": "MG",
    "name": "Madagascar",
    "native": "Madagasikara",
    "phone": "+261",
    "continent": "AF",
    "capital": "Antananarivo",
    "currency": ["MGA"],
    "languages": ["fr", "mg"]
  },
  {
    "code": "MH",
    "name": "Marshall Islands",
    "native": "M̧ajeļ",
    "phone": "+692",
    "continent": "OC",
    "capital": "Majuro",
    "currency": ["USD"],
    "languages": ["en", "mh"]
  },
  {
    "code": "MK",
    "name": "North Macedonia",
    "native": "Северна Македонија",
    "phone": "+389",
    "continent": "EU",
    "capital": "Skopje",
    "currency": ["MKD"],
    "languages": ["mk"]
  },
  {
    "code": "ML",
    "name": "Mali",
    "native": "Mali",
    "phone": "+223",
    "continent": "AF",
    "capital": "Bamako",
    "currency": ["XOF"],
    "languages": ["fr"]
  },
  {
    "code": "MM",
    "name": "Myanmar (Burma)",
    "native": "မြန်မာ",
    "phone": "+95",
    "continent": "AS",
    "capital": "Naypyidaw",
    "currency": ["MMK"],
    "languages": ["my"]
  },
  {
    "code": "MN",
    "name": "Mongolia",
    "native": "Монгол улс",
    "phone": "+976",
    "continent": "AS",
    "capital": "Ulan Bator",
    "currency": ["MNT"],
    "languages": ["mn"]
  },
  {
    "code": "MO",
    "name": "Macao",
    "native": "澳門",
    "phone": "+853",
    "continent": "AS",
    "capital": "",
    "currency": ["MOP"],
    "languages": ["zh", "pt"]
  },
  {
    "code": "MP",
    "name": "Northern Mariana Islands",
    "native": "Northern Mariana Islands",
    "phone": "+1670",
    "continent": "OC",
    "capital": "Saipan",
    "currency": ["USD"],
    "languages": ["en", "ch"]
  },
  {
    "code": "MQ",
    "name": "Martinique",
    "native": "Martinique",
    "phone": "+596",
    "continent": "NA",
    "capital": "Fort-de-France",
    "currency": ["EUR"],
    "languages": ["fr"]
  },
  {
    "code": "MR",
    "name": "Mauritania",
    "native": "موريتانيا",
    "phone": "+222",
    "continent": "AF",
    "capital": "Nouakchott",
    "currency": ["MRU"],
    "languages": ["ar"]
  },
  {
    "code": "MS",
    "name": "Montserrat",
    "native": "Montserrat",
    "phone": "+1664",
    "continent": "NA",
    "capital": "Plymouth",
    "currency": ["XCD"],
    "languages": ["en"]
  },
  {
    "code": "MT",
    "name": "Malta",
    "native": "Malta",
    "phone": "+356",
    "continent": "EU",
    "capital": "Valletta",
    "currency": ["EUR"],
    "languages": ["mt", "en"]
  },
  {
    "code": "MU",
    "name": "Mauritius",
    "native": "Maurice",
    "phone": "+230",
    "continent": "AF",
    "capital": "Port Louis",
    "currency": ["MUR"],
    "languages": ["en"]
  },
  {
    "code": "MV",
    "name": "Maldives",
    "native": "Maldives",
    "phone": "+960",
    "continent": "AS",
    "capital": "Malé",
    "currency": ["MVR"],
    "languages": ["dv"]
  },
  {
    "code": "MW",
    "name": "Malawi",
    "native": "Malawi",
    "phone": "+265",
    "continent": "AF",
    "capital": "Lilongwe",
    "currency": ["MWK"],
    "languages": ["en", "ny"]
  },
  {
    "code": "MX",
    "name": "Mexico",
    "native": "México",
    "phone": "+52",
    "continent": "NA",
    "capital": "Mexico City",
    "currency": ["MXN"],
    "languages": ["es"]
  },
  {
    "code": "MY",
    "name": "Malaysia",
    "native": "Malaysia",
    "phone": "+60",
    "continent": "AS",
    "capital": "Kuala Lumpur",
    "currency": ["MYR"],
    "languages": ["ms"]
  },
  {
    "code": "MZ",
    "name": "Mozambique",
    "native": "Moçambique",
    "phone": "+258",
    "continent": "AF",
    "capital": "Maputo",
    "currency": ["MZN"],
    "languages": ["pt"]
  },
  {
    "code": "NA",
    "name": "Namibia",
    "native": "Namibia",
    "phone": "+264",
    "continent": "AF",
    "capital": "Windhoek",
    "currency": ["NAD", "ZAR"],
    "languages": ["en", "af"]
  },
  {
    "code": "NC",
    "name": "New Caledonia",
    "native": "Nouvelle-Calédonie",
    "phone": "+687",
    "continent": "OC",
    "capital": "Nouméa",
    "currency": ["XPF"],
    "languages": ["fr"]
  },
  {
    "code": "NE",
    "name": "Niger",
    "native": "Niger",
    "phone": "+227",
    "continent": "AF",
    "capital": "Niamey",
    "currency": ["XOF"],
    "languages": ["fr"]
  },
  {
    "code": "NF",
    "name": "Norfolk Island",
    "native": "Norfolk Island",
    "phone": "+672",
    "continent": "OC",
    "capital": "Kingston",
    "currency": ["AUD"],
    "languages": ["en"]
  },
  {
    "code": "NG",
    "name": "Nigeria",
    "native": "Nigeria",
    "phone": "+234",
    "continent": "AF",
    "capital": "Abuja",
    "currency": ["NGN"],
    "languages": ["en"]
  },
  {
    "code": "NI",
    "name": "Nicaragua",
    "native": "Nicaragua",
    "phone": "+505",
    "continent": "NA",
    "capital": "Managua",
    "currency": ["NIO"],
    "languages": ["es"]
  },
  {
    "code": "NL",
    "name": "Netherlands",
    "native": "Nederland",
    "phone": "+31",
    "continent": "EU",
    "capital": "Amsterdam",
    "currency": ["EUR"],
    "languages": ["nl"]
  },
  {
    "code": "NO",
    "name": "Norway",
    "native": "Norge",
    "phone": "+47",
    "continent": "EU",
    "capital": "Oslo",
    "currency": ["NOK"],
    "languages": ["no", "nb", "nn"]
  },
  {
    "code": "NP",
    "name": "Nepal",
    "native": "नेपाल",
    "phone": "+977",
    "continent": "AS",
    "capital": "Kathmandu",
    "currency": ["NPR"],
    "languages": ["ne"]
  },
  {
    "code": "NR",
    "name": "Nauru",
    "native": "Nauru",
    "phone": "+674",
    "continent": "OC",
    "capital": "Yaren",
    "currency": ["AUD"],
    "languages": ["en", "na"]
  },
  {
    "code": "NU",
    "name": "Niue",
    "native": "Niuē",
    "phone": "+683",
    "continent": "OC",
    "capital": "Alofi",
    "currency": ["NZD"],
    "languages": ["en"]
  },
  {
    "code": "NZ",
    "name": "New Zealand",
    "native": "New Zealand",
    "phone": "+64",
    "continent": "OC",
    "capital": "Wellington",
    "currency": ["NZD"],
    "languages": ["en", "mi"]
  },
  {
    "code": "OM",
    "name": "Oman",
    "native": "عمان",
    "phone": "+968",
    "continent": "AS",
    "capital": "Muscat",
    "currency": ["OMR"],
    "languages": ["ar"]
  },
  {
    "code": "PA",
    "name": "Panama",
    "native": "Panamá",
    "phone": "+507",
    "continent": "NA",
    "capital": "Panama City",
    "currency": ["PAB", "USD"],
    "languages": ["es"]
  },
  {
    "code": "PE",
    "name": "Peru",
    "native": "Perú",
    "phone": "+51",
    "continent": "SA",
    "capital": "Lima",
    "currency": ["PEN"],
    "languages": ["es"]
  },
  {
    "code": "PF",
    "name": "French Polynesia",
    "native": "Polynésie française",
    "phone": "+689",
    "continent": "OC",
    "capital": "Papeetē",
    "currency": ["XPF"],
    "languages": ["fr"]
  },
  {
    "code": "PG",
    "name": "Papua New Guinea",
    "native": "Papua Niugini",
    "phone": "+675",
    "continent": "OC",
    "capital": "Port Moresby",
    "currency": ["PGK"],
    "languages": ["en"]
  },
  {
    "code": "PH",
    "name": "Philippines",
    "native": "Pilipinas",
    "phone": "+63",
    "continent": "AS",
    "capital": "Manila",
    "currency": ["PHP"],
    "languages": ["en"]
  },
  {
    "code": "PK",
    "name": "Pakistan",
    "native": "Pakistan",
    "phone": "+92",
    "continent": "AS",
    "capital": "Islamabad",
    "currency": ["PKR"],
    "languages": ["en", "ur"]
  },
  {
    "code": "PL",
    "name": "Poland",
    "native": "Polska",
    "phone": "+48",
    "continent": "EU",
    "capital": "Warsaw",
    "currency": ["PLN"],
    "languages": ["pl"]
  },
  {
    "code": "PM",
    "name": "Saint Pierre and Miquelon",
    "native": "Saint-Pierre-et-Miquelon",
    "phone": "+508",
    "continent": "NA",
    "capital": "Saint-Pierre",
    "currency": ["EUR"],
    "languages": ["fr"]
  },
  {
    "code": "PN",
    "name": "Pitcairn Islands",
    "native": "Pitcairn Islands",
    "phone": "+64",
    "continent": "OC",
    "capital": "Adamstown",
    "currency": ["NZD"],
    "languages": ["en"]
  },
  {
    "code": "PR",
    "name": "Puerto Rico",
    "native": "Puerto Rico",
    "phone": "+1787",
    "continent": "NA",
    "capital": "San Juan",
    "currency": ["USD"],
    "languages": ["es", "en"]
  },
  {
    "code": "PS",
    "name": "Palestine",
    "native": "فلسطين",
    "phone": "+970",
    "continent": "AS",
    "capital": "Ramallah",
    "currency": ["ILS"],
    "languages": ["ar"]
  },
  {
    "code": "PT",
    "name": "Portugal",
    "native": "Portugal",
    "phone": "+351",
    "continent": "EU",
    "capital": "Lisbon",
    "currency": ["EUR"],
    "languages": ["pt"]
  },
  {
    "code": "PW",
    "name": "Palau",
    "native": "Palau",
    "phone": "+680",
    "continent": "OC",
    "capital": "Ngerulmud",
    "currency": ["USD"],
    "languages": ["en"]
  },
  {
    "code": "PY",
    "name": "Paraguay",
    "native": "Paraguay",
    "phone": "+595",
    "continent": "SA",
    "capital": "Asunción",
    "currency": ["PYG"],
    "languages": ["es", "gn"]
  },
  {
    "code": "QA",
    "name": "Qatar",
    "native": "قطر",
    "phone": "+974",
    "continent": "AS",
    "capital": "Doha",
    "currency": ["QAR"],
    "languages": ["ar"]
  },
  {
    "code": "RE",
    "name": "Reunion",
    "native": "La Réunion",
    "phone": "+262",
    "continent": "AF",
    "capital": "Saint-Denis",
    "currency": ["EUR"],
    "languages": ["fr"]
  },
  {
    "code": "RO",
    "name": "Romania",
    "native": "România",
    "phone": "+40",
    "continent": "EU",
    "capital": "Bucharest",
    "currency": ["RON"],
    "languages": ["ro"]
  },
  {
    "code": "RS",
    "name": "Serbia",
    "native": "Србија",
    "phone": "+381",
    "continent": "EU",
    "capital": "Belgrade",
    "currency": ["RSD"],
    "languages": ["sr"]
  },
  {
    "code": "RU",
    "name": "Russia",
    "native": "Россия",
    "phone": "+7",
    "continent": "AS",
    "continents": ["AS", "EU"],
    "capital": "Moscow",
    "currency": ["RUB"],
    "languages": ["ru"]
  },
  {
    "code": "RW",
    "name": "Rwanda",
    "native": "Rwanda",
    "phone": "+250",
    "continent": "AF",
    "capital": "Kigali",
    "currency": ["RWF"],
    "languages": ["rw", "en", "fr"]
  },
  {
    "code": "SA",
    "name": "Saudi Arabia",
    "native": "العربية السعودية",
    "phone": "+966",
    "continent": "AS",
    "capital": "Riyadh",
    "currency": ["SAR"],
    "languages": ["ar"]
  },
  {
    "code": "SB",
    "name": "Solomon Islands",
    "native": "Solomon Islands",
    "phone": "+677",
    "continent": "OC",
    "capital": "Honiara",
    "currency": ["SBD"],
    "languages": ["en"]
  },
  {
    "code": "SC",
    "name": "Seychelles",
    "native": "Seychelles",
    "phone": "+248",
    "continent": "AF",
    "capital": "Victoria",
    "currency": ["SCR"],
    "languages": ["fr", "en"]
  },
  {
    "code": "SD",
    "name": "Sudan",
    "native": "السودان",
    "phone": "+249",
    "continent": "AF",
    "capital": "Khartoum",
    "currency": ["SDG"],
    "languages": ["ar", "en"]
  },
  {
    "code": "SE",
    "name": "Sweden",
    "native": "Sverige",
    "phone": "+46",
    "continent": "EU",
    "capital": "Stockholm",
    "currency": ["SEK"],
    "languages": ["sv"]
  },
  {
    "code": "SG",
    "name": "Singapore",
    "native": "Singapore",
    "phone": "+65",
    "continent": "AS",
    "capital": "Singapore",
    "currency": ["SGD"],
    "languages": ["en", "ms", "ta", "zh"]
  },
  {
    "code": "SH",
    "name": "Saint Helena",
    "native": "Saint Helena",
    "phone": "+290",
    "continent": "AF",
    "capital": "Jamestown",
    "currency": ["SHP"],
    "languages": ["en"]
  },
  {
    "code": "SI",
    "name": "Slovenia",
    "native": "Slovenija",
    "phone": "+386",
    "continent": "EU",
    "capital": "Ljubljana",
    "currency": ["EUR"],
    "languages": ["sl"]
  },
  {
    "code": "SJ",
    "name": "Svalbard and Jan Mayen",
    "native": "Svalbard og Jan Mayen",
    "phone": "+4779",
    "continent": "EU",
    "capital": "Longyearbyen",
    "currency": ["NOK"],
    "languages": ["no"]
  },
  {
    "code": "SK",
    "name": "Slovakia",
    "native": "Slovensko",
    "phone": "+421",
    "continent": "EU",
    "capital": "Bratislava",
    "currency": ["EUR"],
    "languages": ["sk"]
  },
  {
    "code": "SL",
    "name": "Sierra Leone",
    "native": "Sierra Leone",
    "phone": "+232",
    "continent": "AF",
    "capital": "Freetown",
    "currency": ["SLL"],
    "languages": ["en"]
  },
  {
    "code": "SM",
    "name": "San Marino",
    "native": "San Marino",
    "phone": "+378",
    "continent": "EU",
    "capital": "City of San Marino",
    "currency": ["EUR"],
    "languages": ["it"]
  },
  {
    "code": "SN",
    "name": "Senegal",
    "native": "Sénégal",
    "phone": "+221",
    "continent": "AF",
    "capital": "Dakar",
    "currency": ["XOF"],
    "languages": ["fr"]
  },
  {
    "code": "SO",
    "name": "Somalia",
    "native": "Soomaaliya",
    "phone": "+252",
    "continent": "AF",
    "capital": "Mogadishu",
    "currency": ["SOS"],
    "languages": ["so", "ar"]
  },
  {
    "code": "SR",
    "name": "Suriname",
    "native": "Suriname",
    "phone": "+597",
    "continent": "SA",
    "capital": "Paramaribo",
    "currency": ["SRD"],
    "languages": ["nl"]
  },
  {
    "code": "SS",
    "name": "South Sudan",
    "native": "South Sudan",
    "phone": "+211",
    "continent": "AF",
    "capital": "Juba",
    "currency": ["SSP"],
    "languages": ["en"]
  },
  {
    "code": "ST",
    "name": "Sao Tome and Principe",
    "native": "São Tomé e Príncipe",
    "phone": "+239",
    "continent": "AF",
    "capital": "São Tomé",
    "currency": ["STN"],
    "languages": ["pt"]
  },
  {
    "code": "SV",
    "name": "El Salvador",
    "native": "El Salvador",
    "phone": "+503",
    "continent": "NA",
    "capital": "San Salvador",
    "currency": ["SVC", "USD"],
    "languages": ["es"]
  },
  {
    "code": "SX",
    "name": "Sint Maarten",
    "native": "Sint Maarten",
    "phone": "+1721",
    "continent": "NA",
    "capital": "Philipsburg",
    "currency": ["ANG"],
    "languages": ["nl", "en"]
  },
  {
    "code": "SY",
    "name": "Syria",
    "native": "سوريا",
    "phone": "+963",
    "continent": "AS",
    "capital": "Damascus",
    "currency": ["SYP"],
    "languages": ["ar"]
  },
  {
    "code": "SZ",
    "name": "Eswatini",
    "native": "Eswatini",
    "phone": "+268",
    "continent": "AF",
    "capital": "Lobamba",
    "currency": ["SZL"],
    "languages": ["en", "ss"]
  },
  {
    "code": "TC",
    "name": "Turks and Caicos Islands",
    "native": "Turks and Caicos Islands",
    "phone": "+1649",
    "continent": "NA",
    "capital": "Cockburn Town",
    "currency": ["USD"],
    "languages": ["en"]
  },
  {
    "code": "TD",
    "name": "Chad",
    "native": "Tchad",
    "phone": "+235",
    "continent": "AF",
    "capital": "N'Djamena",
    "currency": ["XAF"],
    "languages": ["fr", "ar"]
  },
  {
    "code": "TF",
    "name": "French Southern Territories",
    "native": "Territoire des Terres australes et antarctiques fr",
    "phone": "+262",
    "continent": "AN",
    "capital": "Port-aux-Français",
    "currency": ["EUR"],
    "languages": ["fr"]
  },
  {
    "code": "TG",
    "name": "Togo",
    "native": "Togo",
    "phone": "+228",
    "continent": "AF",
    "capital": "Lomé",
    "currency": ["XOF"],
    "languages": ["fr"]
  },
  {
    "code": "TH",
    "name": "Thailand",
    "native": "ประเทศไทย",
    "phone": "+66",
    "continent": "AS",
    "capital": "Bangkok",
    "currency": ["THB"],
    "languages": ["th"]
  },
  {
    "code": "TJ",
    "name": "Tajikistan",
    "native": "Тоҷикистон",
    "phone": "+992",
    "continent": "AS",
    "capital": "Dushanbe",
    "currency": ["TJS"],
    "languages": ["tg", "ru"]
  },
  {
    "code": "TK",
    "name": "Tokelau",
    "native": "Tokelau",
    "phone": "+690",
    "continent": "OC",
    "capital": "Fakaofo",
    "currency": ["NZD"],
    "languages": ["en"]
  },
  {
    "code": "TL",
    "name": "East Timor",
    "native": "Timor-Leste",
    "phone": "+670",
    "continent": "OC",
    "capital": "Dili",
    "currency": ["USD"],
    "languages": ["pt"]
  },
  {
    "code": "TM",
    "name": "Turkmenistan",
    "native": "Türkmenistan",
    "phone": "+993",
    "continent": "AS",
    "capital": "Ashgabat",
    "currency": ["TMT"],
    "languages": ["tk", "ru"]
  },
  {
    "code": "TN",
    "name": "Tunisia",
    "native": "تونس",
    "phone": "+216",
    "continent": "AF",
    "capital": "Tunis",
    "currency": ["TND"],
    "languages": ["ar"]
  },
  {
    "code": "TO",
    "name": "Tonga",
    "native": "Tonga",
    "phone": "+676",
    "continent": "OC",
    "capital": "Nuku'alofa",
    "currency": ["TOP"],
    "languages": ["en", "to"]
  },
  {
    "code": "TR",
    "name": "Turkey",
    "native": "Türkiye",
    "phone": "+90",
    "continent": "AS",
    "continents": ["AS", "EU"],
    "capital": "Ankara",
    "currency": ["TRY"],
    "languages": ["tr"]
  },
  {
    "code": "TT",
    "name": "Trinidad and Tobago",
    "native": "Trinidad and Tobago",
    "phone": "+1868",
    "continent": "NA",
    "capital": "Port of Spain",
    "currency": ["TTD"],
    "languages": ["en"]
  },
  {
    "code": "TV",
    "name": "Tuvalu",
    "native": "Tuvalu",
    "phone": "+688",
    "continent": "OC",
    "capital": "Funafuti",
    "currency": ["AUD"],
    "languages": ["en"]
  },
  {
    "code": "TW",
    "name": "Taiwan",
    "native": "臺灣",
    "phone": "+886",
    "continent": "AS",
    "capital": "Taipei",
    "currency": ["TWD"],
    "languages": ["zh"]
  },
  {
    "code": "TZ",
    "name": "Tanzania",
    "native": "Tanzania",
    "phone": "+255",
    "continent": "AF",
    "capital": "Dodoma",
    "currency": ["TZS"],
    "languages": ["sw", "en"]
  },
  {
    "code": "UA",
    "name": "Ukraine",
    "native": "Україна",
    "phone": "+380",
    "continent": "EU",
    "capital": "Kyiv",
    "currency": ["UAH"],
    "languages": ["uk"]
  },
  {
    "code": "UG",
    "name": "Uganda",
    "native": "Uganda",
    "phone": "+256",
    "continent": "AF",
    "capital": "Kampala",
    "currency": ["UGX"],
    "languages": ["en", "sw"]
  },
  {
    "code": "UM",
    "name": "U.S. Minor Outlying Islands",
    "native": "United States Minor Outlying Islands",
    "phone": "+1",
    "continent": "OC",
    "capital": "",
    "currency": ["USD"],
    "languages": ["en"]
  },
  {
    "code": "US",
    "name": "United States",
    "native": "United States",
    "phone": "+1",
    "continent": "NA",
    "capital": "Washington D.C.",
    "currency": ["USD", "USN", "USS"],
    "languages": ["en"]
  },
  {
    "code": "UY",
    "name": "Uruguay",
    "native": "Uruguay",
    "phone": "+598",
    "continent": "SA",
    "capital": "Montevideo",
    "currency": ["UYI", "UYU"],
    "languages": ["es"]
  },
  {
    "code": "UZ",
    "name": "Uzbekistan",
    "native": "O'zbekiston",
    "phone": "+998",
    "continent": "AS",
    "capital": "Tashkent",
    "currency": ["UZS"],
    "languages": ["uz", "ru"]
  },
  {
    "code": "VA",
    "name": "Vatican City",
    "native": "Vaticano",
    "phone": "+379",
    "continent": "EU",
    "capital": "Vatican City",
    "currency": ["EUR"],
    "languages": ["it", "la"]
  },
  {
    "code": "VC",
    "name": "Saint Vincent and the Grenadines",
    "native": "Saint Vincent and the Grenadines",
    "phone": "+1784",
    "continent": "NA",
    "capital": "Kingstown",
    "currency": ["XCD"],
    "languages": ["en"]
  },
  {
    "code": "VE",
    "name": "Venezuela",
    "native": "Venezuela",
    "phone": "+58",
    "continent": "SA",
    "capital": "Caracas",
    "currency": ["VES"],
    "languages": ["es"]
  },
  {
    "code": "VG",
    "name": "British Virgin Islands",
    "native": "British Virgin Islands",
    "phone": "+1284",
    "continent": "NA",
    "capital": "Road Town",
    "currency": ["USD"],
    "languages": ["en"]
  },
  {
    "code": "VI",
    "name": "U.S. Virgin Islands",
    "native": "United States Virgin Islands",
    "phone": "+1340",
    "continent": "NA",
    "capital": "Charlotte Amalie",
    "currency": ["USD"],
    "languages": ["en"]
  },
  {
    "code": "VN",
    "name": "Vietnam",
    "native": "Việt Nam",
    "phone": "+84",
    "continent": "AS",
    "capital": "Hanoi",
    "currency": ["VND"],
    "languages": ["vi"]
  },
  {
    "code": "VU",
    "name": "Vanuatu",
    "native": "Vanuatu",
    "phone": "+678",
    "continent": "OC",
    "capital": "Port Vila",
    "currency": ["VUV"],
    "languages": ["bi", "en", "fr"]
  },
  {
    "code": "WF",
    "name": "Wallis and Futuna",
    "native": "Wallis et Futuna",
    "phone": "+681",
    "continent": "OC",
    "capital": "Mata-Utu",
    "currency": ["XPF"],
    "languages": ["fr"]
  },
  {
    "code": "WS",
    "name": "Samoa",
    "native": "Samoa",
    "phone": "+685",
    "continent": "OC",
    "capital": "Apia",
    "currency": ["WST"],
    "languages": ["sm", "en"]
  },
  {
    "code": "XK",
    "name": "Kosovo",
    "native": "Republika e Kosovës",
    "phone": "+377",
    "continent": "EU",
    "capital": "Pristina",
    "currency": ["EUR"],
    "languages": ["sq", "sr"]
  },
  {
    "code": "YE",
    "name": "Yemen",
    "native": "اليَمَن",
    "phone": "+967",
    "continent": "AS",
    "capital": "Sana'a",
    "currency": ["YER"],
    "languages": ["ar"]
  },
  {
    "code": "YT",
    "name": "Mayotte",
    "native": "Mayotte",
    "phone": "+262",
    "continent": "AF",
    "capital": "Mamoudzou",
    "currency": ["EUR"],
    "languages": ["fr"]
  },
  {
    "code": "ZA",
    "name": "South Africa",
    "native": "South Africa",
    "phone": "+27",
    "continent": "AF",
    "capital": "Pretoria",
    "currency": ["ZAR"],
    "languages": ["af", "en", "nr", "st", "ss", "tn", "ts", "ve", "xh", "zu"]
  },
  {
    "code": "ZM",
    "name": "Zambia",
    "native": "Zambia",
    "phone": "+260",
    "continent": "AF",
    "capital": "Lusaka",
    "currency": ["ZMW"],
    "languages": ["en"]
  },
  {
    "code": "ZW",
    "name": "Zimbabwe",
    "native": "Zimbabwe",
    "phone": "+263",
    "continent": "AF",
    "capital": "Harare",
    "currency": ["USD", "ZAR", "BWP", "GBP", "AUD", "CNY", "INR", "JPY"],
    "languages": ["en", "sn", "nd"]
  }
]


member_role_list = [
  { "key": "CM", "value": _("Choir member") },
  { "key": "LD", "value": _("Local director") },
  { "key": "SD", "value": _("State director") },
  { "key": "NM", "value": _("Non choir member") },
]

member_voice_list = [
  { "key": "S1", "value": "Soprano 1" },
  { "key": "S2", "value": "Soprano 2" },
  { "key": "A1", "value": "Alto 1" },
  { "key": "A2", "value": "Alto 2" },
  { "key": "T1", "value": "Tenor 1" },
  { "key": "T2", "value": "Tenor 2" },
  { "key": "B1", "value": f'{_("Bass")} {"1"}' },
  { "key": "B2", "value": f'{_("Bass")} {"2"}' },
]

PHONE_CODES = jsonToTuppleList(country_list, 'code', 'phone')

COUNTRY_NAMES = jsonToTuppleList(country_list, 'code', 'native')

MEMBER_ROLES = jsonToTuppleList(member_role_list, 'key', 'value')

MEMBER_VOICES = jsonToTuppleList(member_voice_list, 'key', 'value')
