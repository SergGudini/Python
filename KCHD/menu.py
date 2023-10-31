from colorama import Fore, Style
from command import *


def run():
    while True:
        command = input(Fore.LIGHTBLUE_EX +
                        '----БИНАРНОЕ ДЕРЕВО----\n'
                        '1 - создать\n'
                        '2 - вывести на экран\n'
                        '3 - найти элемент\n'
                        '4 - удалить элемент\n'
                        '5 - вывести количество узлов\n'
                        '6 - выход\n' +
                        'Сделайте Ваш выбор: '
                        + Style.RESET_ALL)

        if command == '6':
            break

        if command == '1':
            print(Fore.GREEN + '\nСоздать бинарное дерево:' + Style.RESET_ALL)
            createBinaryTree()

        elif command == '2':
            print(Fore.GREEN + '\nВывести на экран:' + Style.RESET_ALL)
            printBinaryTree()

        elif command == '3':
            print(Fore.YELLOW + '\nНайти элемент:' + Style.RESET_ALL)
            findElementBinaryTree()

        elif command == '4':
            print(Fore.RED + '\nУдалить элемент:' + Style.RESET_ALL)
            deleteElementBinaryTree()

        elif command == '5':
            print(Fore.GREEN + '\nВывести количество узлов:' + Style.RESET_ALL)
            countNodeBinaryTree()

        else:
            print(Fore.RED + 'Команда не найдена' + Style.RESET_ALL)
