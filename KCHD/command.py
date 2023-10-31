from colorama import Fore, Style
from binary_tree import BinaryTree
from node import Node

bt = BinaryTree()


def createBinaryTree():
    """
       Функция заполнения бинарного дерева числовыми значениями пользователя
    """
    s = input("Введите список чисел, разделенных пробелами: ")
    lst = s.split()
    for x in lst:
        bt.add(int(x))


def printBinaryTree():
    """
       Функция вывода на экран бинарного дерева с отображением узлов
    """
    current = bt.root
    if bt.root is None:
        print(Fore.RED + 'Бинарное дерево пусто!' + Style.RESET_ALL)
        return
    Node.display(bt.root)
    print("Узлы бинарного дерева: ")
    while current is not None:
        print(current.value),
        current = current.right


def findElementBinaryTree():
    """
       Функция поиска элемента введённого пользователем
    """
    se = int(input("Введите число, которое хотите найти: "))
    print(bt.search(se))


def deleteElementBinaryTree():
    """
       Функция удаления элемента введённого пользователем
    """
    delete_val = int(input("Введите значение, которое необходимо удалить: "))
    print(bt.delete(delete_val))


def countNodeBinaryTree():
    """
       Функция вывода на экран количества узлов в дереве
    """
    print("Кол-во узлов в дереве: ", bt.countNodes())
