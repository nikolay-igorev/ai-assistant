#!/usr/bin/env python3

from __future__ import annotations

import os
import time

from yandex_cloud_ml_sdk import YCloudML


def main() -> None:
    os.system('cls')

    sdk = YCloudML(folder_id="<идентификатор_каталога>", auth="<API-ключ>")

    start_connection_assistant = time.time()
    assistant = sdk.assistants.get('fvtd1b90ftt1sibhvcjq')
    time_connection_assistant = time.time() - start_connection_assistant
    time_first_text_assistant = 1000

    thread = sdk.threads.create()

    thread.write("Расскажи всё, что знаешь про Бали. Важно очень много текста.")
    run = assistant.run_stream(thread)
    i = 0
    for event in run:
        os.system('cls')
        if i == 0:
            time_first_text_assistant = time.time() - start_connection_assistant
        i += 1
        print(f'{event.text}')
        time.sleep(0.01)

    print(f'Время подключения к ассистенту: {time_connection_assistant}')
    print(f'Время до получения первой части текста": {time_first_text_assistant}')

    thread.delete()


if __name__ == '__main__':
    main()
