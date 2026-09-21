---
layout: archive
title: "Education"
permalink: /education/
author_profile: true
---

<div class="education-page">

  <div class="edu-card">
    <div class="edu-card__body">
      <h2 class="edu-card__title">M.Sc. (Engineering) in Computer Science and Engineering</h2>
      <p class="edu-card__university">Hajee Mohammad Danesh Science and Technology University</p>
      <p class="edu-card__location">Dinajpur, Bangladesh</p>
      <div class="edu-card__dates">
        <span class="edu-card__period"><time datetime="2025-01">Jan 2025</time> &ndash; Present</span>
        <span class="edu-card__status edu-card__status--active">Expected <time datetime="2026-12">Dec 2026</time></span>
      </div>

      <div class="edu-card__research">
        <h3>Research Focus</h3>
        <p>Self-supervised contrastive and masked representation learning for reliable arrhythmia classification from noisy multi-lead ECG signals.</p>
      </div>

      <dl class="edu-card__details">
        <div class="edu-card__detail-row">
          <dt>Supervisor</dt>
          <dd><a href="https://hstu.ac.bd/teacher/ashis" target="_blank" rel="noopener noreferrer">Dr. Ashis Kumar Mandal</a></dd>
        </div>
        <div class="edu-card__detail-row">
          <dt>Assistantship</dt>
          <dd>Graduate Research Assistant, 2025&ndash;2026</dd>
        </div>
        <div class="edu-card__detail-row">
          <dt>CGPA</dt>
          <dd><strong>3.65</strong> / 4.00 <span class="edu-card__context">(through the final semester)</span></dd>
        </div>
      </dl>
    </div>
  </div>

  <div class="edu-card">
    <div class="edu-card__body">
      <h2 class="edu-card__title">B.Sc. (Engineering) in Electrical and Electronic Engineering</h2>
      <p class="edu-card__university">Hajee Mohammad Danesh Science and Technology University</p>
      <p class="edu-card__location">Dinajpur, Bangladesh</p>
      <div class="edu-card__dates">
        <span class="edu-card__period"><time datetime="2015">2015</time> &ndash; <time datetime="2019-12">Dec 2019</time></span>
        <span class="edu-card__status edu-card__status--done">Completed</span>
      </div>

      <dl class="edu-card__details">
        <div class="edu-card__detail-row">
          <dt>Parallel Degree</dt>
          <dd>Completed the Computer Science and Engineering degree alongside the Electrical and Electronic Engineering degree.</dd>
        </div>
        <div class="edu-card__detail-row">
          <dt>CGPA</dt>
          <dd><strong>2.92</strong> / 4.00</dd>
        </div>
      </dl>
    </div>
  </div>

  <nav class="edu-links" aria-label="Related academic information">
    <a href="{{ '/publications/' | relative_url }}">View research <span aria-hidden="true">&rarr;</span></a>
    <a href="{{ '/pdf/cv_bipul_islam.pdf' | relative_url }}" download>Download CV (PDF)</a>
  </nav>

</div>

<style>
/* ── Education page styles ── */
.education-page {
  --edu-accent: rgb(0, 76, 153);
  --edu-muted: #515d69;
  --edu-tint: #f2f6fa;
  margin: 1rem 0;
}

