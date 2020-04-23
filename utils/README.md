## To prettify the jsons

Who does that? I do . <br>
Using <br>
* [`npx`](https://www.npmjs.com/package/npx) - To exceute without setting up node project
* [`prettier`](https://www.npmjs.com/package/prettier) - An npm package which prettifies files

> You may run into heap memory limit when prettifying such big files (~20 MB in this case), so refer the below snippet to increase the heap memory limit for node. \t The error may look something like this: <br> _FATAL ERROR: Ineffective mark-compacts near heap limit Allocation failed - JavaScript heap out of memory_

## Increase memory limit for node

On windows
``` bash
    set NODE_OPTIONS=--max_old_space_size=4096
```

On linux
``` bash
    export NODE_OPTIONS=--max_old_space_size=4096
```