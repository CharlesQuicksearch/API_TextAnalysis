import asyncio

from app.api.ai.ai_executions.detect_language import DetectLanguageExecution


class DetectLanguageHandler:
    def __init__(self, _input):
        self.input = _input
        self.procedure = DetectLanguageExecution()

    async def get_language(self):
        task = asyncio.create_task(self.procedure.run_procedure(self.input))
        language_result = await task
        return language_result
