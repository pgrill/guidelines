C# guidelines
-------------

Books
=====

#. `C# in Depth  <http://csharpindepth.com/>`__
#. `C# Programming Guide  <https://msdn.microsoft.com/en-us/library/67ef8sbd.aspx/>`__

Coding Style
============

Rules
-----

#. Use four spaces identation.
#. Use the `Rebracer Visual Studio extension <https://visualstudiogallery.msdn.microsoft.com/410e9b9f-65f3-4495-b68e-15567e543c58>`__ and configure Rebracer.xml for the project solution.

Naming
------


#. **Classes** must be in ``CamelCase``.

    .. code-block:: c#

        class User {}

#. **Interfaces** must be in ``CamelCase`` and prefixed with I.

    .. code-block:: c#
    
        interface IService {}

#. **Function/Method** must be in ``CamelCase``.

    .. code-block:: c#
        
        class User
        {
            private int GetPublicId()
            {
                ...
            }
        }

#. **Variables** must be in ``camelCase``.

    .. code-block:: c#
        
        string name = "this is a variable";

#. **Function/Method Parameters** must be in ``camelCase``.

    .. code-block:: c#
    
        int GetTest(string para, string longParam)
        {
            ...
        }

#. Do not prefix enums, classes, or delegates with any letter .

Syntax
======

#. Use object intilization.

    .. code-block:: c#
    
        ExampleClass element = new ExampleClass { 
            Id = 1,
            Name = "Test", 
            Location = "Sophilabs"
        };

References
==========

1. `C# Code Style <https://msdn.microsoft.com/en-us/library/ff926074.aspx>`__ 
2. `Framework Design Guidelines <https://msdn.microsoft.com/en-us/library/ms229042.aspx>`__
