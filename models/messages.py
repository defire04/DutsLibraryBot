from telegram_bot.controllers.keyboard_controller import KeyboardController
from telegram_bot.controllers.message_creator import MessageCreator


class Messages:
    start_message = MessageCreator(

        """
Радий вас бачити,  {name}! 🎓
Я бот написаний на Python 🐍 для пошуку книг у бібліотеці ДУТ (Державний університет телекомунікацій) по:  

💻 Інформаційних технологіях
🔐 Захисту інформації
📡 Телекомунікаціях
🗃 Менеджменту та підприємництву

Зараз у боті книг: {book_in_db} 📚
Кількість користувачів: {count_of_users} 
    
Ми надаємо вам можливість вибрати за яким параметром ви хочете шукати. Давайте почнемо?

Потрібна допомога? 🫶
Пишіть /help або заходь в меню 🧭
""",
        reply_markup=KeyboardController.create_start_menu_keyboard()
    )

    main_menu_message = MessageCreator(
        """
🔍 Виберіть спосіб пошуку книг 🔍
        """,
        reply_markup=KeyboardController.create_main_menu_keyboard()
    )

    help_info_message = MessageCreator(
        """
Інструкція роботи з ботом. 👩‍🏫
Щоб розпочати роботу з ботом, потрібно натиснути кнопку "Розпочати!"
Вам видасть головне меню, де ви можете вибрати за яким критерієм ви хочете знайти книгу.

На даний момент є вибір пошуку за категоріями та за назвою книги.

·Якщо ви натисните кнопку "📃 Категорії", вас перекине на 4 глобальні категорії, натиснувши на одну з них, вас направить на більш вузькоспрямовану категорію, натиснувши на цю категорію, ви отримаєте всі книги, які є в бібліотеці ДУТу за цим напрямком.

·Якщо ви оберете кнопку "📘 Назва книги", вам буде надіслано повідомлення, на яке ви надіслати назву бажаної книги. Якщо не знаєте точну назву - не проблема, можна написати зразкову назву і бот все знайде. Наприклад: С#.

В описі книги є посилання на завантаження з офіційного сайту ДУТ.
Також нижче в цьому повідомленні ви побачите кнопку "Сортувати за".
У нас є кілька режимів сортування:
1) Без сортувань
2) За датою публікації книги –  📆
3) За назвою книги – 📚
4) За автором – 👴

Кнопка сортування має вибір сортування "↕". Натиснувши кнопку, ви можете вибрати як хочете сортувати книги.

УВАГА❗❗❗
Якщо ви хочете зробити новий запит по назві книги, натисніть на кнопку "Головне меню" або створіть нове меню, натиснув на кнопку "Меню", що знаходиться знизу зліва або напишіть /menu.
        """,
        reply_markup=KeyboardController.create_start_menu_keyboard()
    )

    no_book_message = MessageCreator(
        "Такої книги немає чи запит не вірний! 😦",
        reply_markup=KeyboardController.create_back_to_main_menu_keyboard()
    )

    global_category_pick_message = MessageCreator(
        "👇 Оберіть глобальну категорію серед нижче наведених 👇",
        reply_markup=KeyboardController.create_global_categories_keyboard()
    )
