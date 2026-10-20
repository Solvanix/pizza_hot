function addToCart(name, price) {
  const key = 'pizzaHotBalainCart';
  const cart = JSON.parse(localStorage.getItem(key) || '[]');
  const existing = cart.find(item => item.name === name && item.variant === '');
  if (existing) existing.qty += 1; else cart.push({ name, price: Number(price), variant: '', qty: 1 });
  localStorage.setItem(key, JSON.stringify(cart));
  window.location.href = 'store.html#cart';
}
