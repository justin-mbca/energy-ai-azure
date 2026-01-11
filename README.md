## Azure ML Workflow (Mermaid Diagram)

```mermaid
graph TD
  A[Data Ingestion] --> B[Feature Engineering]
  B --> C[Azure ML Experiment Tracking]
  C --> D[Model Training (TFT, LLM, RAG)]
  D --> E[Model Deployment (Azure ML Endpoint)]
  E --> F[Monitoring & Drift Detection]
  D --> G[Model Cards & Versioning]
  D --> H[Databricks Feature Store]
  F --> I[Automated Retraining]

  subgraph "Azure OpenAI"
    D
  end
```
# Enterprise AI Layered Adaptation (Global Context)

# Enterprise AI Layered Adaptation (Global Context)

This diagram illustrates a global, sector-specific approach to enterprise AI adaptation across Energy, Pharma, and Industrial domains. Each sector is represented as a swimlane, with layers flowing top-down to show the progression from prompt and policy control through to fine-tuning and distillation. The diagram highlights how each sector can leverage a single cloud platform (e.g., Azure for Energy and Pharma, AWS for Industrial) while sharing common architectural patterns and adaptation strategies. Horizontal links indicate shared concepts and best practices across sectors, while vertical flows show the recommended order of adaptation layers for robust, compliant, and domain-optimized AI deployment.

```mermaid
%% Enterprise AI Layered Adaptation Swimlane Diagram
%% Sectors are lanes, layers flow top-down
%% Shows recommended single cloud per sector
%% Paste into Mermaid live editor or compatible renderer

flowchart TD
  %% Core Layer Styles
  classDef coreLayer fill:#e0f7fa,stroke:#00796b,stroke-width:1px;
  classDef sectorLayer fill:#fff3e0,stroke:#ef6c00,stroke-width:1px,dasharray:5 5;

  %% Energy Lane (Azure)
  subgraph ENERGY ["Energy Sector (Azure)"]
    A1[Prompt & Policy Control: HSE rules, regulatory safety]:::sectorLayer
    B1[Inference-Time Control: Output stability, operational limits]:::sectorLayer
    C1[RAG: SOPs, manuals, incident reports]:::sectorLayer
    D1[Tool & Agent Orchestration: Diagnostics, operational workflows]:::sectorLayer
    E1[Post-Generation Validation: Human-in-the-loop, safety checks]:::sectorLayer
    F1[PEFT: LoRA / Adapters - Engineering language]:::sectorLayer
    G1[Full Fine-Tuning / Distillation: Edge tasks if needed]:::sectorLayer
  end

  %% Pharma Lane (Azure)
  subgraph PHARMA ["Pharma Sector (Azure)"]
    A2[Prompt & Policy Control: Clinical compliance, patient safety]:::sectorLayer
    B2[Inference-Time Control: Strict output validation]:::sectorLayer
    C2[RAG: Guidelines, trial protocols]:::sectorLayer
    D2[Tool & Agent Orchestration: Workflow automation, decision support]:::sectorLayer
    E2[Post-Generation Validation: Regulatory & quality review]:::sectorLayer
    F2[PEFT: LoRA / Adapters - Scientific/clinical terminology]:::sectorLayer
    G2[Full Fine-Tuning / Distillation: Specialized clinical tasks]:::sectorLayer
  end

  %% Industrial Lane (AWS)
  subgraph INDUSTRIAL ["Industrial OEM Sector (AWS)"]
    A3[Prompt & Policy Control: Operational & process boundaries]:::sectorLayer
    B3[Inference-Time Control: Stable output, safety constraints]:::sectorLayer
    C3[RAG: Engineering specs, maintenance logs]:::sectorLayer
    D3[Tool & Agent Orchestration: Predictive maintenance, root-cause analysis]:::sectorLayer
    E3[Post-Generation Validation: Human review, compliance checks]:::sectorLayer
    F3[PEFT: LoRA / Adapters - Equipment/process-specific language]:::sectorLayer
    G3[Full Fine-Tuning / Distillation: Edge tasks as needed]:::sectorLayer
  end

  %% Vertical flow of core layers
  A1 --> B1 --> C1 --> D1 --> E1 --> F1 --> G1
  A2 --> B2 --> C2 --> D2 --> E2 --> F2 --> G2
  A3 --> B3 --> C3 --> D3 --> E3 --> F3 --> G3

  %% Horizontal links to indicate shared layer concepts
  A1 --- A2 --- A3
  B1 --- B2 --- B3
  C1 --- C2 --- C3
  D1 --- D2 --- D3
  E1 --- E2 --- E3
  F1 --- F2 --- F3
  G1 --- G2 --- G3

  %% Optional: Label for cloud platform
  class ENERGY,PHARMA sectorLayer;
  class INDUSTRIAL sectorLayer;
```
# energy-ai-azure

