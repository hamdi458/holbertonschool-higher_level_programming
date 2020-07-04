#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer
 */
void print_python_list_info(PyObject *p)
{
	int size, x, i;
	PyObject *item;
	size = (((PyVarObject *)(p))->ob_size);
	printf("[*] Size of the Python List = %d\n", size);
	x = (((PyListObject *)(p))->allocated);
	printf("[*] Allocated = %d\n", x);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		item = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
