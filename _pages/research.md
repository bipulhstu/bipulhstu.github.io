---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

<div class="research-page">

  <div class="research-statement">
    <h2 class="research-section__title">Research Statement</h2>
    <hr class="research-section__rule">
    <p>My research focuses on developing <strong>reliable, interpretable, and trustworthy AI systems for healthcare applications</strong>. I am motivated by the gap between high-performing deep learning models and their safe deployment in clinical settings — where noisy data, distribution shifts, and the need for human understanding of model decisions present fundamental challenges.</p>
    <p>Currently, I investigate <strong>self-supervised representation learning</strong> to build robust ECG classifiers that maintain accuracy under real-world noise conditions, and <strong>explainable neural architectures</strong> that provide clinically meaningful explanations for their predictions. My work bridges signal processing, deep learning, and clinical informatics, with an emphasis on methods that generalize across patient populations and healthcare systems.</p>
    <p>I am seeking a <strong>PhD position (Fall 2027)</strong> to deepen this research agenda — developing ML methods that are not only accurate but also robust, interpretable, and safe for deployment in high-stakes medical decision-making.</p>
  </div>

  <div class="research-projects">
    <h2 class="research-section__title">Research Projects</h2>
    <hr class="research-section__rule">

    <div class="research-card">
      <h3 class="research-card__title">Self-Supervised ECG Representation Learning for Reliable Arrhythmia Classification</h3>
      <p class="research-card__meta">
        <span class="research-card__role">Lead Researcher</span>
        <span class="research-card__period">Jan 2025 &ndash; Present</span>
      </p>
      <p class="research-card__supervisor">Supervisor: <a href="https://hstu.ac.bd/teacher/ashis" target="_blank" rel="noopener noreferrer">Dr. Ashis Kumar Mandal</a></p>
      <div class="research-card__content">
        <p><strong>Motivation:</strong> Clinical ECG recordings are inherently noisy due to electrode artifacts, patient movement, and device variability. Standard supervised classifiers degrade significantly under these conditions, limiting their real-world reliability.</p>
        <p><strong>Approach:</strong> We develop a self-supervised pretraining framework combining <em>contrastive learning</em> and <em>masked signal modeling</em> to learn robust ECG representations from unlabeled multi-lead recordings. The pretrained encoder is then fine-tuned for arrhythmia classification, with uncertainty quantification to flag unreliable predictions.</p>
        <p><strong>Key contributions:</strong></p>
        <ul>
          <li>Novel pretraining strategy that combines contrastive and generative objectives for multi-lead ECG signals</li>
          <li>Systematic evaluation of robustness under synthetic and real-world noise conditions</li>
          <li>Uncertainty-aware classification with calibrated confidence scores for clinical decision support</li>
        </ul>
        <p class="research-card__status"><strong>Status:</strong> M.Sc. thesis research &mdash; manuscript in preparation for submission</p>
      </div>
    </div>

    <div class="research-card">
      <h3 class="research-card__title">AI-Based Potato Leaf Disease Detection with Farmer Guidance</h3>
      <p class="research-card__meta">
        <span class="research-card__role">Lead Researcher</span>
        <span class="research-card__period">2025 &ndash; Present</span>
      </p>
      <p class="research-card__supervisor">Funded by: Government of Bangladesh</p>
      <div class="research-card__content">
        <p><strong>Motivation:</strong> Potato is a staple crop in Bangladesh, and leaf diseases cause significant yield losses. Early, accurate detection enables timely intervention, but expert pathologists are scarce in rural areas.</p>
        <p><strong>Approach:</strong> We build a deep learning pipeline for automated leaf disease classification from smartphone images, paired with an actionable guidance system that recommends treatment protocols to farmers in local language.</p>
        <p><strong>Key contributions:</strong></p>
        <ul>
          <li>Custom curated dataset of potato leaf diseases from Bangladeshi farms</li>
          <li>Transfer learning with fine-tuned CNN architectures optimized for mobile deployment</li>
          <li>Farmer-facing guidance module providing actionable disease-specific treatment recommendations</li>
        </ul>
        <p class="research-card__status"><strong>Status:</strong> Government-funded research &mdash; manuscript in preparation</p>
      </div>
    </div>

    <div class="research-card">
      <h3 class="research-card__title">Explainable Physics-Informed Neural Networks for Health Risk Prediction</h3>
      <p class="research-card__meta">
        <span class="research-card__role">Lead Researcher</span>
        <span class="research-card__period">2025 &ndash; Present</span>
      </p>
      <div class="research-card__content">
        <p><strong>Motivation:</strong> Predictive models for clinical risk assessment often sacrifice interpretability for accuracy. In healthcare, understanding <em>why</em> a model predicts high risk is as important as the prediction itself.</p>
        <p><strong>Approach:</strong> We integrate physics-informed constraints into neural network architectures for tabular medical data, producing models that respect known clinical relationships while providing voxel-level and feature-level explanations for their predictions.</p>
        <p><strong>Key contributions:</strong></p>
        <ul>
          <li>Physics-informed regularization adapted for multi-condition medical tabular data</li>
          <li>Interpretable feature attribution aligned with established clinical knowledge</li>
          <li>Robustness evaluation across diverse patient populations and data quality levels</li>
        </ul>
        <p class="research-card__status"><strong>Status:</strong> Manuscript in preparation</p>
      </div>
    </div>

    <div class="research-card">
      <h3 class="research-card__title">Interpretable Brain Tumor Segmentation with Uncertainty Quantification</h3>
      <p class="research-card__meta">
        <span class="research-card__role">Co-Investigator</span>
        <span class="research-card__period">2025 &ndash; Present</span>
      </p>
      <div class="research-card__content">
        <p><strong>Motivation:</strong> Accurate brain tumor segmentation from multi-modal MRI is critical for surgical planning, yet existing models lack uncertainty estimates that clinicians need to assess prediction reliability.</p>
        <p><strong>Approach:</strong> We adapt foundation models for volumetric medical image segmentation, incorporating voxel-level uncertainty quantification to highlight regions where the model is less confident — enabling clinicians to identify areas requiring manual review.</p>
        <p><strong>Key contributions:</strong></p>
        <ul>
          <li>Foundation model adaptation strategy for 3D medical image segmentation</li>
          <li>Voxel-level uncertainty maps for clinical decision support in surgical planning</li>
          <li>Interpretable attention visualization aligned with radiological features</li>
        </ul>
        <p class="research-card__status"><strong>Status:</strong> Manuscript in preparation</p>
      </div>
    </div>

  </div>

