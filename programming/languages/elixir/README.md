# Elixir guidelines

## Learning Resources

- [Elixir getting started](https://elixir-lang.org/getting-started/introduction.html)
- [Elixir learning resources](https://elixir-lang.org/learning.html)
- [Elixir School](https://elixirschool.com/en/)

## Coding Style

### Rules

- Use two spaces per indentation level

```elixir
# not preferred - four spaces
def some_function do
    do_something
end

# preferred
def some_function do
    do_something
end
```

- Use spaces around operators, after commas, colons and semicolons. Do not put spaces around matched
  pairs like brackets, parentheses, etc. Whitespace might be (mostly) irrelevant to the Elixir runtime,
  but its proper use is the key to writing easily readable code.

```elixir
sum = 1 + 2
{a, b} = {2, 3}
[first | rest] = [1, 2, 3]
Enum.map(["one", <<"two">>, "three"], fn num -> IO.puts(num) end)
```

- Do not use spaces after non-word operators that only take one argument; or around the range operator.

```elixir
0 - 1 == -1
^pinned = some_func()
5 in 1..10
```

- Use blank lines between defs to break up a function into logical paragraphs.

```elixir
def some_function(some_data) do
  some_data |> other_function() |> List.first()
end

def some_function do
  result
end

def some_other_function do
  another_result
end

def a_longer_function do
  one
  two

  three
  four
end
```

- Use parentheses for one-arity functions when using the pipe operator (`|>`).

```elixir
# not preferred
some_string |> String.downcase |> String.strip

# preferred
some_string |> String.downcase() |> String.strip()
```

- Use the pipe operator to chain functions together.

```elixir
# not preferred
String.strip(String.downcase(some_string))

# preferred
some_string |> String.downcase() |> String.strip()

# Multiline pipelines are not further indented
some_string
|> String.downcase()
|> String.strip()

# Multiline pipelines on the right side of a pattern match
# should be indented on a new line
sanitized_string =
  some_string
  |> String.downcase()
  |> String.strip()
```

- Avoid using the pipe operator just once.

```elixir
# not preferred
some_string |> String.downcase()

# preferred
String.downcase(some_string)
```

- Another rules can be fount in [Elixir Guidelines](https://github.com/christopheradams/elixir_style_guide#syntax)

### Naming Conventions

- Use `snake_case` for atoms, functions and variables.

```elixir
# not preferred
:"some atom"
:SomeAtom
:someAtom

someVar = 5

def someFunction do
  ...
end

# preferred
:some_atom

some_var = 5

def some_function do
  ...
end
```

- Use `CamelCase` for modules (keep acronyms like HTTP, RFC, XML uppercase).

```elixir
# not preferred
defmodule Somemodule do
  ...
end

defmodule Some_Module do
  ...
end

defmodule SomeXml do
  ...
end

# preferred
defmodule SomeModule do
  ...
end

defmodule SomeXML do
  ...
end
```

- The names of predicate macros (compile-time generated functions that return a
  boolean value) _that can be used within guards_ should be prefixed with `is_`.
  For a list of allowed expressions, see the [Guard][Guard Expressions] docs.

```elixir
defmacro is_cool(var) do
  quote do: unquote(var) == "cool"
end
```

- The names of predicate functions _that cannot be used within guards_ should have a trailing question mark (`?`) rather than the `is_` (or similar) prefix.

```elixir
def cool?(var) do
  # Complex check if var is cool not possible in a pure function.
end
```

- Private functions with the same name as public functions should start with `do_`.

```elixir
def sum(list), do: do_sum(list, 0)

# private functions
defp do_sum([], total), do: total
defp do_sum([head | tail], total), do: do_sum(tail, head + total)
```

## Resources

- [Awesome Elixir](https://github.com/h4cc/awesome-elixir)

## References

- [Elixir Style Guide](https://github.com/christopheradams/elixir_style_guide)