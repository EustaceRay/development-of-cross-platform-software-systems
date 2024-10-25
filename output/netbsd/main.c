#include <Python.h>

int main(int argc, char *argv[]) {
	Py_Initialize();

    // Объявление переменной 'command' и её инициализация
	const char *command = "exec(open('pasart.py', encoding='utf-8').read())";

    // Выполнение Python-кода
	PyRun_SimpleString(command);

    // Завершение работы интерпретатора Python
	Py_Finalize();
	return 0;
}
