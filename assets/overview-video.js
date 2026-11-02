(() => {
  const video = document.getElementById('overview-video');
  if (!video) return;
  const narrow = window.matchMedia('(max-width: 640px)');
  function chooseLayout() {
    const layout = narrow.matches ? 'search' : 'header';
    if (video.dataset.layout === layout) return;
    video.dataset.layout = layout;
    const src = `assets/video/loopsplit-${layout}-en.mp4`;
    video.poster = `assets/video/${layout}-poster.jpg`;
    if (video.getAttribute('src') !== src) {
      video.pause();
      video.setAttribute('src', src);
      video.load();
    }
  }
  chooseLayout();
  narrow.addEventListener('change', chooseLayout);
})();