![Azure ML](https://img.shields.io/badge/Azure%20ML-blue?logo=microsoft-azure) ![PyTorch](https://img.shields.io/badge/PyTorch-orange?logo=pytorch) ![Hugging Face](https://img.shields.io/badge/Hugging%20Face-yellow?logo=huggingface) ![Databricks](https://img.shields.io/badge/Databricks-red?logo=databricks) ![Chevron](https://img.shields.io/badge/Chevron-blue?logo=chevron)

## Problem Statement

Energy companies face unique challenges in production forecasting, supply chain optimization, and leveraging AI at scale. This portfolio demonstrates advanced Azure ML and Azure OpenAI workflows for the energy sector, targeting enterprise AI, foundation models, and MLOps best practices.

## Architecture

```mermaid
graph TD
    A[Data Ingestion] --> B[Feature Engineering]
    B --> C[Azure ML Experiment Tracking]
    C --> D[Model Training (TFT, LLM, RAG)]
    D --> E[Model Deployment (Azure ML Endpoint)]
    E --> F[Monitoring & Drift Detection]
    D --> G[Model Cards & Versioning]
    D --> H[Databricks Feature Store]
    F --> I[Automated Retraining]
    subgraph Azure OpenAI
      D
    end
```

## Quick Start

1. **Azure Setup**: See [docs/AZURE_SETUP.md](docs/AZURE_SETUP.md)
2. **Local Testing**: Clone repo, install dependencies (`pip install -r requirements.txt`), run notebooks in `notebooks/`
3. **Experiment Tracking**: Configure Azure ML workspace, run forecasting notebook
4. **LLM Fine-tuning**: Use LoRA scripts in `models/energy_llm/`
5. **RAG Demo**: Run RAG notebook with Azure OpenAI and ChromaDB

## Notebooks
- [01_production_forecasting_azureml.ipynb](notebooks/01_production_forecasting_azureml.ipynb): Oil well production forecasting with TFT, Azure ML logging, deployment, drift detection
- [02_energy_llm_lora_finetuning.ipynb](notebooks/02_energy_llm_lora_finetuning.ipynb): LLM fine-tuning (LoRA, QLoRA) on energy text, deployment, evaluation
- [03_rag_azure_openai_energy.ipynb](notebooks/03_rag_azure_openai_energy.ipynb): RAG for energy Q&A, Azure OpenAI embeddings, ChromaDB, cost tracking

## Why This Matters for Chevron
- Demonstrates scalable, reproducible AI/ML workflows for energy
- Transferable to production forecasting, supply chain, and document intelligence
- Aligns with Chevron’s focus on enterprise AI, MLOps, and foundation models

## Expanded Modules (Chevron Enterprise AI)

- **Seismic Imaging & Subsurface Modeling**: Deep learning for seismic, well log, and reservoir simulation data
- **Predictive Maintenance**: Equipment failure prediction, anomaly detection, sensor analytics
- **Robotics & Automation**: AI for robotics, field inspection, and safety monitoring
- **Emissions Monitoring & Optimization**: GHG tracking, carbon intensity, regulatory analytics
- **Energy Trading & Price Forecasting**: Market data, price prediction, risk optimization
- **Well Placement & Drilling Optimization**: Drilling path optimization, real-time analytics
- **Document Intelligence**: Automated parsing, search, and summarization of technical documents
- **Digital Twin & Asset Performance**: Real-time asset modeling, digital twin analytics
- **Human-in-the-Loop AI**: Decision support, expert feedback, active learning
- **Safety Incident Prediction & Analytics**: HSE analytics, near-miss detection, safety modeling

## Additional Data Sources
- Seismic and well log data (SEG-Y, LAS)
- IoT sensor streams (pressure, temperature, vibration)
- Maintenance logs and work orders
- Satellite and drone imagery
- SCADA data
- Market and trading data
- Technical documents (PDFs, reports, manuals)
- Environmental and regulatory data

---

For details, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) and [docs/MODEL_LIFECYCLE.md](docs/MODEL_LIFECYCLE.md).
