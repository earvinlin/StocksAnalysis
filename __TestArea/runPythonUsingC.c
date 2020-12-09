#include <Python.h>

int main(void) 
{
    Py_Initialize();
    PyRun_SimpleString("x= 'brave ' + 'sir robin'");

    return 0;
}