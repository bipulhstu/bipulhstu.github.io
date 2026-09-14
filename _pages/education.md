---
layout: archive
title: "Education"
permalink: /education/
author_profile: true
---

<div class="education-page">
  <section class="education-degree" aria-labelledby="masters-degree">
    <h2 id="masters-degree" class="education-degree__title">M.Sc. (Engineering) in Computer Science and Engineering</h2>
    <p class="education-degree__university">Hajee Mohammad Danesh Science and Technology University</p>
    <p class="education-degree__location">Dinajpur, Bangladesh</p>
    <div class="education-degree__dates">
      <p><time datetime="2025-01">Jan 2025</time> &ndash; Present</p>
      <span class="education-degree__status">Expected <time datetime="2026-12">Dec 2026</time></span>
    </div>

    <div class="education-degree__research">
      <h3>Research focus</h3>
      <p>Self-supervised contrastive and masked representation learning for reliable arrhythmia classification from noisy multi-lead ECG signals.</p>
    </div>

    <dl class="education-degree__details">
      <dt>Supervisor</dt>
      <dd><a href="https://hstu.ac.bd/teacher/ashis" target="_blank" rel="noopener noreferrer">Dr. Ashis Kumar Mandal</a></dd>
      <dt>Assistantship</dt>
      <dd>Graduate Research Assistant, 2025&ndash;2026</dd>
      <dt>CGPA</dt>
      <dd>3.65 / 4.00 <span class="education-degree__context">(through the final semester)</span></dd>
    </dl>
  </section>

  <section class="education-degree" aria-labelledby="bachelors-degree">
    <h2 id="bachelors-degree" class="education-degree__title">B.Sc. (Engineering) in Electrical and Electronic Engineering</h2>
    <p class="education-degree__university">Hajee Mohammad Danesh Science and Technology University</p>
    <p class="education-degree__location">Dinajpur, Bangladesh</p>
    <div class="education-degree__dates">
      <p><time datetime="2015">2015</time> &ndash; <time datetime="2019-12">Dec 2019</time></p>
      <span class="education-degree__status">Completed</span>
    </div>

    <dl class="education-degree__details">
      <dt>Parallel degree</dt>
      <dd>Completed the Computer Science and Engineering degree alongside the Electrical and Electronic Engineering degree.</dd>
      <dt>CGPA</dt>
      <dd>2.92 / 4.00</dd>
    </dl>
  </section>

  <nav class="education-links" aria-label="Related academic information">
    <a href="{{ '/publications/' | relative_url }}">View research <span aria-hidden="true">&rarr;</span></a>
    <a href="{{ '/pdf/cv_bipul_islam.pdf' | relative_url }}" download>Download CV (PDF)</a>
  </nav>
</div>

<style>
/* These styles apply only to the Education page content. */
.education-page {
  --education-accent: rgb(0, 76, 153);
  --education-muted: #515d69;
  --education-tint: #f2f6fa;
  margin: 1.5rem 0;
  padding: 1.75rem;
  border: 1px solid var(--global-border-color);
  border-radius: 12px;
  background: var(--global-bg-color);
  color: var(--global-text-color);
  font-size: 0.95rem;
  line-height: 1.6;
  overflow-wrap: anywhere;
}

.education-page ::selection {
  background: var(--education-accent);
  color: #fff;
}

.education-page a,
.education-page a:visited {
  color: var(--education-accent);
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 0.18em;
}

.education-page a:hover {
  color: var(--education-accent);
  text-decoration-thickness: 2px;
}

.education-page a:focus-visible {
  outline: 2px solid var(--education-accent);
  outline-offset: 3px;
  box-shadow: 0 0 0 5px #fff;
  border-radius: 2px;
}

.education-page .education-degree + .education-degree {
  margin-top: 1.75rem;
  padding-top: 1.75rem;
  border-top: 1px solid var(--global-border-color);
}

.education-page .education-degree__title {
  margin: 0 0 0.65rem;
  font-size: 1.15rem;
  line-height: 1.4;
}

.education-page .education-degree__university {
  margin: 0;
  font-weight: 600;
}

.education-page .education-degree__location {
  margin: 0.15rem 0 0;
  color: var(--education-muted);
}

.education-page .education-degree__dates {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.45rem 0.8rem;
  margin: 0.65rem 0 1.1rem;
  color: var(--education-muted);
  font-size: 0.9rem;
}

.education-page .education-degree__dates p {
  margin: 0;
}

.education-page .education-degree__status {
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  background: #e8eff6;
  color: var(--education-accent);
  font-size: 0.85rem;
  font-weight: 600;
}

.education-page .education-degree__research {
  margin: 1.1rem 0;
  padding: 0.9rem 1rem;
  border-left: 3px solid var(--education-accent);
  border-radius: 0 6px 6px 0;
  background: var(--education-tint);
}

.education-page .education-degree__research h3 {
  margin: 0 0 0.35rem;
  font-size: 0.95rem;
  line-height: 1.5;
}

.education-page .education-degree__research p {
  margin: 0;
}

.education-page .education-degree__details {
  display: grid;
  grid-template-columns: max-content minmax(0, 1fr);
  gap: 0.55rem 1rem;
  margin: 1rem 0 0;
}

.education-page .education-degree__details dt {
  margin: 0;
  font-weight: 600;
}

.education-page .education-degree__details dd {
  margin: 0;
}

.education-page .education-degree__context {
  color: var(--education-muted);
}

.education-page .education-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1.5rem;
  margin-top: 1.75rem;
  padding-top: 1.1rem;
  border-top: 1px solid var(--global-border-color);
}

.education-page .education-links a {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  min-height: 44px;
  font-weight: 600;
}

html[data-theme="dark"] .education-page {
  --education-muted: #d4dce4;
  --education-tint: #383e45;
}

/* A light backing keeps the requested navy link color readable in dark mode. */
html[data-theme="dark"] .education-page a {
  padding: 0.1em 0.3em;
  border-radius: 3px;
  background: #e8eff6;
  box-decoration-break: clone;
  -webkit-box-decoration-break: clone;
}

@media (max-width: 600px) {
  .education-page {
    padding: 1.15rem 1rem;
  }

  .education-page .education-degree__title {
    font-size: 1.05rem;
  }

  .education-page .education-degree__dates {
    align-items: flex-start;
    flex-direction: column;
  }

  .education-page .education-degree__details {
    grid-template-columns: minmax(0, 1fr);
    gap: 0.15rem;
  }

  .education-page .education-degree__details dd + dt {
    margin-top: 0.65rem;
  }

  .education-page .education-links {
    align-items: flex-start;
    flex-direction: column;
  }
}
</style>
