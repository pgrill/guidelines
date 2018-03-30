# Rust Guidelines

## Learning resources

* [rust-learning](https://github.com/ctjhoa/rust-learning) includes a bunch
  of links to blog posts, articles, videos, etc for learning Rust.

## Code Style

This is an excerpt from the [Rust code formatting RFCs](https://github.com/rust-lang-nursery/fmt-rfcs)

### Names

* Types shall be `PascalCase`,
* Enum variants shall be `PascalCase`,
* Struct fields shall be `snake_case`,
* Function and method names shall be `snake_case`,
* Local variables shall be `snake_case`,
* Macro names shall be `snake_case`,
* Constants (`const`s and immutable `static`s) shall be `SCREAMING_SNAKE_CASE`.
* When a name is forbidden because it is a reserved word (e.g., `crate`), use a
  trailing underscore to make the name legal (e.g., `crate_`).

#### Blocks

A block expression should have a newline after the initial `{` and before the
terminal `}`. Any qualifier before the block (e.g., `unsafe`) should always be
on the same line as the opening brace, and separated with a single space. The
contents of the block should be block indented:

```rust
fn block_as_stmt() {
    a_call();

    {
        a_call_inside_a_block();

        // a comment in a block
        the_value
    }
}

fn block_as_expr() {
    let foo = {
        a_call_inside_a_block();

        // a comment in a block
        the_value
    };
}

fn unsafe_block_as_stmt() {
    a_call();

    unsafe {
        a_call_inside_a_block();

        // a comment in a block
        the_value
    }
}
```

If a block has an attribute, it should be on its own line:

```rust
fn block_as_stmt() {
    #[an_attribute]
    {
        #![an_inner_attribute]

        // a comment in a block
        the_value
    }
}
```

Avoid writing comments on the same line as the braces.

An empty block should be written as `{}`.

#### Closures

Don't put any extra spaces before the first `|` , but put a space between the second `|` and the
expression of the closure. Between the `|`s, you should use function definition syntax, however,
elide types where possible.

Use closures without the enclosing `{}`, if possible.

#### Struct literals

If a struct literal is *small* it may be formatted on a single line. If not,
each field should be on it's own, block-indented line. There should be a
trailing comma in the multi-line form only. There should be a space after the
colon only.

There should be a space before the opening brace. In the single-line form there
should be spaces after the opening brace and before the closing brace.

```rust
Foo { field1, field2: 0 }
let f = Foo {
    field1,
    field2: an_expr,
};
```

Functional record update syntax is treated like a field, but it must never have
a trailing comma. There should be no space after `..`.

let f = Foo {
    field1,
    ..an_expr
};

#### Tuple literals

Use a single-line form where possible. There should not be spaces around the
parentheses. Where a single-line form is not possible, each element of the tuple
should be on it's own block-indented line and there should be a trailing comma.

```rust
(a, b, c)

let x = (
    a_long_expr,
    another_very_long_expr,
);
```

#### Tuple struct literals

There should be no space between the identifier and the opening parenthesis.
Otherwise, follow the rules for tuple literals, e.g., `Foo(a, b)`.

#### Enum literals

Follow the formatting rules for the various struct literals. Prefer using the
name of the enum as a qualifying name, unless the enum is in the prelude. E.g.,

```rust
Foo::Bar(a, b)
Foo::Baz {
    field1,
    field2: 1001,
}
Ok(an_expr)
```

#### Array literals

For simple array literals, avoid line breaking, no spaces around square
brackets, contents of the array should be separated by commas and spaces. If
using the repeating initialiser, there should be a space after the semicolon
only. Apply the same rules if using the `vec!` or similar macros (always use
square brackets here). Examples:

```rust
fn main() {
    [1, 2, 3];
    vec![a, b, c, d];
    let a = [42; 10];
}
```

If a line must be broken, prefer breaking only after the `;`, if possible.
Otherwise, follow the rules below for function calls. In any case, the contents
of the initialiser should be block indented and there should be line breaks
after the opening bracket and before the closing bracket:

```rust
fn main() {
    [
        a_long_expression();
        1234567890
    ]
    let x = [
        an_expression,
        another_expression,
        a_third_expression,
    ];
}
```

#### Array accesses, indexing, and slicing

No spaces around the square brackets, avoid breaking lines if possible, never
break a line between the target expression and the opening bracket. If the
indexing expression covers multiple lines, then it should be block indented and
there should be newlines after the opening brackets and before the closing
bracket. However, this should be avoided where possible.

Examples:

```rust
fn main() {
    foo[42];
    &foo[..10];
    bar[0..100];
    foo[4 + 5 / bar];
    a_long_target[
        a_long_indexing_expression
    ];
}
```

#### Unary operations

Do not include a space between a unary op and its operand (i.e., `!x`, not
`! x`). However, there must be a space after `&mut`. Avoid line-breaking
between a unary operator and its operand.

#### Binary operations

Do include spaces around binary ops (i.e., `x + 1`, not `x+1`) (including `=`).

For comparison operators, because for `T op U`, `&T op &U` is also implemented:
if you have `t: &T`, and `u: U`, prefer `*t op u` to `t op &u`. In general,
within expressions, prefer dereferencing to taking references.

Use parentheses liberally, do not necessarily elide them due to precedence.
Tools should not automatically insert or remove parentheses. Do not use spaces
to indicate precedence.

If line-breaking, put the operator on a new line and block indent. E.g.,

```rust
foo + bar + baz
    + qux + whatever
```

#### Control flow

Do not include extraneous parentheses for `if` and `while` expressions.

```rust
if true {
}
```

is better than

```rust
if (true) {
}
```

Do include extraneous parentheses if it makes an arithmetic or logic expression
easier to understand (`(x * 15) + (y * 20)` is fine)

#### Function calls

Do not put a space between the function name, and the opening parenthesis.

Do not put a space between an argument, and the comma which follows.

Do put a space between an argument, and the comma which precedes it.

Prefer not to break a line in the callee expression.

##### Single-line calls

Do not put a space between the function name and open paren, between the open
paren and the first argument, or between the last argument and the close paren.

Do not put a comma after the last argument.

```rust
foo(x, y, z)
```

##### Multi-line calls

If the function call is not *small*, it would otherwise over-run the max width,
or any argument or the callee is multi-line, then the call should be formatted
across multiple lines. In this case, each argument should be on it's own block-
indented line, there should be a newline after the opening parenthesis and
before the closing parenthesis, and there should be a trailing comma. E.g.,

```rust
a_function_call(
    arg1,
    a_nested_call(a, b),
)
```

#### Method calls

Follow the function rules for calling.

Do not put any spaces around the `.`.

```rust
x.foo().bar().baz(x, y, z);
```

#### Macro uses

Macros which can be parsed like other constructs should be formatted like those
constructs. For example, a macro use `foo!(a, b, c)` can be parsed like a
function call (ignoring the `!`), therefore it should be formatted following the
rules for function calls.

##### Special case macros

Macros which take a format string and where all other arguments are *small* may
be formatted with arguments before and after the format string on a single line
and the format string on its own line, rather than putting each argument on its
own line. For example,

```rust
println!(
    "Hello {} and {}",
    name1, name2,
);

assert_eq!(
    x, y,
    "x and y were not equal, see {}",
    reason,
);
```

#### Casts (`as`)

Put spaces before and after `as`:

```rust
let cstr = "Hi\0" as *const str as *const [u8] as *const std::os::raw::c_char;
```

#### Chains of fields and method calls

A chain is a sequence of field accesses and/or method calls. A chain may also
include the try operator. E.g., `a.b.c().d` or `foo?.bar().baz?`.

Prefer formatting on one line if possible, and the chain is *small*. If
formatting on multiple lines, each field access or method call in the chain
should be on it's own line with the line-break before the `.` and after any `?`.
Each line should be block-indented. E.g.,

```rust
let foo = bar
    .baz?
    .qux();
```

If the length of the last line of the first element plus it's indentation is
less than or equal to the indentation of the second line (and there is space),
then combine the first and second lines, e.g.,

```rust
x.baz?
    .qux()

let foo = x
    .baz?
    .qux();

foo(
    expr1,
    expr2,
).baz?
    .qux();
```

##### Multi-line elements

If any element in a chain is formatted across multiple lines, then that element
and any later elements must be on their own line. Earlier elements may be kept
on a single line. E.g.,

```rust
a.b.c()?.d
    .foo(
        an_expr,
        another_expr,
    )
    .bar
    .baz
```

Note there is block indent due to the chain and the function call in the above
example.

Prefer formatting the whole chain in mulit-line style and each element on one
line, rather than putting some elements on multiple lines and some on a single
line, e.g.,

```rust
// Better
self.pre_comment
    .as_ref()
    .map_or(false, |comment| comment.starts_with("//"))

// Worse
self.pre_comment.as_ref().map_or(
    false,
    |comment| comment.starts_with("//"),
)
```

#### Match

Prefer not to line-break inside the discriminant expression. There must always
be a line break after the opening brace and before the closing brace. The match
arms must be block indented once:

```rust
match foo {
    // arms
}

let x = match foo.bar.baz() {
    // arms
};
```

Use a trailing comma for a match arm if and only if not using a block.

Avoid splitting the left-hand side (before the `=>`) of a match arm where
possible. If the right-hand side of the match arm is kept on the same line,
never use a block (unless the block is empty).

If the right-hand side consists of multiple statements or has line comments or
the start of the line cannot be fit on the same line as the left-hand side, use
a block.

The body of a block arm should be block indented once.

Examples:

```rust
match foo {
    foo => bar,
    a_very_long_patten | another_pattern if an_expression() => {
        no_room_for_this_expression()
    }
    foo => {
        // A comment.
        an_expression()
    }
    foo => {
        let a = statement();
        an_expression()
    }
    bar => {}
    // Trailing comma on last item.
    foo => bar,
}
```

If the body is a single expression with no line comments and not a control flow
expression, then it may be started on the same line as the right-hand side. If
not, then it must be in a block. Example,

```rust
match foo {
    // A combinable expression.
    foo => a_function_call(another_call(
        argument1,
        argument2,
    )),
    // A non-combinable expression
    bar => {
        a_function_call(
            another_call(
                argument1,
                argument2,
            ),
            another_argument,
        )
    }
}
```

##### Line-breaking

Where it is possible to use a block form on the right-hand side and avoid
breaking the left-hand side, do that. E.g.

```rust
    // Assuming the following line does done fit in the max width
    a_very_long_pattern | another_pattern => ALongStructName {
        ...
    },
    // Prefer this
    a_very_long_pattern | another_pattern => {
        ALongStructName {
            ...
        }
    }
    // To splitting the pattern.
```

Never break after `=>` without using the block form of the body.

If the left-hand side must be split and there is an `if` clause, break before
the `if` and block indent. In this case, always use a block body and start the
body on a new line:

```rust
    a_very_long_pattern | another_pattern
        if expr =>
    {
        ...
    }
```

If required to break the pattern, put each clause of the pattern on its own
line, breaking before the `|`. If there is an `if` clause, then you must use the
above form:

```rust
    a_very_long_pattern
    | another_pattern
    | yet_another_pattern
    | a_forth_pattern => {
        ...
    }
    a_very_long_pattern
    | another_pattern
    | yet_another_pattern
    | a_forth_pattern
        if expr =>
    {
        ...
    }
```

If every clause in a pattern is *small*, but does not fit on one line, then the
pattern may be formatted across multiple lines with as many clauses per line as
possible. Again break before a `|`:

```rust
    foo | bar | baz
    | qux => {
        ...
    }
```

#### Combinable expressions

Where a function call has a single argument, and that argument is formatted
across multiple-lines, the outer call may be formatted as if it were a single-
line call. The same combining behaviour may be applied to any similar
expressions which have multi-line, block-indented lists of sub-expressions
delimited by parentheses (e.g., macros or tuple struct literals). E.g.,

```rust
foo(bar(
    an_expr,
    another_expr,
))

let x = foo(Bar {
    field: whatever,
});

foo(|param| {
    action();
    foo(param)
})
```

Such behaviour should extend recursively, however, tools may choose to limit the
depth of nesting.

Only where the multi-line sub-expression is a closure with an explicit block,
this combining behviour may be used where there are other arguments, as long as
all the arguments and the first line of the closure fit on the first line, the
closure is the last argument, and there is only one closure argument:

```rust
foo(first_arg, x, |param| {
    action();
    foo(param)
})
```

#### Ranges

Do not put spaces in ranges, e.g., `0..10`, `x..=y`, `..x.len()`, `foo..`.

When writing a range with both upper and lower bounds, if the line must be
broken, break before the range operator and block indent the second line:

```rust
a_long_expression
    ..another_long_expression
```

For the sake of indicating precedence, we recommend that if either bound is a
compound expression, then use parentheses around it, e.g., `..(x + 1)`,
`(x.f)..(x.f.len())`, or `0..(x - 10)`.

#### Hexadecimal literals

Hexadecimal literals may use upper- or lower-case letters, but they must not be
mixed within the same literal. Projects should use the same case for all
literals, but we do not make a recommendation for either lower- or upper-case.
Tools should have an option to convert mixed case literals to upper-case, and
may have an option to convert all literals to either lower- or upper-case.

### Formatting conventions

These formatting conventions are a work in progress, and may do anything they
like, up to and including eating your laundry.

#### Indentation

Use spaces, not tabs.

#### Blank lines

Separate items and statements by either zero or one blank lines (i.e., one or
two newlines). E.g,

```rust
fn foo() {
    let x = ...;

    let y = ...;
    let z = ...;
}

fn bar() {}
fn baz() {}
```

Formatting tools should make the bounds on blank lines configurable: there
should be separate minimum and maximum numbers of newlines between both
statements and (top-level) items (i.e., four options). As described above, the
defaults for both statements and items should be minimum: 1, maximum: 2.

#### Comments

The following guidelines are recommendations only, a mechanical formatter should
not change comments except to move them within a file. To be clear this means
changing the whitespace before a line comment or the whitespace before or after
a block comment.

Prefer line comments (`//`) to block comments (`/* ... */`).

When using line comments there should be a single space after the opening sigil.

When using single-line block comments there should be a single space after the
opening sigil and before the closing sigil. Multi-line block comments should
have a newline after the opening sigil and before the closing sigil.

Prefer to put a comment on its own line. Where a comment follows code, there
should be a single space before it. Where a block comment is inline, there
should be surrounding whitespace as if it were an identifier or keyword. There
should be no trailing whitespace after a comment. Examples:

```rust
// A comment on an item.
struct Foo { ... }

fn foo() {} // A comment after an item.

pub fn foo(/* a comment before an argument */ x: T) {...}
```

Comments should usually be complete sentences. Start with a capital letter, end
with a period (`.`). An inline block comment may be treated as a note without
punctuation.

Source lines which are entirely a comment should be limited to 80 characters
in length (including comment sigils, but excluding indentation) or the maximum
width of the line (including comment sigils and indentation), whichever is
smaller:

```rust
// This comment goes up to the ................................. 80 char margin.

{
    // This comment is .............................................. 80 chars wide.
}

{
    {
        {
            {
                {
                    {
                        // This comment is limited by the ......................... 100 char margin.
                    }
                }
            }
        }
    }
}
```

##### Doc comments

Prefer line comments (`///`) to block comments (`//* ... */`).

Prefer outer doc comments (`///` or `//*`), only use inner doc comments (`//!`
and `//*!`) to write module-level or crate-level documentation.

Doc comments should come before attributes.

#### Attributes

Put each attribute on its own line, indented to the indentation of its item.
In the case of inner attributes (`#!`), indent it to the inner indentation (the
indentation of the item + 1). Prefer outer attributes, where possible.

For attributes with argument lists, format like functions.

```rust
##[repr(C)]
##[foo(foo, bar)]
struct CRepr {
    #![repr(C)]
    x: f32,
    y: f32,
}
```

For attributes with an equal sign, there should be a single space before and
after the `=`, e.g., `#[foo = 42]`.

There must only be a single `derive` attribute. Note for tool authors: if
combining multiple `derive` attributes into a single attribute, the ordering of
the derived names should be preserved. E.g., `#[derive(bar)] #[derive(foo)]
struct Baz;` should be formatted to `#[derive(bar, foo)] struct Baz;`.

### Items

`extern crate` statements must be first in a file. They must be ordered
alphabetically.

`use` statements, and module *declarations* (`mod foo;`, not `mod { ... }`)
must come before other items. We recommend that imports come before module
declarations; if imports and modules are separated, then they should be ordered
alphabetically. When sorting, `self` and `super` must come before any other
names. Module declarations should not be moved if they are annotated with
`#[macro_export]`, since that may be semantics changing.

Tools should make the above ordering optional.

#### Function definitions

In Rust, one finds functions by searching for `fn [function-name]`; It's
important that you style your code so that it's very searchable in this way.

The proper ordering and spacing is:

```rust
[pub] [unsafe] [extern ["ABI"]] fn foo(arg1: i32, arg2: i32) -> i32 {
    ...
}
```

Avoid comments within the signature itself.

If the function signature does not fit on one line, then break after the opening
parenthesis and before the closing parenthesis and put each argument on its own
block-indented line. For example,

```rust
fn foo(
    arg1: i32,
    arg2: i32,
) -> i32 {
    ...
}
```

#### Tuples and tuple structs

Write the type list as you would a parameter list to a function.

Build a tuple or tuple struct as you would call a function.

##### Single-line

```rust
struct Bar(Type1, Type2);

let x = Bar(11, 22);
let y = (11, 22, 33);
```

#### Enums

In the declaration, put each variant on its own line, block indented.

Format each variant accordingly as either a struct, tuple struct, or identifier,
which doesn't require special formatting (but without the `struct` keyword.

```rust
enum FooBar {
    First(u32),
    Second,
    Error {
        err: Box<Error>,
        line: u32,
    },
}
```

#### Structs and Unions

Struct names follow on the same line as the `struct` keyword, with the opening
brace on the same line when it fits within the right margin. All struct fields
are indented once and end with a trailing comma. The closing brace is not
indented and appears on its own line.

```rust
struct Foo {
    a: A,
    b: B,
}
```

If and only if the type of a field does not fit within the right margin, it is
pulled down to its own line and indented again.

```rust
struct Foo {
    a: A,
    long_name:
        LongType,
}
```

#### Tuple structs

Put the whole struct on one line if possible. Types in the parentheses should be
separated by a comma and space with no trailing comma. No spaces around the
parentheses or semi-colon:

```rust
pub struct Foo(String, u8);
```

Prefer unit structs to empty tuple structs (these only exist to simplify code
generation), e.g., `struct Foo;` rather than `struct Foo();`.

For more than a few fields, prefer a proper struct with named fields. Given
this, a tuple struct should always fit on one line. If it does not, block format
the fields with a field on each line and a trailing comma:

```rust
pub struct Foo(
    String,
    u8,
);
```

#### Traits

Trait items should be block-indented. If there are no items, the trait may be
formatted on a single line. Otherwise there should be line-breaks after the
opening brace and before the closing brace:

```rust
trait Foo {}

pub trait Bar {
    ...
}
```

If the trait has bounds, there should be a space after the colon but not before
and before and after each `+`, e.g.,

```rust
trait Foo: Debug + Bar {}
```

Prefer not to line-break in the bounds if possible (consider using a `where`
clause). Prefer to break between bounds than to break any individual bound. If
you must break the bounds, put each bound (including the first) on its own
block-indented line, break before the `+` and put the opening brace on its own
line:

```rust
pub trait IndexRanges:
    Index<Range<usize>, Output=Self>
    + Index<RangeTo<usize>, Output=Self>
    + Index<RangeFrom<usize>, Output=Self>
    + Index<RangeFull, Output=Self>
{
    ...
}
```

#### Extern crate

`extern crate foo;`

Use spaces around keywords, no spaces around the semi-colon.

#### Modules

```rust
mod foo {
}
```

```rust
mod foo;
```

Use spaces around keywords and before the opening brace, no spaces around the
semi-colon.

#### macro\_rules

Use `{}` for the full definition of the macro.

```rust
macro_rules! foo {
}
```

#### Generics

Prefer to put a generics clause on one line. Break other parts of an item
declaration rather than line-breaking a generics clause. If a generics clause is
large enough to require line-breaking, you should prefer to use a `where` clause
instead.

Do not put spaces before or after `<` nor before `>`. Only put a space after `>`
if it is followed by a word or opening brace, not an opening parenthesis. There
should be a space after each comma and no trailing comma.

```rust
fn foo<T: Display, U: Debug>(x: Vec<T>, y: Vec<U>) ...

impl<T: Display, U: Debug> SomeType<T, U> { ...
```

If the generics clause must be formatted across multiple lines, each parameter
should have its own block-indented line, there should be newlines after the
opening bracket and before the closing bracket, and the should be a trailing
comma.

```rust
fn foo<
    T: Display,
    U: Debug,
>(x: Vec<T>, y: Vec<U>) ...
```

If an associated type is bound in a generic type, then there should be spaces on
either side of the `=`:

```rust
<T: Example<Item = u32>>
```

Prefer to use single-letter names for generic parameters.

#### `where` clauses

These rules apply for `where` clauses on any item.

A `where` clause may immediately follow a closing bracket of any kind.
Otherwise, it must start a new line, with no indent. Each component of a `where`
clause must be on its own line and be block indented. There should be a trailing
comma, unless the clause is terminated with a semicolon. If the `where` clause
is followed by a block (or assignment), the block should be started on a new
line. Examples:

```rust
fn function<T, U>(args)
where
    T: Bound,
    U: AnotherBound,
{
    body
}

fn foo<T>(
    args
) -> ReturnType
where
    T: Bound,
{
    body
}

fn foo<T, U>(
    args,
) where
    T: Bound,
    U: AnotherBound,
{
    body
}

fn foo<T, U>(
    args
) -> ReturnType
where
    T: Bound,
    U: AnotherBound;  // Note, no trailing comma.

type Foo<T>
where
    T: Bound
= Bar<T>;
```

If a `where` clause is very short, we recommend using an inline bound on the
type parameter.

If a component of a `where` clause is long, it may be broken before `+` and
further block indented. Each bound should go on its own line. E.g.,

```rust
impl<T: ?Sized, Idx> IndexRanges<Idx> for T
where
    T: Index<Range<Idx>, Output = Self::Output>
        + Index<RangeTo<Idx>, Output = Self::Output>
        + Index<RangeFrom<Idx>, Output = Self::Output>
        + Index<RangeInclusive<Idx>, Output = Self::Output>
        + Index<RangeToInclusive<Idx>, Output = Self::Output> + Index<RangeFull>
```

##### Option - `where_single_line`

`where_single_line` is `false` by default. If `true`, then a where clause with
exactly one component may be formatted on a single line if the rest of the
item's signature is also kept on one line. In this case, there is no need for a
trailing comma and if followed by a block, no need for a newline before the
block. E.g.,

```rust
// May be single-lined.
fn foo<T>(args) -> ReturnType
where T: Bound {
    body
}

// Must be multi-lined.
fn foo<T>(
    args
) -> ReturnType
where
    T: Bound,
{
    body
}
```

#### Type aliases

Type aliases should generally be kept on one line. If necessary to break the
line, do so after the `=`; the right-hand-side should be block indented:

```rust
pub type Foo = Bar<T>;

// If multi-line is required
type VeryLongType<T, U: SomeBound> =
    AnEvenLongerType<T, U, Foo<T>>;
```

Where possible avoid `where` clauses and keep type constraints inline. Where
that is not possible split the line before and after the `where` clause (and
split the `where` clause as normal), e.g.,

```rust
type VeryLongType<T, U>
where
    T: U::AnAssociatedType,
    U: SomeBound,
= AnEvenLongerType<T, U, Foo<T>>;
```

#### Associated types

Associated types should follow the guidelines above for type aliases. Where an
associated type has a bound, there should be a space after the colon but not
before:

```rust
    pub type Foo: Bar;
```

#### extern items

When writing extern items (such as `extern "C" fn`), always be explicit about
the ABI. For example, write `extern "C" fn foo ...`, not `extern fn foo ...`, or
`extern "C" { ... }.

### Overarching guidelines

Prefer block indent over visual indent. E.g.,

```rust
// Block indent
a_function_call(
    foo,
    bar,
);

// Visual indent
a_function_call(foo,
                bar);
```

This makes for smaller diffs (e.g., if `a_function_call` is renamed in the above
example) and less rightward drift.

Lists should have a trailing comma when followed by a newline, see the block
indent example above. This choice makes moving code (e.g., by copy and paste)
easier and makes smaller diffs.

#### Let statements

There should be spaces after the `:` and on both sides of the `=` (if they are
present). No space before the semi-colon.

```rust
// A comment.
let pattern: Type = expr;

let pattern;
let pattern: Type;
let pattern = expr;
```

If possible the declaration should be formatted on a single line. If this is not
possible, then try splitting after the `=`, if the declaration can fit on two
lines. The expression should be block indented.

```rust
let pattern: Type =
    expr;
```

If the first line does not fit on a single line, then split after the colon,
using block indentation. If the type covers multiple lines, even after line-
breaking after the `:`, then the first line may be placed on the same line as
the `:`, subject to the [combining rules](https://github.com/rust-lang-nursery/fmt-rfcs/issues/61) (WIP).

```rust
let pattern:
    Type =
    expr;
```

e.g,

```rust
let Foo {
    f: abcd,
    g: qwer,
}: Foo<Bar> =
    Foo { f, g };

let (abcd,
     defg):
    Baz =
{ ... }
```

If the expression covers multiple lines, if the first line of the expression
fits in the remaining space, it stays on the same line as the `=`, the rest of the
expression is not indented. If the first line does not fit, then it should start
on the next lines, and should be block indented. If the expression is a block
and the type or pattern cover multiple lines, then the opening brace should be
on a new line and not indented (this provides separation for the interior of the
block from the type), otherwise the opening brace follows the `=`.

Examples:

```rust
let foo = Foo {
    f: abcd,
    g: qwer,
};

let foo =
    ALongName {
        f: abcd,
        g: qwer,
    };

let foo: Type = {
    an_expression();
    ...
};

let foo:
    ALongType =
{
    an_expression();
    ...
};

let Foo {
    f: abcd,
    g: qwer,
}: Foo<Bar> = Foo {
    f: blimblimblim,
    g: blamblamblam,
};

let Foo {
    f: abcd,
    g: qwer,
}: Foo<Bar> = foo(
    blimblimblim,
    blamblamblam,
);
```

#### Macros in statement position

A macro use in statement position should use parentheses or square brackets as
delimiters and should be terminated with a semi-colon. There should be no spaces
between the name, `!`, the delimiters, or the `;`.

```rust
// A comment.
a_macro!(...);
```

#### Expressions in statement position

There should be no space between the expression and the semi-colon.

<expr>;

All expressions in statement position should be terminated with a semi-colon,
unless they end with a block or are used as the value for a block.

E.g.,

```rust
{
    an_expression();
    expr_as_value()
}

return foo();

loop {
    break;
}
```

Use a semi-colon where an expression has void type, even if it could be
propagated. E.g.,

```rust
fn foo() { ... }

fn bar() {
    foo();
}
```

### Types and Bounds

#### Single line formatting

* `[T]` no spaces
* `[T; expr]`, e.g., `[u32; 42]`, `[Vec<Foo>; 10 * 2 + foo()]` (space after colon,
  no spaces around square brackets)
* `*const T`, `*mut T` (no space after `*`, space before type)
* `&'a T`, `&T`, `&'a mut T`, `&mut T` (no space after `&`, single spaces separating other words)
* `unsafe extern "C" fn<'a, 'b, 'c>(T, U, V) -> W` or `fn()` (single spaces around keyowrds
   and sigils, and after commas, no trailing commas, no spaces around brackets)
* `!` should be treated like any other type name, `Name`
* `(A, B, C, D)` (spaces after commas, no spaces around parens, no trailing comma unless it is a one-tuple)
* `<Baz<T> as SomeTrait>::Foo::Bar` or `Foo::Bar` or `::Foo::Bar` (no spaces around `::` or angle
  brackets, single spaces around `as`)
* `Foo::Bar<T, U, V>` (spaces after commas, no trailing comma, no spaces around angle brackets)
* `T + T + T` (single spaces between types, and `+`).
* `impl T + T + T` (single spaces between keyword, types, and `+`).

Parentheses used in types should not be surrounded by whitespace, e.g., `(Foo)`

#### Line breaks

Avoid breaking lines in types where possible. Prefer breaking at outermost scope, e.g., prefer

```rust
Foo<
    Bar,
    Baz<Type1, Type2>,
>
```

to

```rust
Foo<Bar, Baz<
    Type1,
    Type2,
>>
```

`[T; expr]` may be broken after the `;` if necessary.

Function types may be broken following the rules for function declarations.

Generic types may be broken following the rules for generics.

Types with `+` may be broken after any `+` using block indent and breaking before the `+`.
When breaking such a type, all `+`s should be line broken, e.g.,

```rust
impl Clone
    + Copy
    + Debug

Box<
    Clone
    + Copy
    + Debug
>
```

## References

* [Rust code formatting RFCs](https://github.com/rust-lang-nursery/fmt-rfcs)