"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot


# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        self.execute(r'C:\Users\lucas\OneDrive\Área de Trabalho\otPokemon New.lnk')
        if not self.find( "EncontrarBotão", matching=0.97, waiting_time=10000):
            self.not_found("EncontrarBotão")
        if not self.find( "iniciarjogo", matching=0.97, waiting_time=10000):
            self.not_found("iniciarjogo")
        self.click()
        if not self.find( "encontrararealogin", matching=0.97, waiting_time=10000):
            self.not_found("encontrararealogin")

        if not self.find( "usuario", matching=0.97, waiting_time=10000):
            self.not_found("usuario")
        self.click()
        self.paste('lucassenaandrade')

        if not self.find( "senha", matching=0.97, waiting_time=10000):
            self.not_found("senha")
        self.click()
        self.paste('lukinhas103')

        if not self.find( "entrar", matching=0.97, waiting_time=10000):
            self.not_found("entrar")
        self.enter()

        if not self.find( "mensagemdodia", matching=0.97, waiting_time=10000):
            self.not_found("mensagemdodia")
        self.enter()

        if not self.find( "acharchar", matching=0.97, waiting_time=10000):
            self.not_found("acharchar")

        if not self.find( "clicarOknovamente", matching=0.97, waiting_time=10000):
            self.not_found("clicarOknovamente")
        self.enter()

        if not self.find( "esperarcarregar", matching=0.97, waiting_time=10000):
            self.not_found("esperarcarregar")

        if not self.find( "roserade", matching=0.97, waiting_time=10000):
            self.not_found("roserade")
        self.right_click()

        for cont in range(100):

            if not self.find( "pescar", matching=0.97, waiting_time=10000):
                self.not_found("pescar")
            self.control_a()
            self.click()
            if not self.find( "encontrarpeixeverde", matching=0.97, waiting_time=20000):
                self.not_found("encontrarpeixeverde")
            if self.find( "encontrarpeixeverde", matching=0.97, waiting_time=20000):
                if not self.find( "pegapokemon", matching=0.97, waiting_time=10000):
                    self.not_found("pegapokemon")
                self.control_a()
                self.click()
                
                self.sleep(3)
                self.key_f3()
                self.key_f4()
                self.key_f6()
                self.key_f7()
                self.key_f8()
                self.key_f9()

            print('Pescas Concluidas:' + str(cont))

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
