import asyncio
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from datetime import datetime, timedelta
from .constants import device, list_devices, dict_devices
from .rundoc import documents, exel_logger, isint
import os


now = datetime.now()

data_pick = datetime.strftime(now - timedelta(days=14), "%d/%m/%Y")  # дата отбора изделия
start_data = datetime.strftime(now - timedelta(days=7), "%d/%m/%Y")  # дата начала испытаний
end_data = start_data  # дата окончания испытаний
data_exp_device = datetime.strftime(
    (now - timedelta(days=7)).replace(year=now.year + 1), "%d/%m/%Y")  # дата окончания действия испытаний

dir = os.getcwd()
dir_file = os.path.basename(__file__)
dir_folder = os.path.abspath(__file__).replace(dir_file, '')
os.chdir(dir_folder)

class HelloWorld(toga.App):
    def startup(self):
        self.progress = toga.ProgressBar(max=100, value=0)

        # ввод серийного номера
        serial_number_label = toga.Label("СЕРИЙНЫЙ НОМЕР: ", style=Pack(padding=(0, 5)))
        self.serial_number_input = toga.TextInput(style=Pack(flex=1))
        self.serial_number_input.style.update(flex=1, padding_right=485)
        serial_number_box = toga.Box(style=Pack(direction=ROW, padding=5))
        serial_number_box.add(serial_number_label, self.serial_number_input)
        serial_number_box.style.update(direction=ROW, padding=5)

        # выбор устройства
        block_chooser_label = toga.Label("ВЫБРАТЬ ДЕВАЙС: ", style=Pack(padding=(0, 5)))
        self.block_chooser = toga.Selection(items=[''] + list_devices)
        self.block_chooser.style.update(flex=1, padding_right=500)
        block_chooser_box = toga.Box(style=Pack(direction=ROW, padding=5))
        block_chooser_box.add(block_chooser_label, self.block_chooser)
        block_chooser_box.style.update(direction=ROW, padding=5)

        # кнопка выполнить
        self.button = toga.Button("ПОЕХАЛИ!", on_press=self.result_window, style=Pack(padding=5))

           # главный контенйер
        main_box = toga.Box(style=Pack(direction=COLUMN))
        main_box.style.update(direction=COLUMN, padding=5)
        main_box.add(serial_number_box, block_chooser_box, self.button, self.progress)

        # главное окно
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    async def result_window(self, widget):
        outer_box = toga.Box()
        self.result_window = toga.Window(size=(100, 100), resizeable=False, minimizable=False)
        self.windows.add(self.result_window)
        self.result_window.content = outer_box
        if isint(self.serial_number_input.value) and self.block_chooser.value:
            try:
                self.progress.value = 0
                await self.make_doc()
                self.progress.value = 100
                os.startfile(dir_folder)
                await asyncio.sleep(1)
                self.result_window.info_dialog('!!!ВЫПОЛНЕНО!!!', 'ПРОДЕЛАНО')
                self.serial_number_input.value = ''
                self.block_chooser.value = ''
            except Exception as e:
                print(e)
                self.result_window.info_dialog('!!!ПРОБЛЕМА С ШАБЛОНОМ!!!', 'ОТСУТСТВУЕТ ИЛИ НЕВЕРНОЕ ИМЯ ШАБЛОНА')

        else:
            self.result_window.info_dialog('!!!ПРОБЛЕМА С ДАННЫМИ!!!', 'ВВЕДИТЕ ЗАВ. НОМЕР ИЛИ ВЫБЕРИТЕ ДЕВАЙС\n'
                                                                      'ЗАВ. НОМЕР - ЦЕЛОЕ ЧИСЛО')

    async def make_doc(self):
        doc_number = exel_logger(
            data=datetime.strftime(now, "%d/%m/%Y"),
            serial=self.serial_number_input.value,
            block=self.block_chooser.value,
        )
        documents(
            device=device[dict_devices[self.block_chooser.value]],
            device_number=self.serial_number_input.value,   # серийный номер устройства
            periodic_number=f'П{doc_number}',  # номер протокола периодических испытаний
            data_pick=data_pick,  # дата отбора изделия
            start_data=start_data,  # дата начала испытаний
            end_data=end_data,  # дата окончания испытаний
            data_exp_device=data_exp_device,  # дата окончания действия испытаний
            result_number=f'А{doc_number}',  # номер акта результата периодических испытаний
        )


def main():
    return HelloWorld()
