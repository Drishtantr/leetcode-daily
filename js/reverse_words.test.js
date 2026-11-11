const assert = require('node:assert');
const { reverseWords } = require('./reverse_words');

assert.strictEqual(reverseWords('the sky is blue'), 'blue is sky the');
assert.strictEqual(reverseWords('  hello world  '), 'world hello');
assert.strictEqual(reverseWords('a good   example'), 'example good a');
assert.strictEqual(reverseWords(''), '');
console.log('reverse_words: ok');
