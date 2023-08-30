# Importarea modulelor și variabilelor:

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import API_TOKEN  # Importă variabila TELEGRAM_API_TOKEN din config.py

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)  # Folosește variabila TELEGRAM_API_TOKEN din config.py
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Inițializarea tastaturii principale:

main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add(types.KeyboardButton("1 - Pentru a raporta un caz de asigurare"))
main_keyboard.add(types.KeyboardButton("2 - Pentru a anula o polița de asigurare"))
main_keyboard.add(types.KeyboardButton("3 - Pentru a introduce modificări în poliță de asigurare"))
main_keyboard.add(types.KeyboardButton("4 - Pentru perfectarea unei polițe de asigurare"))

# Adaugă butoane pentru diferite tipuri de evenimente
event_report_options_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
event_report_options_keyboard.add(types.KeyboardButton("11 - CASCO"))
event_report_options_keyboard.add(types.KeyboardButton("12 - AORC"))
event_report_options_keyboard.add(types.KeyboardButton("13 - Asigurarea bunurilor"))
event_report_options_keyboard.add(types.KeyboardButton("14 - Asigurarea medicală peste hotare"))

# Adaugă butoane pentru sub-opțiunile CASCO
casco_sub_options_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
casco_sub_options_keyboard.add(types.KeyboardButton("111 - Sunt o persoană fizică, doresc să înregistrez un caz de asigurare și să aflu lista documentelor necesare"))
casco_sub_options_keyboard.add(types.KeyboardButton("112 - Sunt o persoană juridică, doresc să înregistrez un caz de asigurare și să aflu lista documentelor necesare"))
casco_sub_options_keyboard.add(types.KeyboardButton("113 - Să transmit documentele care au lipsit pentru un caz asigurat, raportat anterior"))
casco_sub_options_keyboard.add(types.KeyboardButton("114 - La ce stadiu de procesare se află cererea mea de despăgubire"))
casco_sub_options_keyboard.add(types.KeyboardButton("115 - Acțiuni în cazul unui eveniment asigurat"))
casco_sub_options_keyboard.add(types.KeyboardButton("00 - La începutul meniului"))

# Adaugă butoane pentru sub-sub-opțiunile CASCO
sub_sub_options_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
sub_sub_options_keyboard.add(types.KeyboardButton("1111 - ACCIDENT RUTIER"))
sub_sub_options_keyboard.add(types.KeyboardButton("1112 - Avariere într-o parcare, calamități naturale, incendiu"))
sub_sub_options_keyboard.add(types.KeyboardButton("1113 - Furt"))
sub_sub_options_keyboard.add(types.KeyboardButton("00 - La începutul meniului"))

sub_sub_sub_options_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
sub_sub_sub_options_keyboard.add(types.KeyboardButton("00 - La începutul meniului"))

back_to_start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_to_start_keyboard.add(types.KeyboardButton("00 - La începutul meniului"))


# Definirea handlerelor pentru comenzile și opțiunile selectate de utilizator
# Afisarea mesajelor corespunzătoare utilizatorului în funcție de alegere

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Bine ați venit! Vă rugăm să selectați punctul care vă interesează și să transmiteți un mesaj de răspuns cu numărul corespunzător, de exemplu, 1 sau 3:", reply_markup=main_keyboard)


@dp.message_handler(lambda message: message.text.startswith("2"))
async def cancel_policy(message: types.Message):
    await message.answer("Ați selectat opțiunea 2. Dacă doriți să anulați polița, vă rugăm să ne contactați la numărul de telefon (022) 889 889")

@dp.message_handler(lambda message: message.text.startswith("3"))
async def modify_policy(message: types.Message):
    await message.answer("Ați selectat opțiunea 3. Vă rugăm să ne furnizați detaliile pe care doriți să le modificați.")

@dp.message_handler(lambda message: message.text.startswith("4"))
async def buy_or_extend_policy(message: types.Message):
    await message.answer("Ați selectat opțiunea 4. Vă rugăm să accesați site-ul nostru pentru a cumpăra o polița de asigurare: https://moldasig.md/company/comanda-produs-asigurare/.")

@dp.message_handler(lambda message: message.text.startswith("5"))
async def check_claim_status(message: types.Message):
    await message.answer("Ați selectat opțiunea 5. Vă rugăm să ne furnizați numărul cererii de despăgubire pentru a clarifica stadiul acesteia.")

@dp.message_handler(lambda message: message.text == "1 - Pentru a raporta un caz de asigurare")
async def report_event(message: types.Message):
    await message.answer("Ați selectat opțiunea 1 - Pentru a raporta un eveniment asigurat. Vă rugăm să selectați tipul de asigurare:", reply_markup=event_report_options_keyboard)

