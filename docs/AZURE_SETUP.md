# Azure Setup Instructions

1. **Create Azure ML Workspace**
   - Follow [Azure ML docs](https://docs.microsoft.com/azure/machine-learning/how-to-manage-workspace) to create a workspace.
2. **Configure CLI & SDK**
   - `az login`
   - `az ml folder attach -w <workspace> -g <resource-group>`
3. **Set Up Compute**
   - Create compute cluster (Standard_DS3_v2 or GPU for LLM)
4. **Register Datasets**
   - Upload sample data to Azure ML datasets
5. **Configure OpenAI Service**
   - Deploy OpenAI resource in Azure Portal
   - Get API key and endpoint
6. **Set Environment Variables**
   - `AZUREML_WORKSPACE`, `AZURE_OPENAI_KEY`, etc.
7. **Test Connection**
   - Run a sample notebook in `notebooks/` to verify setup
