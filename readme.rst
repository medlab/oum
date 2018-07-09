oum
======================================================
UI automation <==> object auto map which work with selenium engine(winium: https://github.com/medlab/winium-super-build), focus on Win32/WinForm/WPF

Tutorial
======================================================

Ui contract
------------------------------------------------------
.. include:: oum/uiapps/uiacontractfortest.py
    :code: python

Ui PageObject
------------------------------------------------------
.. include:: oum/uiapps/uiacontractfortest.py
    :code: python

Test Sample
------------------------------------------------------
.. include:: oum/tests/hello_test.py
    :code: python

Release to pypi workflow
======================================================
1. setup.py sdist
2. twine upload dist/*

Refs
=======================================================
1. https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/
2. https://github.com/medlab/winium-super-build
