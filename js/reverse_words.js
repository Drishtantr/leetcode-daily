// Reverse the order of the words in a sentence, collapsing runs of spaces.
function reverseWords(s) {
  return s.trim().split(/\s+/).filter(Boolean).reverse().join(' ');
}

module.exports = { reverseWords };