</div>

<style>
/* ── Research page styles ── */
.research-page {
  --research-accent: rgb(0, 76, 153);
  margin: 0.5rem 0;
}

.research-section__title {
  color: var(--research-accent);
  font-size: 1.15rem;
  font-weight: 700;
  line-height: 1.4;
  letter-spacing: 0.02em;
  margin: 0 0 0.2rem;
}

.research-section__rule {
  border: none;
  border-top: 1px solid var(--global-border-color, #e0e0e0);
  margin: 0.4rem 0 1rem;
}

.research-statement {
  margin-bottom: 2rem;
  padding: 1.2rem 1.4rem;
  border-left: 3px solid var(--research-accent);
  border-radius: 6px;
  background: var(--global-bg-color, #fff);
  box-shadow: 0 1px 4px rgba(0,0,0,.06);
}

.research-statement p {
  font-size: 0.95rem;
  line-height: 1.7;
  margin: 0 0 0.8rem;
}
.research-statement p:last-child {
  margin-bottom: 0;
}

.research-card {
  margin-bottom: 1.5rem;
  padding: 1.2rem 1.4rem;
  border-left: 3px solid var(--research-accent);
  border-radius: 6px;
  background: var(--global-bg-color, #fff);
  box-shadow: 0 1px 4px rgba(0,0,0,.06);
  transition: box-shadow .2s ease;
}
.research-card:hover {
  box-shadow: 0 3px 12px rgba(0,0,0,.1);
}

.research-card__title {
  font-size: 1rem;
  font-weight: 700;
  margin: 0 0 0.3rem;
  color: var(--global-text-color, #222);
  line-height: 1.4;
}

.research-card__meta {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 0.3rem 1rem;
  color: #515d69;
  font-size: 0.88rem;
  margin-bottom: 0.2rem;
}

.research-card__role {
  font-weight: 600;
  color: var(--research-accent);
}

.research-card__period {
  white-space: nowrap;
  font-weight: 500;
  color: var(--research-accent);
}

.research-card__supervisor {
  color: #515d69;
  font-size: 0.88rem;
  margin: 0 0 0.5rem;
}

.research-card__supervisor a {
  color: #2980b9;
  text-decoration: none;
}
.research-card__supervisor a:hover {
  text-decoration: underline;
}

.research-card__content {
  font-size: 0.92rem;
  line-height: 1.65;
}
.research-card__content p {
  margin: 0.4rem 0;
}
.research-card__content ul {
  margin: 0.3rem 0 0.5rem;
  padding-left: 1.2rem;
}
.research-card__content li {
  margin-bottom: 0.2rem;
}

.research-card__status {
  margin-top: 0.5rem;
  padding: 0.4rem 0.8rem;
  background: #f8f9fa;
  border-radius: 4px;
  font-size: 0.88rem;
  color: #515d69;
}

/* ── Dark mode ── */
html[data-theme="dark"] .research-statement,
html[data-theme="dark"] .research-card {
  background: var(--global-bg-color, #1a1a2e);
  box-shadow: 0 1px 4px rgba(0,0,0,.25);
  border-left-color: #4a90d9;
}
html[data-theme="dark"] .research-section__title {
  color: #7eb8f7;
}
html[data-theme="dark"] .research-section__rule {
  border-top-color: #333;
}
html[data-theme="dark"] .research-card__title {
  color: var(--global-text-color, #e0e0e0);
}
html[data-theme="dark"] .research-card__meta,
html[data-theme="dark"] .research-card__supervisor {
  color: #a8b8c8;
}
html[data-theme="dark"] .research-card__role,
html[data-theme="dark"] .research-card__period {
  color: #7eb8f7;
}
html[data-theme="dark"] .research-card__status {
  background: #2a2f36;
  color: #a8b8c8;
}
html[data-theme="dark"] .research-card__supervisor a {
  color: #7eb8f7;
}

@media (max-width: 600px) {
  .research-statement,
  .research-card {
    padding: 0.9rem 1rem;
  }
  .research-card__meta {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
