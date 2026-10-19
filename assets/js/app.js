(() => {
  const KEY = 'pizzaHotBalainCart';
  let cart = JSON.parse(localStorage.getItem(KEY) || '[]');
  const $ = (s, root = document) => root.querySelector(s);
  const $$ = (s, root = document) => [...root.querySelectorAll(s)];
  const money = value => `${Number(value).toFixed(0)}₪`;
  const save = () => localStorage.setItem(KEY, JSON.stringify(cart));
  const total = () => cart.reduce((sum, item) => sum + item.price * item.qty, 0);
  const count = () => cart.reduce((sum, item) => sum + item.qty, 0);

  function updateBadges() {
    $$('[data-cart-count]').forEach(el => el.textContent = count());
    const floating = $('#floating-total');
    if (floating) floating.textContent = money(total());
  }
  function renderCart() {
    const list = $('#cart-items'), empty = $('#cart-empty'), totalEl = $('#cart-total'), wa = $('#cart-wa');
    updateBadges();
    if (!list) return;
    list.innerHTML = '';
    empty.hidden = cart.length > 0;
    cart.forEach((item, index) => {
      const line = document.createElement('div'); line.className = 'cart-line';
      line.innerHTML = `<div><strong>${item.name}</strong><small>${item.variant || 'حجم عادي'} · ${money(item.price)} × ${item.qty}</small></div><div><b>${money(item.price * item.qty)}</b><br><button type="button" data-remove="${index}" aria-label="حذف ${item.name}">حذف</button></div>`;
      list.appendChild(line);
    });
    if (totalEl) totalEl.textContent = money(total());
    if (wa) {
      const member = JSON.parse(localStorage.getItem('pizzaHotBalainLoyalty') || 'null');
      const reward = JSON.parse(localStorage.getItem('pizzaHotActiveReward') || 'null');
      const lines = ['مرحبًا Pizza Hot، أريد تأكيد هذا الطلب:', '', ...cart.map(i => `• ${i.name}${i.variant ? ` (${i.variant})` : ''} × ${i.qty} — ${money(i.price * i.qty)}`), '', `الإجمالي: ${money(total())}`, reward ? `المكافأة المحجوزة: ${reward.name}` : '', member ? `عضو نقاط: ${member.name} — الهاتف: ${member.phone}` : '', 'الاسم: ', 'العنوان: '];
      wa.href = `https://wa.me/972569787731?text=${encodeURIComponent(lines.join('\n'))}`;
    }
  }
  function openCart() { $('#cart')?.classList.add('active'); $('#cart-overlay')?.classList.add('active'); document.body.style.overflow = 'hidden'; }
  function closeCart() { $('#cart')?.classList.remove('active'); $('#cart-overlay')?.classList.remove('active'); document.body.style.overflow = ''; }
  function addItem(name, price, variant = '') {
    const existing = cart.find(i => i.name === name && i.variant === variant);
    if (existing) existing.qty += 1; else cart.push({ name, price: Number(price), variant, qty: 1 });
    save(); renderCart();
    const toast = document.createElement('div'); toast.className = 'toast'; toast.textContent = `تمت إضافة ${name} إلى السلة`; document.body.appendChild(toast); setTimeout(() => toast.remove(), 2200);
    if (window.innerWidth < 650) openCart();
  }
  $$('.add-btn').forEach(button => button.addEventListener('click', () => {
    const card = button.closest('.menu-card'); const size = $('.size', card); const variant = size ? size.options[size.selectedIndex].text : '';
    addItem(card.dataset.name, size ? size.value : card.dataset.price, variant);
  }));
  $('#cart-toggle')?.addEventListener('click', openCart); $('#cart-close')?.addEventListener('click', closeCart); $('#cart-overlay')?.addEventListener('click', closeCart);
  $('#cart-items')?.addEventListener('click', e => { const btn = e.target.closest('[data-remove]'); if (!btn) return; cart.splice(Number(btn.dataset.remove), 1); save(); renderCart(); });
  $$('.category-tabs button').forEach(button => button.addEventListener('click', () => { $$('.category-tabs button').forEach(b => b.classList.remove('active')); button.classList.add('active'); filterMenu(); }));
  $('#menu-search')?.addEventListener('input', filterMenu);
  function filterMenu() { const term = ($('#menu-search')?.value || '').trim().toLowerCase(); const filter = $('.category-tabs button.active')?.dataset.filter || 'all'; let found = false; $$('.menu-card').forEach(card => { const matches = (filter === 'all' || card.dataset.category === filter) && card.dataset.name.toLowerCase().includes(term); card.hidden = !matches; if (matches) found = true; }); if ($('#no-results')) $('#no-results').hidden = found; }
  renderCart();
  if (location.hash === '#cart') setTimeout(openCart, 100);
})();
