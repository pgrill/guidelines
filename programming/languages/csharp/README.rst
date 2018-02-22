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

* Use four spaces identation.
* Use the `Rebracer Visual Studio extension <https://visualstudiogallery.msdn.microsoft.com/410e9b9f-65f3-4495-b68e-15567e543c58>`__  and configure Rebracer.xml for the project solution.
* Use `implicit typing <https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/implicitly-typed-local-variables>`__ for local variables when the type of the variable is obvious from the right side of the assignment.
* Use implicit typing to determine the type of the loop variable in `for <https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/for>`__ and foreach `loops <https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/foreach-in>`__.
* Use `&& <https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/conditional-and-operator>`__ instead of `& <https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/and-operator>`__ and `|| <https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/conditional-or-operator>`__ instead of `| <https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/or-operator>`__ when you perform comparisons.
* Constructor should require the parameters needed in order to completely setup an object, so that it's impossible to create an object in an invalid state.
* Use object initializers to simplify object creation.
* Add at least one blank line between method and property definitions.
* Start comment text with an uppercase letter, and end comment text with a period.
* Use StringBuilder for Fast String Creation.
* Do not throw exceptions from exception filter blocks.
* Throw exceptions from instance constructors, if appropriate.
* Use one of the following linting tools `FxCop <http://msdn.microsoft.com/en-us/library/bb429476.aspx>`__ - `Microsoft Code Analysis <https://marketplace.visualstudio.com/items?itemName=VisualStudioPlatformTeam.MicrosoftCodeAnalysis2017>`__ - `Resharper <http://www.jetbrains.com/resharper/>`__

------

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
        ExampleClass element = new ExampleClass 
        { 
            Id = 1,
            Name = "Test",
            Location = "sophilabs"
        };

#. If you are defining an event handler that you do not need to remove later, use a lambda expression.
    
    .. code-block:: c#
    
        public Form2()
        {
            // You can use a lambda expression to define an event handler.
            this.Click += (s, e) =>
                {
                    MessageBox.Show(
                        ((MouseEventArgs)e).Location.ToString());
                };
        }

        // Using a lambda expression shortens the following traditional definition.
        public Form1()
        {
            this.Click += new EventHandler(Form1_Click);
        }

        void Form1_Click(object sender, EventArgs e)
        {
            MessageBox.Show(((MouseEventArgs)e).Location.ToString());
        }
      
#. Align query clauses under the from clause.
    
    .. code-block:: c#
    
        var seattleCustomers2 = from cust in customers
                                where cust.City == "Seattle"
                                orderby cust.Name
                                select cust;
 
#. Use multiple from clauses instead of a join clause to access inner collections.
    
    .. code-block:: c#
    
        var scoreQuery = from student in students
                         from score in student.Scores
                         where score > 90
                         select new { Last = student.LastName, score };
                         

References
==========

1. `C# Code Style <https://msdn.microsoft.com/en-us/library/ff926074.aspx>`__
2. `Framework Design Guidelines <https://msdn.microsoft.com/en-us/library/ms229042.aspx>`__
3. `FxCop <http://msdn.microsoft.com/en-us/library/bb429476.aspx>`__  
4. `Microsoft Code Analysis <https://marketplace.visualstudio.com/items?itemName=VisualStudioPlatformTeam.MicrosoftCodeAnalysis2017>`__
5. `Resharper <http://www.jetbrains.com/resharper/>`__
