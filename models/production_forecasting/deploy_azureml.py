from azureml.core import Workspace, Model, Environment, InferenceConfig
from azureml.core.webservice import AciWebservice, Webservice

ws = Workspace.from_config()
model = Model.register(workspace=ws, model_path='tft_model.pth', model_name='tft_model')

env = Environment.from_conda_specification(name='tft-env', file_path='../../environment.yml')

inference_config = InferenceConfig(entry_script='score.py', environment=env)

deployment_config = AciWebservice.deploy_configuration(cpu_cores=2, memory_gb=4)

service = Model.deploy(
    workspace=ws,
    name='tft-endpoint',
    models=[model],
    inference_config=inference_config,
    deployment_config=deployment_config,
    overwrite=True
)
service.wait_for_deployment(show_output=True)
print(f"Deployed at: {service.scoring_uri}")
