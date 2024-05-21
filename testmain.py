# # main.py
# import asyncio
# from central.api import main as central_main
# from connection.api import main as connection_main

# async def main():
#     await asyncio.gather(
#         central_main(),
#         connection_main()
#     )

# if __name__ == "__main__":
#     asyncio.run(main())










# import asyncio
# from control_input.api import main as control_input_main
# from keyboard.api import main as keyboard_main

# async def main():
#     # Запуск обработки сообщений от клавиатуры
#     await keyboard_main()

#     # Запуск обработки сообщений от контроля ввода
#     await control_input_main()

# if __name__ == "__main__":
#     asyncio.run(main())


import asyncio
from control_input.control_input import main as control_input_main
from battery_control.api import main as battery_main

async def main():
    # Запуск обработки сообщений от клавиатуры
    await battery_main()

    # Запуск обработки сообщений от контроля ввода
    await control_input_main()

if __name__ == "__main__":
    asyncio.run(main())