@dp.message_handler(lambda message: message.text == "11 - CASCO")
async def casco_sub_options(message: types.Message):
    await message.answer("Ați selectat opțiunea 11 - CASCO. Vă rugăm să alegeți una dintre următoarele opțiuni:", reply_markup=casco_sub_options_keyboard)

@dp.message_handler(lambda message: message.text == "11111 - Operator de contact")
async def handle_sub_sub_sub_menu_selection(message: types.Message):
    await message.answer("Ați selectat opțiunea 11111 - Operator de contact. ...", reply_markup=None)

@dp.message_handler(lambda message: message.text == "00 - La începutul meniului")
async def back_to_main_menu(message: types.Message):
    await message.answer("Vă rugăm să selectați punctul care vă interesează și să transmiteți un mesaj de răspuns cu numărul corespunzător, de exemplu, 1 sau 3:", reply_markup=main_keyboard)
@dp.message_handler(lambda message: message.text == "111 - Sunt o persoană fizică, doresc să înregistrez un caz de asigurare și să aflu lista documentelor necesare")
async def handle_sub_menu_selection(message: types.Message):
    await message.answer("Ați selectat opțiunea 111 - Sunt o persoană fizică, doresc să înregistrez un caz de asigurare și să aflu lista documentelor necesare. Vă rugăm să selectați tipul de accident care vi s-a întâmplat și trimiteți numărul punctului din meniu:", reply_markup=sub_sub_options_keyboard)


@dp.message_handler(lambda message: message.text == "1111 - ACCIDENT RUTIER")
async def handle_sub_sub_menu_selection(message: types.Message, sub_sub_sub_options_keyboard=None):
    response = (
        "Pentru avizarea unei daune CASCO către C.A. „GENERAL ASIGURĂRI”S.A. aveți la dispoziție următoarele modalități:\n"
        "- putețiaccesa linkul: https://moldasig.md/case-report.html și completa formularul de înregistrare, va dura doar 5-7 minute.\n"
        "- ne puteți apela telefonic la numerele tel: (022) 78-41-15, 78-41-07, programul fiind de luni până vineri între orele 08:30-17:30;\n"
        "- ne puteți expedia oricând un e-mail la adresa: despagubiri@general.md cu detalii despre eveniment, seria/numărul poliței GENERAL ASIGURĂRI și numele Dvs.\n"
        "- ne puteți transmite documentele prin poștă, la adresa: C.A „GENERAL ASIGURĂRI”S.A., Moldova, mun. Chișinău, str. Burebista, 106.\n"
        "- vă puteți prezenta la centrul de despăgubiri al C.A.„GENERAL ASIGURĂRI”SA de pe str. Burebista, 106, etajul 3, mun. Chișinău, sau la oficiile teritoriale din țară ale GENERAL ASIGURĂRI.\n"
        
        "Lista documentelor necesar a fi prezentate de către persoanele asigurate:\n"
        
        "1) Buletin de identitate al asiguratului sau al delegatului plus procura;\n"
        "2) Permisul de conducere al persoanei care se afla la volan în timpul producerii evenimentului;\n"
        "3) Certificat de înmatriculare a mașinii avariate;\n"
        "4) Raport de verificare tehnică a vehiculului, valabil la data accidentului;\n"
        "5) Foaia de parcurs, în cazul în care mașina este în proprietatea unei firme;\n"
        "6) Copia poliței CASCO sau indicarea numărului si seriei poliței de asigurare;\n"
        "7) Dosarul contravențional (copia legalizată) sau oricare alt act emis de poliție, din care să reiasă cum și când s-a produs evenimentul și – după caz – cine este vinovat de producerea daunei;\n"
        "8) Împuternicire de la firma, în cazul în care mașina este în proprietatea unei firme;\n"
        "9) Procura notarială, în cazul în care proprietarul nu se poate prezenta la constatare;\n"
        "10) Împuternicire de la firma de leasing, în cazul în care mașina este in proprietatea unei firmei de leasing.\n"
        "11) Expert regularizare daune - AutoCASCO (Tel: 022 990 726).\n"
        "-----------------------------\n"
        "00 - La începutul meniului\n"
    )

    await message.answer(response, reply_markup=sub_sub_sub_options_keyboard)

@dp.message_handler(lambda message: message.text == "00 - La începutul meniului")
async def back_to_start(message: types.Message):
    await start(message)

# Pornirea executării botului:

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)


