from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder as ikbuilder
from aiogram.fsm.state import State, StatesGroup

from lib.math import generate_math_problem_5_class
from lib.math import generate_math_problem_7_class
from lib.math import generate_math_problem_9_class

router = Router()

class level:
    def __init__(self, code, ru_text):
        self.code = code
        self.ru_text = ru_text

levels = [
    level("easy", "5 класс"),
    level("medium", "7 класс"),
    level("hard", "9 класс")
]

def math_btns():
    builder = ikbuilder()
    for l in levels:
        builder.button(
            text=f"{l.ru_text}", 
            callback_data=f"math_{l.code}")
    builder.adjust(1, 1)
    return builder.as_markup()

# Состояния для FSM
class MathState(StatesGroup):
    waiting_for_answer = State()

@router.message(Command('start'))
async def handle_command_start(message: types.Message):
    await message.answer("Выбери уровень/сложность задач", reply_markup=math_btns())
    

@router.callback_query(F.data.startswith("math_"))
async def math_callbacks(c: types.CallbackQuery,  state: FSMContext):
    data = c.data.split("_")[1:]
    code = data[0]

    problem, answer = None, None

    if code == levels[0].code:
        problem, answer = generate_math_problem_5_class()
    elif code == levels[1].code:
        problem, answer = generate_math_problem_7_class()
    elif code == levels[2].code:
        problem, answer = generate_math_problem_9_class()
    else:
        await c.answer("Неправильный ввод")
    # Сохраняем правильный ответ в состояние
    await state.update_data(correct_answer=answer)
    
    await c.message.answer(problem)
    await c.answer()
    
    # Переводим состояние в режим ожидания ответа
    await state.set_state(MathState.waiting_for_answer)


# Обработчик для ответов пользователя
@router.message(MathState.waiting_for_answer)
async def check_answer(message: types.Message, state: FSMContext):
    user_answer = message.text
    data = await state.get_data()
    correct_answer = data.get("correct_answer")
    
    if user_answer == str(correct_answer):
        await message.answer("Правильно! 🎉")
    else:
        await message.answer(f"Неправильно. Правильный ответ: {correct_answer}")
    
    # Сбрасываем состояние
    await state.clear()