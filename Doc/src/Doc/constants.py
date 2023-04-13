from dataclasses import dataclass


@dataclass(frozen=True)
class Block:
    tu: str     # ТУ
    iclg: str   # ИЦЛГ
    name: str
    latin_name: str
    fullname: str
    test_devices: str    # испытательные приборы
    measure_devices: str    # измерительные приборы


@dataclass(frozen=True)
class People:
    name: str   # имя
    job: str    # должность
    division: str   # отдел


@dataclass(frozen=True)
class Meter:
    name: str   # название прибора
    data: str    # срок действия метрологической аттестации


meter = {
    'Э515': Meter(
        name='Вольтметр Э515',
        data='«11» апреля 2023г',
    ),
    'УПУ-22': Meter(
        name='Установка высоковольтная измерительная (испытательная )УПУ-22',
        data='«11»мая 2023г',
    ),
    'UTB139B': Meter(
        name='Мультиметр цифровой UTB139B',
        data='«11»апреля 2023г',
    ),
    'М1102/1': Meter(
        name='Мегаомметр М1102/1',
        data='«03» сентября 2023г',
    ),
    'К121': Meter(
        name='Осциллограф светолучевой К121',
        data='«21» сентября 2023г',
    ),
    'Штанг': Meter(
        name='Штангенциркуль ШЦЦ I-300 0.01',
        data='«21» сентября 2023г',
    ),
    'Весы': Meter(
        name='Весы AD-05',
        data='«04» апреля 2023г',
    ),
}

device = {
    'BKCU': Block(
        tu='ВY 690376244.001-2012',
        iclg='ИЦЛГ 656119.0011',
        name='БКЦУ-4И-5',
        fullname='Блок контроля цепей управления искробезопасный БКЦУ-4И-5',
        test_devices=f"{meter['Э515'].name} ({meter['Э515'].data}.)",
        measure_devices=f"{meter['М1102/1'].name} ({meter['М1102/1'].data}.)\n"
                        f"{meter['К121'].name} ({meter['К121'].data}.)\n"
                        f"{meter['Штанг'].name} ({meter['Штанг'].data}.)\n"
                        f"{meter['Весы'].name} ({meter['Весы'].data}.)\n",
        latin_name='BKCU',
    ),
    'BKIR1': Block(
        tu='ВY 690376244.007-2019',
        iclg='__________________',
        name='БКИР-1',
        fullname='Блок контроля изоляции регулируемый БКИР-1',
        latin_name='BKIR1',
        test_devices=f"{meter['Э515'].name} ({meter['Э515'].data}.)",
        measure_devices=f"{meter['М1102/1'].name} ({meter['М1102/1'].data}.)\n"
                        f"{meter['К121'].name} ({meter['К121'].data}.)\n"
                        f"{meter['Штанг'].name} ({meter['Штанг'].data}.)\n"
                        f"{meter['Весы'].name} ({meter['Весы'].data}.)\n",

    ),
    'BI1XDSL': Block(
        tu='ВY 690376244.012-2019',
        iclg='ИЦЛГ 3.12.001.00.00.0.000',
        name='БИ-1-xDSL',
        fullname='Барьер искрозащиты БИ-1-xDSL',
        latin_name='BI1XDSL',
        test_devices=f"{meter['УПУ-22'].name} ({meter['УПУ-22'].data}.)",
        measure_devices=f"{meter['UTB139B'].name} ({meter['UTB139B'].data}.)\n"
                        f"{meter['Штанг'].name} ({meter['Штанг'].data}.)\n"
                        f"{meter['Весы'].name} ({meter['Весы'].data}.)\n",
    ),
    'UKU2S2': Block(
        tu='BY 690376244.011-2019',
        iclg='ИЦЛГ 3.03.003.00.00.0.000',
        name='УКУ-2С-2',
        fullname='Устройство контроля уровня УКУ-2С-2',
        latin_name='UKU2S2',
        test_devices=f"{meter['УПУ-22'].name} ({meter['УПУ-22'].data}.)",
        measure_devices=f"{meter['UTB139B'].name} ({meter['UTB139B'].data}.)\n"
                        f"{meter['К121'].name} ({meter['К121'].data}.)\n"
                        f"{meter['Штанг'].name} ({meter['Штанг'].data}.)\n"
                        f"{meter['Весы'].name} ({meter['Весы'].data}.)\n",
    ),
    'UKU2S1': Block(
        tu='BY 690376244.011-2019',
        iclg='ИЦЛГ 3.03.003.00.00.0.000',
        name='УКУ-2С-1',
        fullname='Устройство контроля уровня УКУ-2С-1',
        latin_name='UKU2S1',
        test_devices=f"{meter['УПУ-22'].name} ({meter['УПУ-22'].data}.)",
        measure_devices=f"{meter['UTB139B'].name} ({meter['UTB139B'].data}.)\n"
                        f"{meter['К121'].name} ({meter['К121'].data}.)\n"
                        f"{meter['Штанг'].name} ({meter['Штанг'].data}.)\n"
                        f"{meter['Весы'].name} ({meter['Весы'].data}.)\n",
    ),
    'BTZ1MK': Block(
        tu='BY 690376244.003-2014',
        iclg='__________________',
        name='БТЗ-1МК',
        fullname='Блок токовых защит микропроцессорный БТЗ-1МК',
        latin_name='BTZ1MK',
        test_devices=f"{meter['Э515'].name} ({meter['Э515'].data}.)",
        measure_devices=f"{meter['М1102/1'].name} ({meter['М1102/1'].data}.)\n"
                        f"{meter['К121'].name} ({meter['К121'].data}.)\n"
                        f"{meter['Штанг'].name} ({meter['Штанг'].data}.)\n"
                        f"{meter['Весы'].name} ({meter['Весы'].data}.)\n",
    ),
    'BSD61': Block(
        tu='BY 690376244.005-2019',
        iclg='__________________',
        name='БСД-6-1',
        fullname='Блок сбора данных БСД-6-1',
        latin_name='BSD61',
        test_devices=f"{meter['Э515'].name} ({meter['Э515'].data}.)",
        measure_devices=f"{meter['М1102/1'].name} ({meter['М1102/1'].data}.)\n"
                        f"{meter['К121'].name} ({meter['К121'].data}.)\n"
                        f"{meter['Штанг'].name} ({meter['Штанг'].data}.)\n"
                        f"{meter['Весы'].name} ({meter['Весы'].data}.)\n",
    ),
}

people = {
    'директор': People(
        name='Ильичев Д.В.',
        job='директор',
        division='',
    ),
    'гл инженер': People(
        name='Плехан В.Л.',
        job='главный инженер',
        division='',
    ),
    'ОТК': People(
        name='Лазовский А.И.',
        job='инженер ОТК',
        division='',
    ),
    'я': People(
        name='Царюк Ю.Л.',
        job='инженер-электроник',
        division='',
    ),
    'ЦИ': People(
        name='Зеневич А.О.',
        job='',
        division='',
    ),
    'ИИЛ': People(
        name='Родько В.А.',
        job='',
        division='',
    ),
}

list_devices = [i.name for i in device.values()]
list_devices_class = [i for i in device]
dict_devices = dict(zip(list_devices, list_devices_class))


if __name__ == '__main__':
    pass
