import {cp, mkdir, readFile, rm, writeFile} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {verify} from './verify.mjs';

const root = fileURLToPath(new URL('../', import.meta.url));
const dist = path.resolve(root, 'dist');
if (path.dirname(dist) !== path.resolve(root) || path.basename(dist) !== 'dist') {
  throw new Error('Unsafe output directory');
}
await verify(root, false);
await rm(dist, {recursive: true, force: true});
await mkdir(dist);
await cp(path.join(root, 'web'), dist, {recursive: true});
await writeFile(path.join(dist, 'curriculum.json'), await readFile(path.join(root, 'data/curriculum.json')));
await verify(root, true);
console.log('Build complete: dist/');