.edu-card {
  margin-bottom: 1.5rem;
  padding: 1.3rem 1.4rem;
  border-left: 3px solid var(--edu-accent);
  border-radius: 6px;
  background: var(--global-bg-color, #fff);
  box-shadow: 0 1px 4px rgba(0,0,0,.06);
  transition: box-shadow .2s ease;
}
.edu-card:hover {
  box-shadow: 0 3px 12px rgba(0,0,0,.1);
}

.edu-card__title {
  margin: 0 0 0.3rem;
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1.35;
  color: var(--global-text-color, #222);
}

.edu-card__university {
  margin: 0;
  font-weight: 600;
  font-size: 0.95rem;
}

.edu-card__location {
  margin: 0.1rem 0 0;
  color: var(--edu-muted);
  font-size: 0.9rem;
}

.edu-card__dates {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.5rem 1rem;
  margin: 0.7rem 0 1rem;
}

.edu-card__period {
  color: var(--edu-muted);
  font-size: 0.9rem;
}

.edu-card__status {
  padding: 0.2rem 0.65rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
}
.edu-card__status--active {
  background: #e8f5e9;
  color: #2e7d32;
}
.edu-card__status--done {
  background: #e8eff6;
  color: var(--edu-accent);
}

.edu-card__research {
  margin: 0.8rem 0 1rem;
  padding: 0.85rem 1rem;
  border-left: 3px solid var(--edu-accent);
  border-radius: 0 6px 6px 0;
  background: var(--edu-tint);
}

.edu-card__research h3 {
  margin: 0 0 0.3rem;
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--edu-accent);
}

.edu-card__research p {
  margin: 0;
  font-size: 0.92rem;
  line-height: 1.6;
}

.edu-card__details {
  margin: 0.8rem 0 0;
  padding: 0;
}

.edu-card__detail-row {
  display: flex;
  gap: 0.8rem;
  padding: 0.4rem 0;
  border-bottom: 1px solid rgba(0,0,0,.05);
}
.edu-card__detail-row:last-child {
  border-bottom: none;
}

.edu-card__details dt {
  flex: 0 0 auto;
  min-width: 120px;
  margin: 0;
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--edu-muted);
}

.edu-card__details dd {
  margin: 0;
  font-size: 0.92rem;
  line-height: 1.55;
}

.edu-card__details dd a {
  color: var(--edu-accent);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 0.18em;
}
.edu-card__details dd a:hover {
  text-decoration-thickness: 2px;
}

.edu-card__context {
  color: var(--edu-muted);
  font-size: 0.88em;
}

.edu-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1.5rem;
  margin-top: 0.5rem;
  padding-top: 1rem;
  border-top: 1px solid var(--global-border-color, #e0e0e0);
}

.edu-links a {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  font-weight: 600;
  font-size: 0.92rem;
  color: var(--edu-accent);
  text-decoration: underline;
  text-underline-offset: 0.18em;
}
.edu-links a:hover {
  text-decoration-thickness: 2px;
}

/* ── Dark mode ── */
html[data-theme="dark"] .education-page {
  --edu-muted: #a8b8c8;
  --edu-tint: #2a2f36;
}
html[data-theme="dark"] .edu-card {
  background: var(--global-bg-color, #1a1a2e);
  box-shadow: 0 1px 4px rgba(0,0,0,.25);
  border-left-color: #4a90d9;
}
html[data-theme="dark"] .edu-card__title {
  color: var(--global-text-color, #e0e0e0);
}
html[data-theme="dark"] .edu-card__status--active {
  background: #1b4332;
  color: #81c784;
}
html[data-theme="dark"] .edu-card__status--done {
  background: #1e3a5f;
  color: #7eb8f7;
}
html[data-theme="dark"] .edu-card__research {
  border-left-color: #4a90d9;
}
html[data-theme="dark"] .edu-card__research h3 {
  color: #7eb8f7;
}
html[data-theme="dark"] .edu-card__detail-row {
  border-bottom-color: rgba(255,255,255,.06);
}
html[data-theme="dark"] .edu-card__details dd a,
html[data-theme="dark"] .edu-links a {
  color: #7eb8f7;
}
html[data-theme="dark"] .edu-links {
  border-top-color: #333;
}

@media (max-width: 600px) {
  .edu-card {
    padding: 0.9rem 1rem;
  }
  .edu-card__title {
    font-size: 1rem;
  }
  .edu-card__dates {
    flex-direction: column;
    align-items: flex-start;
  }
  .edu-card__detail-row {
    flex-direction: column;
    gap: 0.15rem;
  }
  .edu-card__details dt {
    min-width: auto;
  }
  .edu-links {
    flex-direction: column;
  }
}
</style>
