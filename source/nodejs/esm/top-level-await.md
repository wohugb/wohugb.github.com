# Top-level `await`[#](#top-level-await)

Added in: v14.8.0

The `await` keyword may be used in the top level body of an ECMAScript module.

Assuming an `a.mjs` with

    export const five = await Promise.resolve(5);

And a `b.mjs` with

    import { five } from './a.mjs';

    console.log(five); // Logs `5`

    node b.mjs # works

If a top level `await` expression never resolves, the `node` process will exit with a `13` [status code](process.html#exit-codes).

    import { spawn } from 'node:child_process';
    import { execPath } from 'node:process';

    spawn(execPath, [
      '--input-type=module',
      '--eval',
      // Never-resolving Promise:
      'await new Promise(() => {})',
    ]).once('exit', (code) => {
      console.log(code); // Logs `13`
    });
