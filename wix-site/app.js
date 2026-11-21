(function () {
  document.documentElement.classList.add('js');

  const prefersReducedMotion = () =>
    window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Frosted glass sticky header scroll hairline
  const siteHeader = document.getElementById('siteHeader') || document.querySelector('.site-header');
  if (siteHeader) {
    const syncHeaderBorder = () => {
      siteHeader.classList.toggle('is-scrolled', window.scrollY > 8);
    };
    window.addEventListener('scroll', syncHeaderBorder, { passive: true });
    syncHeaderBorder();
  }

  // Subtle one-time scroll reveal
  const revealEls = [...document.querySelectorAll('.reveal')];
  if (revealEls.length) {
    if (prefersReducedMotion() || !('IntersectionObserver' in window)) {
      revealEls.forEach((el) => el.classList.add('is-visible'));
    } else {
      const revealObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add('is-visible');
              revealObserver.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.01, rootMargin: '0px 0px 80px 0px' }
      );
      revealEls.forEach((el) => revealObserver.observe(el));
    }
  }

  function revealAnchor(hash) {
    const target = document.getElementById(hash.slice(1));
    if (!target) return;
    if (target.classList.contains('reveal')) target.classList.add('is-visible');
    target.querySelectorAll('.reveal').forEach((el) => el.classList.add('is-visible'));
  }

  revealAnchor(window.location.hash);
  window.addEventListener('hashchange', () => revealAnchor(window.location.hash));
  document.addEventListener('click', (event) => {
    const anchor = event.target.closest('a[href^="#"]');
    if (anchor) revealAnchor(anchor.hash);
  });

  // Mobile menu toggle
  const menuToggle = document.getElementById('menuToggle');
  const mobileDrawer = document.getElementById('mobileDrawer');
  if (menuToggle && mobileDrawer) {
    menuToggle.addEventListener('click', () => {
      const open = !mobileDrawer.hidden;
      mobileDrawer.hidden = open;
      menuToggle.setAttribute('aria-expanded', String(!open));
    });
    mobileDrawer.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        mobileDrawer.hidden = true;
        menuToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Interactive Custom-Salon iPhone Booking Demo
  const presets = {
    nail: {
      name: 'Lumière Nail Studio',
      primary: { en: 'Gel Manicure', zh: '凝膠美甲', price: 'HK$280', mins: 60, room: 'Nail Station 1' },
      secondary: { en: 'Classic Facial', zh: '經典面部護理', price: 'HK$420', mins: 60 },
      booked: { service: 'Classic Facial', room: 'Room 2' },
      story: 'Autumn Gel Manicure',
      storyZh: '秋日凝膠美甲',
      handoff: {
        callback: 'Owner callback queued',
        notes: 'Bridal nail and makeup notes sent',
        role: { en: 'salon owner', zh: '店主' },
        request: {
          mixed: '我有 sensitive skin，想問 4 位姊妹嘅 bridal nail & makeup package 幾錢？',
          en: 'I have sensitive skin. Can you quote for bridal nails and makeup for four bridesmaids?',
          zh: '我皮膚容易敏感，想問四位姊妹嘅婚禮美甲同化妝套餐幾錢？'
        },
        summary: { en: 'your bridal package and skin sensitivity', zh: '婚禮套餐同皮膚敏感嘅資料' }
      }
    },
    hair: {
      name: 'Mong Kok Hair Lab',
      primary: { en: 'Cut & Colour', zh: '剪髮連染髮', price: 'HK$680', mins: 90, room: 'Stylist Chair 1' },
      secondary: { en: 'Keratin Hair Treatment', zh: '角蛋白護髮', price: 'HK$480', mins: 60 },
      booked: { service: 'Silk Blowout', room: 'Hair Wash Bay' },
      story: 'Evening Cut & Colour',
      storyZh: '晚間剪髮連染髮',
      handoff: {
        callback: 'Senior stylist callback queued',
        notes: 'Balayage & bridal styling notes sent',
        role: { en: 'senior stylist', zh: '資深髮型師' },
        request: {
          mixed: '想搵 senior stylist 做 balayage 同 bridal hair styling，可唔可以報個價？',
          en: 'Can your senior stylist quote for balayage with bleach and bridal hair styling?',
          zh: '想做手掃漂染同新娘髮型，可唔可以請資深髮型師報價？'
        },
        summary: { en: 'your bleaching and bridal styling request', zh: '漂染同新娘造型嘅要求' }
      }
    },
    skin: {
      name: 'TST Skin Atelier',
      primary: { en: 'Hydra Facial', zh: '水漾補濕護理', price: 'HK$520', mins: 60, room: 'Treatment Room 1' },
      secondary: { en: 'Sensitive Skin Repair', zh: '敏感肌修護', price: 'HK$620', mins: 60 },
      booked: { service: 'Deep Cleanse Facial', room: 'Room 2' },
      story: 'Hydra Facial Care',
      storyZh: '水漾補濕護理',
      handoff: {
        callback: 'Lead therapist callback queued',
        notes: 'Post-laser facial assessment sent',
        role: { en: 'lead therapist', zh: '主管美容師' },
        request: {
          mixed: '我做完 laser 之後皮膚有啲敏感，可唔可以約 therapist 做個 assessment 先 book facial？',
          en: 'My skin is sensitive after laser treatment. Can a therapist assess me before I book a facial?',
          zh: '我做完激光之後皮膚有啲敏感，可唔可以請美容師評估咗先約面部護理？'
        },
        summary: { en: 'your request for a post-laser skin assessment', zh: '激光療程後嘅皮膚評估要求' }
      }
    }
  };

  const channels = {
    whatsapp: {
      header: 'WhatsApp Business', headerZh: 'WhatsApp Business', calendar: 'WhatsApp', confirmation: 'WhatsApp', badge: 'WA',
      composer: 'WhatsApp Business · Auto-reply active',
      composerZh: 'WhatsApp Business · 自動回覆已啟用',
      opening: { mixed: '你好 {salon}，', zh: '你好，', en: 'Hi {salon}! ' }
    },
    instagram: {
      header: 'Instagram DM', headerZh: 'Instagram 私訊', calendar: 'Instagram DM', confirmation: 'Instagram', badge: 'DM',
      composer: 'Message…',
      composerZh: '發送訊息…',
      opening: { mixed: '啱啱睇到你哋 IG story，', zh: '啱啱睇到你哋嘅限時動態，', en: 'Just saw your IG story. ' }
    },
    web: {
      header: 'Salon Website Chat', headerZh: '網站對話', calendar: 'Website', confirmation: 'Website', badge: 'Web',
      composer: 'Website chat · 24/7 assistant',
      composerZh: '網站對話 · 24/7 接待助手',
      opening: { mixed: '你好，我睇緊你哋個 online menu。', zh: '你好，我喺網站睇緊價目表。', en: 'Hi, I am browsing your website menu. ' }
    }
  };

  const scenarios = {
    book: {
      time: '21:14',
      day: 'Thursday',
      syncText: 'Illustrative: confirmed in 0.8s',
      detail: 'Illustrative: auto-reminder queued 10:00 AM',
      holding: 'Holding 18:30',
      client: {
        mixed: ({ primary }) => `想 book 星期四 6:30 PM 做 ${primary.en}，有冇位？`,
        zh: ({ primary }) => `想問星期四傍晚六點半有冇位做${primary.zh}？`,
        en: ({ primary }) => `Can I book ${primary.en} for Thursday at 6:30 PM?`
      },
      reply: {
        zh: ({ primary, salonName }) => `多謝聯絡 ${salonName}！幫你訂咗星期四 18:30 嘅${primary.zh}，${primary.price}，需時 ${primary.mins} 分鐘。當日 10:00 會提你。`,
        en: ({ primary, salonName }) => `Thanks for messaging ${salonName}. You're booked for ${primary.en} on Thursday at 6:30 PM, ${primary.price} for ${primary.mins} mins. We'll remind you at 10 AM that day.`
      }
    },
    price: {
      time: '14:22',
      day: 'Thursday',
      syncText: 'Illustrative: menu matched in 0.6s',
      detail: 'Illustrative: evening slot offered',
      holding: 'Checking 18:30',
      client: {
        mixed: ({ primary, secondary }) => `有冇 price list？想睇吓 ${primary.en} 同 ${secondary.en} 各幾錢。`,
        zh: ({ primary, secondary }) => `請問${primary.zh}同${secondary.zh}分別收幾多錢？`,
        en: ({ primary, secondary }) => `How much are ${primary.en} and ${secondary.en}?`
      },
      reply: {
        zh: ({ primary, secondary, salonName }) => `${salonName} 嘅收費係${primary.zh} ${primary.price}（${primary.mins} 分鐘），${secondary.zh} ${secondary.price}（${secondary.mins} 分鐘）。星期四 18:30 有位，想約邊項？`,
        en: ({ primary, secondary, salonName }) => `At ${salonName}, ${primary.en} is ${primary.price} (${primary.mins} mins) and ${secondary.en} is ${secondary.price} (${secondary.mins} mins). Thursday at 6:30 PM is open. Which would you like?`
      }
    },
    reschedule: {
      time: '11:05',
      day: 'Friday',
      syncText: 'Illustrative: updated in 0.9s',
      detail: 'Illustrative: Thursday slot released',
      holding: 'Holding 18:30',
      client: {
        mixed: ({ primary }) => `星期四 6:30 PM 個 ${primary.en} booking 趕唔切，可唔可以 reschedule 去 Friday 同一時間？`,
        zh: ({ primary }) => `想將星期四傍晚六點半嘅${primary.zh}改去星期五同一時間，得唔得？`,
        en: ({ primary }) => `Could I move my Thursday 6:30 PM ${primary.en} to the same time on Friday?`
      },
      reply: {
        zh: ({ primary, salonName }) => `你喺 ${salonName} 嘅${primary.zh}已經改到星期五 18:30，收費照舊係 ${primary.price}。星期四嗰個位已經放返出嚟。`,
        en: ({ primary, salonName }) => `Your ${primary.en} at ${salonName} is now on Friday at 6:30 PM at the same price, ${primary.price}. We've released your Thursday slot.`
      }
    },
    handoff: {
      time: '16:40',
      day: 'Owner handoff',
      syncText: 'Illustrative: escalated in 0.7s',
      detail: 'Illustrative: callback requested',
      holding: 'Sending notes',
      client: {
        mixed: ({ handoff }) => handoff.request.mixed,
        zh: ({ handoff }) => handoff.request.zh,
        en: ({ handoff }) => handoff.request.en
      },
      reply: {
        zh: ({ handoff, salonName }) => `多謝聯絡 ${salonName}，我已經幫你將${handoff.summary.zh}轉交畀${handoff.role.zh}，佢一得閒就會覆你。`,
        en: ({ handoff, salonName }) => `I've passed on the details about ${handoff.summary.en} to the ${handoff.role.en} at ${salonName}. They'll get back to you.`
      }
    }
  };

  let activeChannel = 'whatsapp';
  let activePreset = 'nail';
  let activeScenario = 'book';
  let activeLang = 'mixed';
  let demoRunId = 0;
  let demoTimers = [];
  let inputDebounceTimer = null;
  let coSalonDirty = false;
  let coEmailDirty = false;

  const customSalonInput = document.getElementById('customSalonInput');
  const salonPills = [...document.querySelectorAll('.salon-pill')];
  const phoneScreen = document.querySelector('.iphone-screen');
  const phoneSalonInitials = document.getElementById('phoneSalonInitials');
  const phoneSalonName = document.getElementById('phoneSalonName');
  const phoneChannel = document.getElementById('phoneChannel');
  const phoneHandle = phoneScreen.querySelector('.chat-handle');
  const phoneUrl = phoneScreen.querySelector('.web-url');
  const phoneBadge = phoneScreen.querySelector('.chat-channel-badge');
  const phoneComposer = phoneScreen.querySelector('.iphone-composer span');
  const transcriptBody = document.getElementById('transcriptBody');
  const calendarSlots = document.getElementById('calendarSlots');
  const calendarDayLabel = document.getElementById('calendarDayLabel');
  const calendarDetail = document.querySelector('.calendar-detail');
  const syncStatus = document.getElementById('syncStatus');
  const coSalonInput = document.getElementById('coSalon');
  const coEmailInput = document.getElementById('coEmail');
  const demoSalonInput = document.getElementById('fSalon');

  if (coSalonInput) {
    coSalonInput.addEventListener('input', () => {
      coSalonDirty = true;
    });
  }
  if (coEmailInput) {
    coEmailInput.addEventListener('input', () => {
      coEmailDirty = true;
    });
  }

  function getSalonName() {
    return customSalonInput.value.trim() || presets[activePreset].name;
  }

  function getSalonSlug(name) {
    return name.normalize('NFKD').toLowerCase().replace(/[^a-z0-9]/g, '') || 'deskmatesalon';
  }

  function getSalonInitials(name) {
    const words = name.trim().split(/\s+/).filter(Boolean);
    if (words.length >= 2) {
      return (Array.from(words[0])[0] + Array.from(words[1])[0]).toUpperCase();
    }
    const chars = Array.from(words[0] || 'LN');
    return chars.slice(0, 2).join('').toUpperCase();
  }

  function clearDemoTimers() {
    demoTimers.forEach((id) => clearTimeout(id));
    demoTimers = [];
  }

  function scheduleDemo(fn, ms, runId) {
    const id = setTimeout(() => {
      if (runId === demoRunId) fn();
    }, ms);
    demoTimers.push(id);
  }

  function createLockIcon() {
    const ns = 'http://www.w3.org/2000/svg';
    const svg = document.createElementNS(ns, 'svg');
    svg.setAttribute('viewBox', '0 0 16 16');
    svg.setAttribute('width', '14');
    svg.setAttribute('height', '14');
    svg.setAttribute('fill', 'none');
    svg.setAttribute('stroke', 'currentColor');
    svg.setAttribute('stroke-width', '1.5');
    svg.setAttribute('stroke-linecap', 'round');
    svg.setAttribute('stroke-linejoin', 'round');
    svg.setAttribute('aria-hidden', 'true');
    svg.classList.add('lock-icon');

    const rect = document.createElementNS(ns, 'rect');
    rect.setAttribute('x', '3');
    rect.setAttribute('y', '7');
    rect.setAttribute('width', '10');
    rect.setAttribute('height', '7');
    rect.setAttribute('rx', '2');

    const path = document.createElementNS(ns, 'path');
    path.setAttribute('d', 'M5 7V5a3 3 0 0 1 6 0v2');

    svg.appendChild(rect);
    svg.appendChild(path);
    return svg;
  }

  function createBubble(kind, text, timeStr, showReadMark = false) {
    const div = document.createElement('div');
    div.className = `bubble bubble--${kind}`;
    div.appendChild(document.createTextNode(text));
    const t = document.createElement('time');
    t.textContent = timeStr;
    if (showReadMark) {
      const mark = document.createElement('span');
      mark.className = 'chat-read-mark';
      mark.setAttribute('aria-hidden', 'true');
      mark.textContent = '✓✓';
      t.append(' ', mark);
    }
    div.appendChild(t);
    return div;
  }

  function renderChatContext(preset) {
    transcriptBody.replaceChildren();
    const chinese = activeLang === 'zh';
    if (activeChannel === 'instagram') {
      const card = document.createElement('div');
      card.className = 'story-reply-card';
      const title = document.createElement('strong');
      title.textContent = chinese ? '回覆了你的限時動態' : 'Replied to your story';
      const story = chinese ? preset.storyZh : preset.story;
      card.append(title, document.createTextNode(`${story} · ${preset.primary.price}`));
      transcriptBody.appendChild(card);
    } else if (activeChannel === 'web') {
      const banner = document.createElement('div');
      banner.className = 'web-context-banner';
      banner.textContent = chinese ? '正在瀏覽：服務及價目表' : 'Viewing: Services & Pricing';
      transcriptBody.appendChild(banner);
    }
    transcriptBody.scrollTop = 0;
  }

  function createTypingBubble() {
    const div = document.createElement('div');
    div.className = 'bubble bubble--out typing';
    div.setAttribute('role', 'status');
    div.setAttribute('aria-label', activeLang === 'zh' ? 'DeskMate AI 輸入中' : 'DeskMate AI is typing');
    for (let i = 0; i < 3; i += 1) {
      const dot = document.createElement('span');
      dot.setAttribute('aria-hidden', 'true');
      div.appendChild(dot);
    }
    return div;
  }

  function getCalendarSlots(preset, scenario) {
    const { primary, secondary, booked, handoff } = preset;
    const primaryLabel = `${primary.en} · ${primary.price}`;
    const session = `${primary.mins} mins, ${primary.room}`;
    const first = { time: '17:00', svc: booked.service, sub: booked.room, status: 'Booked' };
    const evening = { time: '18:30', svc: primaryLabel, sub: session, status: 'Open', target: true };
    const last = { time: '20:00', svc: 'Available slot', sub: 'Open for instant booking', status: 'Open' };

    if (scenario === 'handoff') {
      return [
        first,
        { time: 'Next', svc: handoff.callback, sub: handoff.notes, status: 'Pending', target: true },
        last
      ];
    }

    if (scenario === 'price') {
      return [
        first,
        evening,
        { ...last, sub: `${secondary.en} · ${secondary.price} · ${secondary.mins} mins` }
      ];
    }

    evening.sub = scenario === 'reschedule'
      ? `${session} · Moved from Thu 18:30`
      : `${session} · Reminder at 10:00 AM`;
    return [first, evening, last];
  }

  function renderInitialCalendar(slots) {
    if (!calendarSlots) return null;
    calendarSlots.replaceChildren();
    let targetEl = null;

    slots.forEach((s) => {
      const row = document.createElement('div');
      row.className = 'cal-slot slot';

      const timeEl = document.createElement('span');
      timeEl.className = 'cal-t slot-time';
      timeEl.textContent = s.time;

      const info = document.createElement('div');
      const svcEl = document.createElement('div');
      svcEl.className = 'cal-svc';
      svcEl.textContent = s.svc;
      const subEl = document.createElement('div');
      subEl.className = 'cal-sub';
      subEl.textContent = s.sub;
      info.appendChild(svcEl);
      info.appendChild(subEl);

      const statusEl = document.createElement('span');
      statusEl.className = 'cal-st slot-status';
      statusEl.textContent = s.status;

      row.appendChild(timeEl);
      row.appendChild(info);
      row.appendChild(statusEl);
      calendarSlots.appendChild(row);

      if (s.target) {
        targetEl = { row, statusEl };
      }
    });

    return targetEl;
  }

  function syncActivePill() {
    const current = customSalonInput.value.trim();
    salonPills.forEach((pill) => {
      pill.classList.toggle('is-active', current === pill.dataset.salon);
    });
  }

  function runDemo() {
    const runId = ++demoRunId;
    clearDemoTimers();

    const sc = scenarios[activeScenario];
    const preset = presets[activePreset];
    const channel = channels[activeChannel];
    const salonName = getSalonName();
    const slug = getSalonSlug(salonName);
    const replyLang = activeLang === 'en' ? 'en' : 'zh';
    const replyTag = replyLang === 'en' ? 'English reply' : 'Cantonese reply';
    const chinese = activeLang === 'zh';
    const subtitle = chinese ? `${channel.headerZh} · 廣東話回覆` : `${channel.header} · ${replyTag}`;
    const isHandoff = activeScenario === 'handoff';
    const isPrice = activeScenario === 'price';
    const reduced = prefersReducedMotion();

    syncActivePill();
    if (coSalonInput && !coSalonDirty) {
      coSalonInput.value = salonName;
    }
    if (coEmailInput && !coEmailDirty) {
      coEmailInput.value = `owner@${slug}.example.com`;
    }
    demoSalonInput.placeholder = `e.g. ${salonName}`;

    phoneScreen.dataset.channel = activeChannel;
    phoneSalonName.textContent = salonName;
    phoneSalonInitials.textContent = getSalonInitials(salonName);
    phoneChannel.textContent = subtitle;
    phoneHandle.textContent = `@${slug}`;
    phoneUrl.textContent = `${slug}.example.com/services`;
    phoneBadge.textContent = channel.badge;
    phoneComposer.textContent = chinese ? channel.composerZh : channel.composer;
    const calendarLabel = `${sc.day} · ${salonName} · ${channel.calendar}`;
    calendarDayLabel.textContent = calendarLabel;
    syncStatus.textContent = sc.syncText;
    calendarDetail.textContent = sc.detail;

    const opening = channel.opening[activeLang].replace('{salon}', () => salonName);
    const clientText = opening + sc.client[activeLang](preset);
    renderChatContext(preset);
    transcriptBody.appendChild(createBubble('in', clientText, sc.time));

    const targetSlot = renderInitialCalendar(getCalendarSlots(preset, activeScenario));
    const replyText = sc.reply[replyLang]({ ...preset, salonName });
    const typingAt = 220;
    const typingDuration = reduced ? 300 : Math.min(1400, 700 + replyText.length * 4);
    const fadeDuration = reduced ? 0 : 200;

    let typingBubble = null;
    scheduleDemo(() => {
      if (!transcriptBody) return;
      typingBubble = createTypingBubble();
      transcriptBody.appendChild(typingBubble);
      transcriptBody.scrollTop = transcriptBody.scrollHeight;
      if (phoneChannel) phoneChannel.textContent = chinese ? '輸入中…' : 'typing…';
    }, typingAt, runId);

    // Fade out typing dots 200ms before reply enters (unless reduced motion)
    if (fadeDuration > 0) {
      scheduleDemo(() => {
        if (typingBubble) typingBubble.classList.add('is-fading');
      }, typingAt + typingDuration - fadeDuration, runId);
    }

    const replyAt = typingAt + typingDuration;
    scheduleDemo(() => {
      if (typingBubble && typingBubble.parentNode) {
        typingBubble.remove();
      }
      if (phoneChannel) phoneChannel.textContent = subtitle;
      if (transcriptBody) {
        transcriptBody.appendChild(createBubble('out', replyText, sc.time, activeChannel === 'whatsapp'));
        transcriptBody.scrollTop = transcriptBody.scrollHeight;
      }
    }, replyAt, runId);

    // t = replyAt + 200ms: calendar slot locks with bronze pulse
    scheduleDemo(() => {
      calendarDayLabel.textContent = isHandoff || isPrice ? calendarLabel : `${calendarLabel} synced`;
      if (syncStatus) syncStatus.textContent = sc.syncText;
      if (targetSlot) {
        targetSlot.row.classList.add('is-locking');
        targetSlot.statusEl.textContent = sc.holding;
      }
    }, replyAt + 200, runId);

    // t = replyAt + 200 + 900ms: transition to confirmed locked state with lock SVG
    scheduleDemo(() => {
      if (targetSlot) {
        targetSlot.row.classList.remove('is-locking');
        if (isPrice || isHandoff) {
          targetSlot.statusEl.textContent = isPrice ? 'Open' : 'Queued';
        } else {
          targetSlot.row.classList.add('is-locked');
          targetSlot.statusEl.replaceChildren(
            createLockIcon(),
            document.createTextNode(`Confirmed via ${channel.confirmation}`)
          );
        }
      }
    }, replyAt + 1100, runId);
  }

  if (customSalonInput) {
    customSalonInput.addEventListener('input', () => {
      syncActivePill();
      const current = customSalonInput.value.trim();
      const matchedPill = salonPills.find((pill) => current === pill.dataset.salon);
      if (matchedPill) activePreset = matchedPill.dataset.preset;
      else if (/hair|barber|cut|colour/i.test(current)) activePreset = 'hair';
      else if (/skin|facial|derma|clinic/i.test(current)) activePreset = 'skin';
      else activePreset = 'nail';
      clearTimeout(inputDebounceTimer);
      inputDebounceTimer = setTimeout(() => runDemo(), 450);
    });
    customSalonInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        clearTimeout(inputDebounceTimer);
        runDemo();
      }
    });
  }

  salonPills.forEach((pill) => {
    pill.addEventListener('click', () => {
      clearTimeout(inputDebounceTimer);
      activePreset = pill.dataset.preset;
      customSalonInput.value = pill.dataset.salon;
      runDemo();
    });
  });

  document.querySelectorAll('.lang-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      clearTimeout(inputDebounceTimer);
      activeLang = btn.dataset.lang;
      document.querySelectorAll('.lang-btn').forEach((b) => {
        const on = b === btn;
        b.classList.toggle('active', on);
        b.setAttribute('aria-selected', String(on));
      });
      runDemo();
    });
  });

  document.querySelectorAll('.seg-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      clearTimeout(inputDebounceTimer);
      activeChannel = btn.dataset.channel;
      document.querySelectorAll('.seg-btn').forEach((b) => {
        const on = b === btn;
        b.classList.toggle('active', on);
        b.setAttribute('aria-selected', String(on));
      });
      runDemo();
    });
  });

  document.querySelectorAll('.prompt-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      clearTimeout(inputDebounceTimer);
      activeScenario = btn.dataset.scenario;
      document.querySelectorAll('.prompt-btn').forEach((b) => b.classList.toggle('active', b === btn));
      runDemo();
    });
  });

  runDemo();

  // Savings Estimator Slider
  const hoursSlider = document.getElementById('hoursSlider');
  const hoursValue = document.getElementById('hoursValue');
  const calcStaff = document.getElementById('calcStaff');
  const calcStaffDetail = document.getElementById('calcStaffDetail');
  const calcPct = document.getElementById('calcPct');
  const calcAnnual = document.getElementById('calcAnnual');

  function updateSavings() {
    if (!hoursSlider) return;
    const hrs = Number(hoursSlider.value);
    const staffCost = Math.round(43.1 * hrs * 26);
    const proCost = 788;
    const pct = Math.round(((staffCost - proCost) / staffCost) * 100);
    const annual = (staffCost - proCost) * 12;
    hoursValue.textContent = `${hrs} hours / day (26 days/mo)`;
    calcStaff.textContent = `HK$${staffCost.toLocaleString()}`;
    calcStaffDetail.textContent = `${hrs} hrs/day × 26 days at HK$43.10/hr minimum wage`;
    calcPct.textContent = `-${pct}%`;
    calcAnnual.textContent = `Estimated HK$${annual.toLocaleString()} saved per year`;
  }
  if (hoursSlider) {
    hoursSlider.addEventListener('input', updateSavings);
    updateSavings();
  }

  // Industries Switcher
  const industriesData = {
    salons: {
      title: 'Hong Kong beauty and hair salons',
      desc: 'Designed for independent salons in Mong Kok, Causeway Bay and Tsim Sha Tsui with 1 to 10 staff and no full-time receptionist.',
      bullets: [
        'Instant Cantonese and English replies across WhatsApp, Instagram DM and website chat',
        'Pre-configured with your exact nail, facial, lash or hair treatment durations and prices',
        'Automatic 24-hour reminders reduce costly late cancellations and no-shows'
      ]
    },
    clinics: {
      title: 'Dental and wellness clinics (Year 2)',
      visualTitle: 'Dental, Physio & TCM Clinics',
      visualChips: ['Multi-doctor room sync', 'Cantonese & English intake', 'Target: part of 10 Year 2 accounts'],
      desc: 'Extending the same bilingual receptionist engine to neighbourhood dental, physiotherapy and Chinese medicine clinics.',
      bullets: [
        'Multi-practitioner and treatment-room availability routing on one calendar',
        'Pre-visit preparation instructions sent automatically in Cantonese or English',
        'PDPO-aligned minimal data collection with direct clinic desk handoff'
      ]
    },
    tutorial: {
      title: 'Tutorial and enrichment centres (Year 2)',
      visualTitle: 'Tutorial & Enrichment Centres',
      visualChips: ['Evening parent WhatsApp triage', 'Trial & makeup class booking', 'Target: part of 10 Year 2 accounts'],
      desc: 'Helping small Hong Kong education centres answer high-volume evening parent messages without hiring extra admin staff.',
      bullets: [
        'Answers syllabus, grade level and fee questions across WhatsApp and web chat',
        'Books trial classes and manages makeup-lesson rescheduling automatically',
        'Keeps tutor timetables synced without double-booking classrooms'
      ]
    }
  };

  const industryContent = document.getElementById('industryContent');
  const industryPhoto = document.getElementById('industryPhoto');
  const industryVisual = document.getElementById('industryVisual');
  const industryVisualTitle = industryVisual.querySelector('h3');
  const industryVisualChips = industryVisual.querySelector('.ind-visual-chips');
  function renderIndustry(key) {
    const item = industriesData[key];
    if (!industryContent || !item) return;
    industryPhoto.hidden = key !== 'salons';
    industryVisual.hidden = key === 'salons';
    if (!industryVisual.hidden) {
      industryVisualTitle.textContent = item.visualTitle;
      industryVisualChips.replaceChildren(...item.visualChips.map((label) => {
        const chip = document.createElement('li');
        chip.textContent = label;
        return chip;
      }));
    }
    industryContent.replaceChildren();
    const h3 = document.createElement('h3');
    h3.textContent = item.title;
    const p = document.createElement('p');
    p.textContent = item.desc;
    const ul = document.createElement('ul');
    ul.className = 'ind-bullets';
    item.bullets.forEach((b) => {
      const li = document.createElement('li');
      li.textContent = b;
      ul.appendChild(li);
    });
    industryContent.appendChild(h3);
    industryContent.appendChild(p);
    industryContent.appendChild(ul);
  }
  document.querySelectorAll('.ind-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.ind-btn').forEach((b) => b.classList.toggle('active', b === btn));
      renderIndustry(btn.dataset.industry);
    });
  });
  renderIndustry('salons');

  // Interactive Prototype Checkout Mock-up
  const plans = {
    starter: {
      name: 'Starter Plan',
      monthly: 388,
      desc: '1 WhatsApp Business channel, up to 300 bilingual chats/mo, FAQ and booking capture, done-for-you setup.'
    },
    pro: {
      name: 'Pro Plan',
      monthly: 788,
      desc: 'WhatsApp + Instagram DM + Website chat, up to 1,000 bilingual chats/mo, one shared calendar and reminders.'
    },
    premium: {
      name: 'Premium Plan',
      monthly: 1488,
      desc: 'Multi-branch routing, deposit links, automated no-show follow-up and priority Hong Kong WhatsApp support.'
    }
  };

  const payNames = {
    card: 'Visa / Mastercard',
    wallet: 'Apple Pay / Google Pay',
    fps: 'FPS Bank Transfer'
  };

  let selectedPlan = 'pro';
  let billingCycle = 'monthly';
  let payMethod = 'card';

  const sumPlanName = document.getElementById('sumPlanName');
  const sumPlanDesc = document.getElementById('sumPlanDesc');
  const sumCycle = document.getElementById('sumCycle');
  const sumAfter = document.getElementById('sumAfter');
  const checkoutFormPane = document.getElementById('checkoutFormPane');
  const checkoutConfirmPane = document.getElementById('checkoutConfirmPane');
  const checkoutError = document.getElementById('checkoutError');
  const billingRadios = document.querySelectorAll('input[name="billingCycle"]');

  function formatPostTrial() {
    const p = plans[selectedPlan];
    if (billingCycle === 'annual') {
      const annual = Math.round(p.monthly * 12 * 0.9);
      return `HK$${annual.toLocaleString()} / year (10% off)`;
    }
    return `HK$${p.monthly.toLocaleString()} / month`;
  }

  function renderCheckoutSummary() {
    const p = plans[selectedPlan];
    if (sumPlanName) sumPlanName.textContent = p.name;
    if (sumPlanDesc) sumPlanDesc.textContent = p.desc;
    if (sumCycle) sumCycle.textContent = billingCycle === 'annual' ? 'Annual (FPS invoice)' : 'Monthly recurring';
    if (sumAfter) sumAfter.textContent = formatPostTrial();

    billingRadios.forEach((radio) => {
      radio.checked = radio.value === billingCycle;
    });
    document.querySelectorAll('.sw-btn').forEach((b) => {
      const on = b.dataset.plan === selectedPlan;
      b.classList.toggle('active', on);
      b.setAttribute('aria-checked', String(on));
    });
    document.querySelectorAll('.pay-btn').forEach((b) => {
      const on = b.dataset.pay === payMethod;
      b.classList.toggle('active', on);
      b.setAttribute('aria-checked', String(on));
    });
    const dCard = document.getElementById('payDetailCard');
    const dWallet = document.getElementById('payDetailWallet');
    const dFps = document.getElementById('payDetailFps');
    if (dCard) dCard.hidden = payMethod !== 'card';
    if (dWallet) dWallet.hidden = payMethod !== 'wallet';
    if (dFps) dFps.hidden = payMethod !== 'fps';
  }

  document.querySelectorAll('[data-select-plan]').forEach((el) => {
    el.addEventListener('click', () => {
      selectedPlan = el.dataset.selectPlan;
      if (checkoutFormPane && checkoutConfirmPane) {
        checkoutFormPane.hidden = false;
        checkoutConfirmPane.hidden = true;
      }
      renderCheckoutSummary();
    });
  });

  document.querySelectorAll('.sw-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      selectedPlan = btn.dataset.plan;
      renderCheckoutSummary();
    });
  });

  billingRadios.forEach((radio) => {
    radio.addEventListener('change', () => {
      billingCycle = radio.value;
      if (billingCycle === 'annual') payMethod = 'fps';
      else if (payMethod === 'fps') payMethod = 'card';
      renderCheckoutSummary();
    });
  });

  document.querySelectorAll('.pay-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      payMethod = btn.dataset.pay;
      billingCycle = payMethod === 'fps' ? 'annual' : 'monthly';
      renderCheckoutSummary();
    });
  });

  const confirmCheckoutBtn = document.getElementById('confirmCheckoutBtn');
  const resetCheckoutBtn = document.getElementById('resetCheckoutBtn');

  if (confirmCheckoutBtn) {
    confirmCheckoutBtn.addEventListener('click', () => {
      const salon = (document.getElementById('coSalon')?.value || '').trim();
      const email = (document.getElementById('coEmail')?.value || '').trim();
      if (!salon || !email || !email.includes('@')) {
        if (checkoutError) {
          checkoutError.textContent = 'Please enter your shop or owner name and a valid email to preview trial activation.';
          checkoutError.hidden = false;
        }
        return;
      }
      if (checkoutError) checkoutError.hidden = true;
      const p = plans[selectedPlan];
      document.getElementById('confirmLeadText').textContent =
        `Your 14-day free trial for the ${p.name} has been activated with HK$0 charged today.`;
      document.getElementById('confSalon').textContent = salon;
      document.getElementById('confPlan').textContent = p.name;
      document.getElementById('confAfter').textContent = formatPostTrial();
      document.getElementById('confMethod').textContent = payNames[payMethod];
      checkoutFormPane.hidden = true;
      checkoutConfirmPane.hidden = false;
    });
  }

  if (resetCheckoutBtn) {
    resetCheckoutBtn.addEventListener('click', () => {
      checkoutConfirmPane.hidden = true;
      checkoutFormPane.hidden = false;
    });
  }

  renderCheckoutSummary();

  // Book a Demo Form Validation & Confirmation
  const demoForm = document.getElementById('demoForm');
  const formError = document.getElementById('formError');
  const formSuccess = document.getElementById('formSuccess');
  const formSuccessText = document.getElementById('formSuccessText');
  const resetDemoFormBtn = document.getElementById('resetDemoFormBtn');

  if (demoForm) {
    demoForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('fName').value.trim();
      const salon = document.getElementById('fSalon').value.trim();
      const phone = document.getElementById('fPhone').value.trim();
      const district = document.getElementById('fDistrict').value;
      if (!name || !salon || !phone) {
        formError.hidden = false;
        return;
      }
      formError.hidden = true;
      const optIn = document.getElementById('fOptIn')?.checked;
      const optNote = optIn ? ' Monthly opt-in tips selected (unsubscribe anytime).' : ' No marketing updates selected.';
      formSuccessText.textContent =
        `Thank you, ${name}. Prototype confirmation (simulated, no external data stored): in the live service, your 1-to-1 demo request for ${salon} (${district}) would route to our Hong Kong onboarding team via WhatsApp (${phone}) within 1 business day.${optNote}`;
      demoForm.hidden = true;
      formSuccess.hidden = false;
    });
  }
  if (resetDemoFormBtn) {
    resetDemoFormBtn.addEventListener('click', () => {
      demoForm.reset();
      formSuccess.hidden = true;
      demoForm.hidden = false;
    });
  }

  // Navigation Scroll-Spy
  const navLinks = [...document.querySelectorAll('.nav-links .nav-link')];
  const sections = ['top', 'how-it-works', 'industries', 'pricing', 'faq', 'contact']
    .map((id) => document.getElementById(id))
    .filter(Boolean);
  if ('IntersectionObserver' in window && navLinks.length && sections.length) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const href = '#' + entry.target.id;
            navLinks.forEach((l) => l.classList.toggle('active', l.getAttribute('href') === href));
          }
        });
      },
      { rootMargin: '-30% 0px -60% 0px' }
    );
    sections.forEach((s) => io.observe(s));
  }
})();
