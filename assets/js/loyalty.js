(() => {
  const KEY = 'pizzaHotBalainLoyalty';
  const get = () => JSON.parse(localStorage.getItem(KEY) || 'null');
  const save = value => localStorage.setItem(KEY, JSON.stringify(value));
  const $ = id => document.getElementById(id);
  let member = get();
  const firstReward = 100;

  function render() {
    if (!member) { $('join-form').hidden = false; $('member-view').hidden = true; $('points-balance').textContent = '0'; return; }
    $('join-form').hidden = true; $('member-view').hidden = false;
    $('member-title').textContent = 'محفظة نقاطك'; $('member-name-view').textContent = member.name; $('points-balance').textContent = member.points;
    const remaining = Math.max(firstReward - member.points, 0); $('next-reward-copy').textContent = remaining ? `متبقي ${remaining} نقطة لأول مكافأة` : 'لديك مكافأة جاهزة للاستبدال';
    const progress = Math.min(Math.round(member.points / firstReward * 100), 100); $('progress-value').textContent = `${progress}%`; $('progress-bar').style.width = `${progress}%`;
    document.querySelectorAll('.reward-card').forEach(card => { const cost = Number(card.dataset.cost); const button = card.querySelector('.redeem-btn'); button.disabled = member.points < cost; button.textContent = member.points >= cost ? 'استبدل النقاط' : `تحتاج ${cost - member.points} نقطة`; });
  }
  $('join-loyalty')?.addEventListener('click', () => {
    const name = $('member-name').value.trim(), phone = $('member-phone').value.trim();
    if (name.length < 2 || phone.replace(/\D/g, '').length < 7) { alert('أدخل الاسم ورقم هاتف صحيحًا للمتابعة.'); return; }
    member = { name, phone, points: 50, marketingConsent: $('marketing-consent').checked, createdAt: new Date().toISOString() }; save(member); render();
  });
  $('edit-member')?.addEventListener('click', () => { $('join-form').hidden = false; $('member-view').hidden = true; $('member-name').value = member.name; $('member-phone').value = member.phone; $('marketing-consent').checked = !!member.marketingConsent; });
  document.querySelectorAll('.redeem-btn').forEach(button => button.addEventListener('click', () => {
    if (!member) { alert('سجّل في برنامج المكافآت أولًا.'); return; }
    const card = button.closest('.reward-card'), cost = Number(card.dataset.cost), name = card.querySelector('h3').textContent;
    if (member.points < cost) return;
    member.points -= cost; save(member); render();
    localStorage.setItem('pizzaHotActiveReward', JSON.stringify({ name, cost, at: new Date().toISOString() }));
    alert(`تم حجز «${name}». اذكرها عند إرسال طلبك عبر واتساب.`);
  }));
  render();
})();
