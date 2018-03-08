# C# guidelines

TDB: Write C\# introduction

## Coding Style

## Rules

- Use four spaces identation.
- Use the
 [Rebracer Visual Studio extension](https://visualstudiogallery.msdn.microsoft.com/410e9b9f-65f3-4495-b68e-15567e543c58)
  and configure Rebracer.xml for the project solution.
- Use [implicit
  typing](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/implicitly-typed-local-variables)
  for local variables when the type of the variable is obvious from
  the right side of the assignment.
- Use implicit typing to determine the type of the loop variable in
  [for](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/for)
  and foreach
  [loops](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/foreach-in).
- Use
  [&&](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/conditional-and-operator)
  instead of
  [&](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/and-operator)
  and
  <https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/or-operator>
  when you perform comparisons.
- Constructor should require the parameters needed in order to
  completely setup an object, so that it's impossible to create an
  object in an invalid state.
- Use object initializers to simplify object creation.
- Add at least one blank line between method and property definitions.
- Start comment text with an uppercase letter, and end comment text
  with a period.
- Use StringBuilder for Fast String Creation.
- Do not throw exceptions from exception filter blocks.
- Throw exceptions from instance constructors, if appropriate.
- Use one of the following linting tools
  - [FxCop](http://msdn.microsoft.com/en-us/library/bb429476.aspx)
  - [Microsoft Code Analysis][mca]
  - [Resharper](http://www.jetbrains.com/resharper/)

[mca]: https://marketplace.visualstudio.com/items?itemName=VisualStudioPlatformTeam.MicrosoftCodeAnalysis2017

## Naming

1. **Classes** must be in `CamelCase`.
   ```c#
   class User {}
   ```

2. **Interfaces** must be in `CamelCase` and prefixed with I.
   ```c#
   interface IService {}
   ```

3. **Function/Method** must be in `CamelCase`.
   ```c#
   class User
   {
        private int GetPublicId()
        {
            ...
        }
   }
    ```
4. **Variables** must be in `camelCase`.
   ```c#
   string name = "this is a variable";
   ```
5. **Function/Method Parameters** must be in `camelCase`.
   ``` {.sourceCode .c#}
   int GetTest(string para, string longParam)
   {
       ...
   }
   ```
6. Do not prefix enums, classes, or delegates with any letter .

## Syntax

1. Use object intilization.
   ```c#
   ExampleClass element = new ExampleClass
   {
        Id = 1,
        Name = "Test",
        Location = "Sophilabs"
    };
    ```
1. If you are defining an event handler that you do not need to remove later, use a lambda
   expression.
   ```c#
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
   ```
1. Align query clauses under the from clause.
   ```c#
   var seattleCustomers2 = from cust in customers
                           where cust.City == "Seattle"
                           orderby cust.Name
                           select cust;
   ```
1. Use multiple from clauses instead of a join clause to access inner collections.
   ```c#
   var scoreQuery = from student in students
                    from score in student.Scores
                    where score > 90
                    select new { Last = student.LastName, score };
   ```

## References

1. [C# Code Style](https://msdn.microsoft.com/en-us/library/ff926074.aspx)
2. [Framework Design Guidelines](https://msdn.microsoft.com/en-us/library/ms229042.aspx)
3. [FxCop](http://msdn.microsoft.com/en-us/library/bb429476.aspx)
4. [Microsoft Code Analysis](https://marketplace.visualstudio.com/items?itemName=VisualStudioPlatformTeam.MicrosoftCodeAnalysis2017)
5. [Resharper](http://www.jetbrains.com/resharper/)
6. [C\# in Depth](http://csharpindepth.com/)
7. [C\# Programming Guide](https://msdn.microsoft.com/en-us/library/67ef8sbd.aspx/)