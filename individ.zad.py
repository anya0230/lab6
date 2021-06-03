#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Использовать словарь, содержащий следующие ключи: название пункта назначения; номер поезда; время отправления. Написать программу, выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны быть упорядочены по номерам поездов; вывод на экран информации о поезде, номер которого введен с клавиатуры; если таких поездов нет, выдать на дисплей соответствующее сообщение

import sys

if __name__ == '__main__':
    # Список .
    train = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные .
            race = input("Название пункта назначения")
            number = input("Номер поезда ")
            type = float(input("время отправления "))

            # Создать словарь.
            airport = {
                'race': race,
                'number': number,
                'type': type,
            }

            # Добавить словарь в список.
            train.append(train)
            # Отсортировать список в случае необходимости.
            if len(train) > 1:
                train.sort(key=lambda item: item.get('race', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "No",
                    "Пункт",
                    "Номер",
                    "Время."
                )
            )
            print(line)

            # Вывести данные о всех рейсах.
            for idx, trains in enumerate(train, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                        idx,
                        trains.get('race', ''),
                        trains.get('number', ''),
                        trains.get('type', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            sel = (parts[1])

            count = 0
            for trains in train:
                if trains.get('race') == sel:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, trains.get('race', ''))
                    )
                    print('Номер поезда:', trains.get('number', ''))
                    print('Время отправления:', trains.get('type', ''))

            # Если счетчик равен 0, то рейсы не найдены.
            if count == 0:
                print("Поезд не найден.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <товар> - информация о поезде;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print("Неизвестная команда {command}", file=sys.stderr)