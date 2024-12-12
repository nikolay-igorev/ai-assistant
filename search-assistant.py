#!/usr/bin/env python3

from __future__ import annotations

import os
import time

from yandex_cloud_ml_sdk import YCloudML


def main() -> None:
    os.system('cls')

    sdk = YCloudML(folder_id="<идентификатор_каталога>", auth="<API-ключ>")

    start_connection_assistant = time.time()
    assistant = sdk.assistants.get('<Assistant ID>')
    time_connection_assistant = time.time() - start_connection_assistant

    thread = sdk.threads.create()

    thread.write("Что такое Казахстан?")
    run = assistant.run_stream(thread)
    for event in run:
        os.system('cls')
        print(f'{event.text}')
        time.sleep(0.5)

    print(f'Время подключения к ассистенту: {time_connection_assistant}')

    thread.delete()


if __name__ == '__main__':
    main()
