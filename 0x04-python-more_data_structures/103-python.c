#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	unsigned char index, max_bytes;
	PyBytesObject *bytes_obj = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes_obj->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		max_bytes = 10;
	else
		max_bytes = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", max_bytes);
	for (index = 0; index < max_bytes; index++)
	{
		printf("%02hhx", bytes_obj->ob_sval[index]);
		if (index == (max_bytes - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_list - Prints information about a Python list object
 * @p: Pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
	int listSize, allocation, i;
	const char *elementType;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	listSize = var->ob_size;
	allocation = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", listSize);
	printf("[*] Allocated = %d\n", allocation);

	for (i = 0; i < listSize; i++)
	{
		elementType = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, elementType);
		if (strcmp(elementType, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
