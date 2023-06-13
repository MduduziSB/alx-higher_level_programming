#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: list
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	int lsize, i, alc;
	PyObject *pt;

	alc = ((PyListObject *)p)->allocated;
	lsize = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", lsize);
	printf("[*] Allocated = %d\n", alc);

	i = 0;
	while (i < lsize)
	{
		printf("Element %d: str\n", i);

		pt = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(pt)->tp_name);
		i++;
	}
}

