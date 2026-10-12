import assert from 'node:assert/strict';
import {readFile, readdir} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const forbidden = /C:\\Users\\|C:\/Users\/|AGENTS\.md|Antigravity|Human Lock|QA\/QC|sha256|Tệp Markdown|Cần đối chiếu/;
const expected = ['app.js', 'curriculum.json', 'favicon.svg', 'fonts/NotoSans.ttf', 'fonts/OFL.txt', 'index.html', 'styles.css'];
async function files(dir, prefix = '') {
  const result = [];
  for (const entry of await readdir(dir, {withFileTypes: true})) {
    const name = prefix + entry.name;
    if (entry.isDirectory()) result.push(...await files(path.join(dir, entry.name), name + '/'));
    else { assert(entry.isFile(), 'Only regular files are allowed'); result.push(name); }
  }
  return result.sort();
}

export async function verify(root, built = true) {
  const data = JSON.parse(await readFile(path.join(root, 'data/curriculum.json'), 'utf8'));
  assert.deepEqual(Object.keys(data).sort(), ['grades','lessons','skillGroups','skills','strands','yccd']);
  assert.equal(data.lessons.length, 180);
  assert.equal(data.skills.length, 46);
  assert.equal(data.skillGroups.length, 6);
  assert.equal(data.yccd.length, 123);
  const skillIds = new Set(data.skills.map(s => s.id));
  assert.equal(skillIds.size, 46);
  assert.equal(new Set(data.lessons.map(l => l.id)).size, 180);
  const yccdCodes = new Set(data.yccd.map(y => y.code));
  assert.equal(yccdCodes.size, 123);
  const groups = new Set(data.skillGroups.map(g => g.id));
  for (const skill of data.skills) {
    assert(groups.has(skill.group));
    assert.equal(skill.progression.length, 5);
  }
  for (let grade = 1; grade <= 5; grade++) {
    const lessons = data.lessons.filter(l => l.grade === grade);
    assert.equal(lessons.length, 36);
    for (let index = 0; index < lessons.length; index++) {
      const lesson = lessons[index];
      assert.equal(lesson.position, index + 1);
      assert.equal(lesson.id, `${grade}-${String(index + 1).padStart(2, '0')}`);
      assert(lesson.name.trim() && lesson.focus.trim());
      for (const id of lesson.skillIds) assert(skillIds.has(id), `Unknown KN ${id}`);
    }
  }
  const sourceFiles = await files(path.join(root, 'web'));
  assert.deepEqual(sourceFiles, expected.filter(name => name !== 'curriculum.json'));
  for (const name of sourceFiles.filter(name => /\.(js|css|html)$/.test(name))) {
    assert(!forbidden.test(await readFile(path.join(root, 'web', name), 'utf8')), name);
  }
  assert(!forbidden.test(JSON.stringify(data)));
  if (built) {
    const dist = path.join(root, 'dist');
    assert.deepEqual(await files(dist), expected);
    for (const name of expected) {
      const source = name === 'curriculum.json' ? path.join(root, 'data', name) : path.join(root, 'web', name);
      assert((await readFile(source)).equals(await readFile(path.join(dist, name))), `Output mismatch: ${name}`);
    }
  }
  console.log('PASS: 180 bài / 5 lớp, 46 kỹ năng, 123 YCCĐ; chỉ xuất 7 tệp website.');
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  await verify(fileURLToPath(new URL('../', import.meta.url)));
}
