# Contributing

Feel free to contribute to this guidelines within the scope of the following
best practices.

## Styling Rules

* Introduce changes by creating pull requests and assigning them to the
  sophilabs squad's members. You can reach them in the
  [#squad](https://sophilabs.slack.com/messages/G8N6C487P)
  channel.
* Avoid copying content from other sources, just link it.
* If you are going to upload code snippets, make sure that they respect the
  standards by running linters on it.
* Be concise.
* Use bullet-lists extensively.
* Word proof your code before to avoid typos and grammar mistakes.
* Avoid passive voice where possible.
* Paragraphs more than 5-7 sentences may lose the reader.
* Paragraphs of only 1-3 sentences should either be expanded or folded into
  another paragraph to make the paper easier to read.
* Avoid using vague words to avoid defining terms:
  * Emphasis: Important, interesting …
  * Measurements: Very, marginally, hardly…
* Don't tell the reader what you feel, believe, think, or hope.
* Use the future tense rarely, the present tense occasionally, the past tense
  often.
* Separate the different tenses by paragraphs, not by sentences.
* Semi-colons should be used rarely if ever.
* Count your commas. If you used more than 4-5 commas in a sentence, break it up
  into shorter sentences.

## File and folder names

Lowercase, hyphenated file and folder names, i.e. `code-reviews.md`.

## Editor

We recommend [Visual Studio Code](https://code.visualstudio.com/Download) with
the [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
extension.

### Workspace settings

Open Visual Studio Code preferences and replace the `Workpsace Settings` with
the following content:

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

To run a linter use `yarn mdl`. For example to run it against your
changed files you can use `git diff`.

```bash
yarn mdl `git diff --name-only`
```