// Mobile menu: delegated so it works as soon as the button exists,
// without waiting for the header/footer partials to finish loading.
function setMenu(open) {
  const header = document.querySelector('.site-header');
  const toggle = document.getElementById('navToggle');
  if (!header || !toggle) return;
  header.classList.toggle('menu-open', open);
  toggle.classList.toggle('open', open);
  toggle.setAttribute('aria-expanded', String(open));
}

document.addEventListener('click', (e) => {
  if (e.target.closest('#navToggle')) {
    const header = document.querySelector('.site-header');
    setMenu(!(header && header.classList.contains('menu-open')));
  } else if (e.target.closest('#nav a')) {
    setMenu(false);
  }
});

async function includePartial(selector, url) {
  const mount = document.querySelector(selector);
  if (!mount) return;
  // Production ships the partials baked into the HTML (scripts/inline-partials.py) so
  // crawlers see the nav. Only re-fetch on localhost so edits show up while developing.
  const isDev = ['localhost', '127.0.0.1'].includes(location.hostname);
  if (!isDev && mount.children.length) return;
  try {
    const res = await fetch(url, { cache: 'no-cache' });
    mount.innerHTML = await res.text();
  } catch (e) {
    console.error('Failed to load partial', url, e);
  }
}

(async () => {
  await Promise.all([
    includePartial('#site-header-mount', 'partials/header.html'),
    includePartial('#site-footer-mount', 'partials/footer.html'),
  ]);
  initSite();
})();

function initSite() {
  // Active nav link
  const currentPage = document.body.dataset.page;
  if (currentPage) {
    document.querySelectorAll('.nav a[data-nav]').forEach((link) => {
      if (link.dataset.nav === currentPage) link.classList.add('active');
    });
  }

  // Journey strip (chapter progress)
  const chapters = [
    ['home', 'The truth', 'index.html'],
    ['about', 'Who we are', 'about.html'],
    ['services', 'The system', 'services.html'],
    ['results', 'The evidence', 'results.html'],
    ['contact', 'The next step', 'contact.html'],
  ];
  const journeyHost = document.querySelector('.hero-inner, .page-hero .wrap');
  const currentIdx = chapters.findIndex(([key]) => key === currentPage);
  if (journeyHost && currentIdx > -1) {
    const journeyNav = document.createElement('nav');
    journeyNav.className = 'journey reveal';
    journeyNav.setAttribute('aria-label', 'Your journey through the site');
    chapters.forEach(([, label, href], i) => {
      const a = document.createElement('a');
      a.href = href;
      a.textContent = '0' + (i + 1) + ' ' + label;
      if (i < currentIdx) a.classList.add('is-done');
      if (i === currentIdx) {
        a.classList.add('is-current');
        a.setAttribute('aria-current', 'page');
      }
      journeyNav.appendChild(a);
    });
    journeyHost.insertBefore(journeyNav, journeyHost.firstChild);
  }

  // Flip cards (services)
  document.querySelectorAll('.flip-card').forEach((card) => {
    const toggleFlip = () => {
      const isFlipped = card.classList.toggle('is-flipped');
      card.setAttribute('aria-pressed', String(isFlipped));
    };
    card.addEventListener('click', toggleFlip);
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggleFlip();
      }
    });
  });

  // Scroll progress bar
  const scrollProgress = document.getElementById('scrollProgress');
  if (scrollProgress) {
    const updateProgress = () => {
      const scrollable = document.documentElement.scrollHeight - window.innerHeight;
      const pct = scrollable > 0 ? (window.scrollY / scrollable) * 100 : 0;
      scrollProgress.style.width = pct + '%';
    };
    updateProgress();
    window.addEventListener('scroll', updateProgress, { passive: true });
    window.addEventListener('resize', updateProgress);
  }

  // Reveal-on-scroll
  const revealEls = document.querySelectorAll('.reveal');

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
    );

    revealEls.forEach((el) => observer.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add('is-visible'));
  }
}

// ---- Cookie consent + consent-gated analytics ----
// To enable analytics, paste your provider's script URL below. It only ever
// loads after a visitor presses Accept. Leave empty to keep analytics off.
const ANALYTICS_SRC = '';
const CONSENT_KEY = '3we4-consent';

function getConsent() {
  try { return localStorage.getItem(CONSENT_KEY); } catch (e) { return null; }
}
function setConsent(value) {
  try { localStorage.setItem(CONSENT_KEY, value); } catch (e) {}
}
function loadAnalytics() {
  if (!ANALYTICS_SRC || document.querySelector('script[data-analytics]')) return;
  const s = document.createElement('script');
  s.src = ANALYTICS_SRC;
  s.defer = true;
  s.setAttribute('data-analytics', '');
  document.head.appendChild(s);
}
function showConsentBanner() {
  if (document.getElementById('consentBanner')) return;
  const b = document.createElement('div');
  b.id = 'consentBanner';
  b.className = 'consent';
  b.setAttribute('role', 'dialog');
  b.setAttribute('aria-label', 'Cookie preferences');
  b.innerHTML = '<p>We use optional analytics cookies to see which pages help visitors. Nothing loads unless you accept. <a href="privacy.html">Privacy policy</a></p>' +
    '<div class="consent-actions"><button type="button" class="btn btn-ghost btn-small" data-consent="declined">Decline</button>' +
    '<button type="button" class="btn btn-primary btn-small" data-consent="accepted">Accept</button></div>';
  document.body.appendChild(b);
  b.querySelectorAll('[data-consent]').forEach((btn) => {
    btn.addEventListener('click', () => {
      setConsent(btn.dataset.consent);
      if (btn.dataset.consent === 'accepted') loadAnalytics();
      b.remove();
    });
  });
}
document.addEventListener('click', (e) => {
  if (e.target.closest('#cookieSettings')) showConsentBanner();
});
if (getConsent() === 'accepted') loadAnalytics();
else if (!getConsent()) window.addEventListener('load', showConsentBanner);

// ---- Newsletter form validation ----
document.addEventListener('submit', (e) => {
  const form = e.target.closest('.footer-newsletter');
  if (!form) return;
  const input = form.querySelector('input[type="email"]');
  const err = form.querySelector('.form-error');
  const value = input.value.trim();
  const ok = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value);
  if (!ok) {
    e.preventDefault();
    err.textContent = value ? 'That email address doesn\u2019t look right. Please check it.' : 'Please enter your email address.';
    err.hidden = false;
    input.setAttribute('aria-invalid', 'true');
    input.focus();
  } else {
    err.hidden = true;
    input.removeAttribute('aria-invalid');
  }
});
