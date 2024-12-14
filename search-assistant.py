#!/usr/bin/python
# -*- coding: utf8 -*-
import os
import time
import asyncio

from yandex_cloud_ml_sdk import AsyncYCloudML

assistant_info = """
Ты специалист по IT. 
Ты даёшь советы как стать хорошим ML-инженером новичкам, 
но при этом всегда с чувством юмора. Постоянно шутишь.
"""


async def create_assistant(sdk: AsyncYCloudML, instruction: str):
    assistant = await sdk.assistants.create(
        'yandexgpt',
        ttl_days=5,
        expiration_policy='static',
        instruction=instruction,
        temperature=0.5,
        max_prompt_tokens=500,
    )
    print(f'ID ассистента: {assistant.id}')
    return assistant.id


async def ask(sdk: AsyncYCloudML, assistant_id: str, question: str):
    start_connection_assistant = time.time()
    assistant = await sdk.assistants.get(assistant_id)
    time_connection_assistant = time.time() - start_connection_assistant
    time_first_text_assistant = 1000

    thread = await sdk.threads.create()
    await thread.write(question)

    i = 0
    run = await assistant.run_stream(thread=thread)
    async for event in run:
        os.system('cls')
        if i == 0:
            time_first_text_assistant = time.time() - start_connection_assistant
        i += 1
        print(f'{event.text}')
        time.sleep(0.01)

    print(f'Время подключения к ассистенту: {time_connection_assistant}')
    print(f'Время до получения первой части текста": {time_first_text_assistant}')

    await thread.delete()


async def main() -> None:
    os.system('cls')

    sdk = AsyncYCloudML(folder_id="<идентификатор_каталога>", auth="<API-ключ>")

    assistant_id = await create_assistant(sdk, assistant_info)
    # assistant_id = "fvthb5vnourqlk3ip0kb"

    await ask(sdk, assistant_id, "Расскажи всё, про инструкции для AI ассистента. Важно очень много текста.")


if __name__ == '__main__':
    asyncio.run(main())
