#include <Python.h>

int main(int argc, char *argv[]) {
	Py_Initialize();

    // ���������� ���������� 'command' � � �������������
	const char *command = "exec(open('pasart.py', encoding='utf-8').read())";

    // ���������� Python-����
	PyRun_SimpleString(command);

    // ���������� ������ �������������� Python
	Py_Finalize();
	return 0;
}
