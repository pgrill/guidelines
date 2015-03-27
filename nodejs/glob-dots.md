# Glob



```javascript
var glob = require('glob');
```

"Globs" are the patterns you type when you do stuff like `ls *.js` on the command line, or put `build/*` in a `.gitignore` file.



## Dots

If a file or directory path portion has a . as the first character,
then it will not match any glob pattern unless that pattern's
corresponding path part also has a . as its first character.

For example, the pattern
`a/.*/c` would match the file at `a/.b/c`.
However the pattern `a/*/c` would not, because `*` does not start with a dot character.

You can make glob treat dots as normal characters by setting `dot:true` in the options.

-----------------------

**Sources:**

 - https://github.com/isaacs/node-glob#dots, Isaac Z. Schlueter
