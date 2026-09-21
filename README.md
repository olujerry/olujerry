<div align="center">

# Oluseye Jeremiah Oluwapelumi

**AI/ML Engineer · Building production AI for low-resource healthcare settings**

[![Location](https://img.shields.io/badge/📍-Ibadan%2C%20Nigeria-1d4ed8?style=flat-square)](https://en.wikipedia.org/wiki/Ibadan)
[![Focus](https://img.shields.io/badge/Focus-AI%20in%20Healthcare-7C3AED?style=flat-square)](#)
[![Email](https://img.shields.io/badge/Email-oluseyejeremiah%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:oluseyejeremiah@gmail.com)

</div>

---

I build AI systems that work where connectivity fails and hardware is constrained. My focus is **edge AI for African healthcare** — models small enough to run on a Raspberry Pi, architectures designed for the clinic, not the data centre.

Currently finishing my MSc in Data Science at the University of Ibadan, where my dissertation work produced **MalarAI**: an offline-capable malaria diagnosis system that puts clinical-grade deep learning on a low-end Android device or single-board computer.

---

## Featured Project

### 🔬 [MalarAI](https://github.com/olujerry/MalarAI) — Malaria Diagnosis at the Edge

> *EfficientNet-B0 · TFLite int8 · Grad-CAM · MedGemma · FastAPI · React PWA · Flutter*

Blood smear image → AI diagnosis in under 2 seconds, fully offline.

- **3-tier edge deployment** — Server (EfficientNet Keras), Mid-range (MobileNetV2 float16), Low-end (MobileNetV2 int8, 3.8 MB, ~900 ms on RPi 4)
- **Explainable AI** — Grad-CAM heatmaps highlight the parasitised cells that drove the decision
- **MedGemma** narrative — a 1.5B parameter medical LLM produces a clinical-language explanation
- **Offline queue** — predictions saved to NDJSON locally, synced to backend on reconnect
- **Device-aware model selection** — auto-detects RAM/CPU/GPU at startup, picks the right model

NIH dataset · 27,558 labelled cell images · AUC-ROC ≥ 0.98 (EfficientNet-B0)

---

## Stack

```
Deep Learning    TensorFlow · Keras · TFLite · PyTorch (MedASR)
Edge AI          TFLite Runtime · int8 quantisation · ARM deployment
LLMs             MedGemma 1.5 4B · HuggingFace Transformers
Backend          FastAPI · Uvicorn · Python 3.10
Mobile           Flutter · Dart
Web              React · Vite · Tailwind CSS
Data             NumPy · OpenCV · scikit-learn · Pandas
```

---

## What I'm Working On

- 🔬 **MalarAI** — federated learning across clinic nodes; P. vivax / P. malariae species classification
- 📱 Flutter on-device TFLite inference (`tflite_flutter` integration)
- 🌍 Expanding edge healthcare AI to TB and anaemia screening

---

<div align="center">
<sub>MSc Data Science · University of Ibadan · Supervisor: Adebola Ojo</sub>
</div>
