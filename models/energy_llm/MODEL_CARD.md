# Model Card: Energy LLM (LoRA Fine-tuned)

## Model Details
- Model Type: Llama-3.1-8B or Mistral-7B + LoRA
- Version: 1.0.0
- Date: 2026-01-10
- Developers:  Xiangli Zhang
- License: MIT

## Intended Use
- Primary Use: Energy domain Q&A, document summarization
- Intended Users: Energy analysts, engineers, researchers
- Out-of-Scope: General-purpose chat, legal/financial advice

## Training Data
- Source: EIA reports, Wikipedia, scraped energy docs
- Size: [To be filled after data collection]
- Features: Instruction-tuning Q&A pairs
- Preprocessing: Cleaning, deduplication, QLoRA quantization

## Evaluation
- Metrics: Perplexity, domain accuracy
- Test Set: Holdout Q&A pairs
- Performance: [To be filled after training]
- Fairness: [To be filled after subgroup analysis]

## Ethical Considerations
- Bias: Domain-specific, may reflect source bias
- Environmental: QLoRA for energy efficiency

## Monitoring & Maintenance
- Drift Detection: Periodic eval on new docs
- Retraining Trigger: Accuracy drop > 5%
- Owner:  Xiangli Zhang (justinzhang.xl@gmail.com)
