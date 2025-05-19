// Neon glow effect on nav buttons and form submit button
document.querySelectorAll('.btn, .submit-btn').forEach(button => {
  button.addEventListener('mouseenter', () => {
    button.style.boxShadow = '0 0 15px #00ffff, 0 0 30px #00ffff';
  });
  button.addEventListener('mouseleave', () => {
    button.style.boxShadow = 'none';
  });
});
