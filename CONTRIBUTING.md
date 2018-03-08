# Contributing

Feel free to contribute to this guidelines within the scope of the following
best practices.

## Styling Rules

- Introduce changes by creating pull requests and assigning them to the
  squad's members.
- Avoid copying content from other sources, just link it.
- If you are going to upload code snippets, make sure that they respect the PEP8
  standard by running linters on it.
- Be concise.
- Use bullet-lists extensively.

## File and folder names

Lowercase, hyphenated file and folder names, i.e. `code-reviews.md`.

## Editor

We recommend [Visual Studio Code](https://code.visualstudio.com/Download) with the following
configuration:

### Extensions

- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)

### Workspace settings

Open VSC's preferences and replace the `Workpsace Settings` with the following content:

```json
{
    "workbench.colorTheme": "Visual Studio Light",
    "[markdown]": {
        "editor.wordWrap": "off",
        "editor.rulers": [100],
    },
    "editor.minimap.enabled": false,
    "editor.renderWhitespace": "boundary",
}
```

## Linter

```bash
yarn mdl **/*.md 2>&1 >/dev/null | grep -v node_modules
```