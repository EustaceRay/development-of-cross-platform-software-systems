#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // ������������� Python
    Py_Initialize();

    // ��������, ��������������� �� ������������� Python
    if (!Py_IsInitialized()) {
        fprintf(stderr, "�� ������� ���������������� ������������� Python!\n");
        return 1;
    }

    // ���� � ����� pasart.py
    const char *scriptName = "./pasart.py";

    // ���������� �������� �������� � ����
    PyObject *sysPath = PySys_GetObject("path");
    PyObject *path = PyUnicode_FromString(".");
    PyList_Append(sysPath, path);
    Py_DECREF(path);

    // ������� ������� � ��������� ������
    FILE* file = fopen(scriptName, "r");
    if (file) {
        PyRun_SimpleFile(file, scriptName);
        fclose(file);
    } else {
        fprintf(stderr, "�� ������� ������� ���� %s\n", scriptName);
    }

    // ���������� ������ Python
    Py_Finalize();
    return 0;
}