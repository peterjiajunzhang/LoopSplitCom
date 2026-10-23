(() => {
  const input = document.getElementById('topic-query');
  const topics = [...document.querySelectorAll('[data-help-topic]')];
  if (!input || !topics.length) return;
  const status = document.getElementById('search-status');
  document.getElementById('help-search').hidden = false;
  input.addEventListener('input', () => {
    const terms = input.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    let count = 0;
    topics.forEach(topic => {
      const text = (topic.textContent + ' ' + topic.dataset.search).toLowerCase();
      const matches = terms.every(term => text.includes(term));
      topic.hidden = !matches;
      if (matches) count++;
    });
    document.getElementById('no-results').hidden = count !== 0;
    status.textContent = terms.length ? `${count} ${count === 1 ? 'guide' : 'guides'} found` : '';
  });
})();
