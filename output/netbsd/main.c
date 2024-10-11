#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // Инициализация Python
    Py_Initialize();

    // Проверка, инициализирован ли интерпретатор Python
    if (!Py_IsInitialized()) {
        fprintf(stderr, "Не удалось инициализировать интерпретатор Python!\n");
        return 1;
    }

    // Путь к файлу pasart.py
    const char *scriptName = "./pasart.py";

    // Добавление текущего каталога в путь
    PyObject *sysPath = PySys_GetObject("path");
    PyObject *path = PyUnicode_FromString(".");
    PyList_Append(sysPath, path);
    Py_DECREF(path);

    // Попытка открыть и выполнить скрипт
    FILE* file = fopen(scriptName, "r");
    if (file) {
        PyRun_SimpleFile(file, scriptName);
        fclose(file);
    } else {
        fprintf(stderr, "Не удалось открыть файл %s\n", scriptName);
    }

    // Завершение работы Python
    Py_Finalize();
    return 0;
}
