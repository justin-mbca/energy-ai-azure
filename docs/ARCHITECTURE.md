# System Architecture

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

This architecture supports scalable, reproducible AI/ML workflows for the energy industry, leveraging Azure ML, OpenAI, and Databricks.