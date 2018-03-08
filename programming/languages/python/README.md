# Python Guidelines

## Resources

1.Test your [regular expressions](https://pythex.org)
2.Stay up to date: [Python Weekly](https://www.pythonweekly.com/)

## Rules

- Use 4 spaces for indentation.
- Please conform to the indentation style dictated in the
  .editorconfig file. We recommend using a text editor with
  EditorConfig support to avoid indentation and whitespace issues.
- Follow [PEP8](https://www.python.org/dev/peps/pep-0008/). Use
  [flake8](https://pypi.python.org/pypi/flake8) to check for problems
  in this area.
- In docstrings, follow [PEP 257](https://www.python.org/dev/peps/pep-0257/).
- Recommended `flake8` extensions:
  - flake8-mutable (Mutable default parameters in function definitions)
  - flake8-pep3101 (String formatting)
  - flake8-print (`print` calls)
  - flake8-quotes (Enforce single quotes)
  - flake8-debugger (`pdb/ipdb` traces)

## Naming

|Type                               |Public                    |Internal
|-----------------------------------|--------------------------|--------
|Packages                           |lower\_with\_under        |
|Modules                            |lower\_with\_under        |\_lower\_with\_under
|Classes                            |CapWords                  |\_CapWords
|Exceptions                         |CapWords                  |
|Functions                          |lower\_with\_under()      |\_lower\_with\_under()
|Global/Class Constants             |CAPS\_WITH\_UNDER         |\_CAPS\_WITH\_UNDER
|Global/Class Variables             |lower\_with\_under        |\_lower\_with\_under
|Instance Variables                 |lower\_with\_under        |\_lower\_with\_under (protected) or \_\_lower\_with\_under (private)
|Method Names                       |lower\_with\_under()      |\_lower\_with\_under() (protected) or \_\_lower\_with\_under() (private)
|Function/Method Parameters         |lower\_with\_under        |
|Local Variables                    |lower\_with\_under        |

## Testing

Visit the [testing](./../../../testing/automated/python/README.md) page.

## References

- <https://docs.djangoproject.com/en/1.9/internals/contributing/writing-code/coding-style/>
- <https://google.github.io/styleguide/pyguide.html>