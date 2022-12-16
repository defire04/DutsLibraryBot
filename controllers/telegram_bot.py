from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from controllers.keyboard_controller import KeyboardController
from controllers.message_controller import MessageController
from models.search_result import PagesResult, SearchResult


from resources.config import TOKEN
from services.book_service import BookService
from actions.action_creator import ButtonAction, ButtonPageAction, Actions, ButtonPageActionPayload
from services.query_servise import QueryService
from util.util import string_trim

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

action = ButtonPageAction(1, 2)
button = InlineKeyboardButton('Text', callback_data=action.stringify())
inline_kb_full = InlineKeyboardMarkup(row_width=2).add(button)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне название книги!\nЗапрос должен содержать минимум 3 символа!",
                        reply_markup=inline_kb_full)


def get_search_result_from_search_query(search_string: str):
    book_list_and_query = BookService.find_by_title_and_create_query(search_string)

    if not book_list_and_query["books"]:
        return None

    print(book_list_and_query["query_id"])
    return SearchResult(book_list_and_query["books"], book_list_and_query["query_id"])


@dp.message_handler()
async def echo_message(msg: types.Message):
    # print(msg.from_user.id)
    # print(msg.from_user.username)
    if len(msg.text) < 2:
        await bot.send_message(msg.from_user.id, "Запрос должен содержать минимум 2 символа!")
        return

    search_result = get_search_result_from_search_query(msg.text)
    pages = PagesResult(search_result)
    
    if not pages:
        await bot.send_message(msg.from_user.id, "Такой книги нет или запрос не верен!")
        return

    page_index = 0

    keyboard = KeyboardController.create_pages_keyboard(pages, page_index)

    message = MessageController.preapare_page_message(pages.get_page(page_index))

    await bot.send_message(msg.from_user.id, message, reply_markup=keyboard)
    await msg.delete()


@dp.callback_query_handler(lambda callback: callback.data and ButtonAction.from_json(callback.data).id == Actions.SWITCH_PAGE)
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    
    action = ButtonAction[ButtonPageActionPayload].from_json(callback_query.data)
    books = []

    search_result = SearchResult(books, action.payload.prepared_collection_id)
    pages = PagesResult(search_result)

    page_index = action.payload.page_index
    
    keyboard = KeyboardController.create_pages_keyboard(pages, page_index)

    message = MessageController.preapare_page_message(pages.get_page(page_index))

    await bot.send_message(callback_query.message.from_user.id, message, reply_markup=keyboard)

    await callback_query.message.delete()


# if __name__ == '__main__':

def start():
    executor.start_polling(dp)
    BookService.finalize()
    QueryService.finalize()