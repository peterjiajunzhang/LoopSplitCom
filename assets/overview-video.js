(() => {
  const video = document.getElementById('overview-video');
  if (!video) return;
  const narrow = window.matchMedia('(max-width: 640px)');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const connection = navigator.connection;
  let inView = false;
  let viewerPaused = false;
  let automaticPauses = 0;
  let playPending = false;
  let automaticallyStarted = false;

  // Visibility controls playback; native controls remain available if autoplay is denied.
  video.autoplay = false;
  video.muted = true;
  video.defaultMuted = true;
  video.playsInline = true;

  function pauseOutsideView() {
    if (video.paused) return;
    automaticPauses += 1;
    video.pause();
  }
  function updatePlayback() {
    if (!inView || document.hidden) {
      pauseOutsideView();
      return;
    }
    if (reducedMotion.matches || connection?.saveData || viewerPaused || !video.paused || playPending) return;
    playPending = true;
    video.play().catch(() => {
      // Browser or device policy can still require the visitor to press Play.
    }).finally(() => { playPending = false; });
  }
  video.addEventListener('pause', () => {
    if (automaticPauses > 0) automaticPauses -= 1;
    else viewerPaused = true;
  });
  video.addEventListener('play', () => {
    automaticallyStarted = playPending;
    viewerPaused = false;
  });
  video.addEventListener('loadeddata', updatePlayback);

  function chooseLayout() {
    const layout = narrow.matches ? 'search' : 'header';
    if (video.dataset.layout === layout) return;
    const src = video.dataset[`${layout}Src`];
    const poster = video.dataset[`${layout}Poster`];
    if (!src || !poster) return;
    video.dataset.layout = layout;
    video.poster = poster;
    video.width = Number(video.dataset[`${layout}Width`]);
    video.height = Number(video.dataset[`${layout}Height`]);
    if (video.getAttribute('src') !== src) {
      pauseOutsideView();
      video.setAttribute('src', src);
      video.load();
    }
    updatePlayback();
  }
  chooseLayout();
  narrow.addEventListener('change', chooseLayout);
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(entries => {
      inView = entries[0].isIntersecting && entries[0].intersectionRatio >= 0.15;
      updatePlayback();
    }, { threshold: [0, 0.15] }).observe(video);
  } else {
    inView = true;
    updatePlayback();
  }
  document.addEventListener('visibilitychange', updatePlayback);
  reducedMotion.addEventListener('change', () => {
    if (reducedMotion.matches && automaticallyStarted) pauseOutsideView();
    updatePlayback();
  });
  connection?.addEventListener('change', updatePlayback);
})();
