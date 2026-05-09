(() => {
  const toolbar = document.querySelector('.figure-toolbar');
  if (!toolbar) return;

  const buttons = Array.from(toolbar.querySelectorAll('button[data-mode]'));
  const views = Array.from(document.querySelectorAll('[data-view]'));

  function setMode(mode) {
    buttons.forEach((button) => {
      button.setAttribute('aria-pressed', String(button.dataset.mode === mode));
    });

    views.forEach((view) => {
      view.classList.toggle('hidden', view.dataset.view !== mode);
    });
  }

  buttons.forEach((button) => {
    button.addEventListener('click', () => setMode(button.dataset.mode));
  });
})();
