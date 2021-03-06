# generated by fastapi-codegen:
#   filename:  openapi.yml
#   timestamp: 2022-04-12T11:47:03+00:00

from __future__ import annotations

from typing import List, Union

from fastapi import FastAPI, Path

from .models import (
    DiscoveryResponse,
    LogEntry,
    OcrdExecutable,
    Processor,
    ProcessorArgs,
    ProcessorJob,
    ProcessorList,
    Workflow,
    WorkflowJob,
    Workspace,
)

app = FastAPI(
    title='OCR-D Web API',
    description='# HTTP API for offering OCR-D processing\n> This document defines the [data model](#/components/schemas) and various HTTP APIs related to OCR-D\n## OCR-D API compatibility\nAn implementation may claim compatibility with a `OCR-D ${N} API v{$V}` iff\n\n  * it implements all the methods tagged `${N}`\n  * at major version `${V}` of this API definition\n\n## Media types\n### `application/json`\nContent serialized as `application/json` is defined by the [data model](#/components/schema)\n### `application/vnd.ocrd+zip`\nDefined in [https://ocr-d.de/en/spec/ocrd_zip](https://ocr-d.de/en/spec/ocrd_zip)\n### `text/vnd.ocrd.workflow`\nWorkflow format, currently (April 2022) still to be determined.\n',
    contact={'email': 'info@ocr-d.de'},
    license={
        'name': 'Apache 2.0',
        'url': 'http://www.apache.org/licenses/LICENSE-2.0.html',
    },
    version='0.0.1',
    servers=[
        {
            'url': 'https://example.org/ocrd/v1',
            'description': 'The URL of your server offering the OCR-D API.',
        }
    ],
)


@app.get('/discovery', response_model=DiscoveryResponse)
def discover() -> DiscoveryResponse:
    pass


@app.get('/processor', response_model=ProcessorList)
def list_processors() -> ProcessorList:
    pass


@app.get('/processor/{executable}', response_model=Processor)
def get_processor(executable) -> Processor:
    pass


@app.post('/processor/{executable}', response_model=ProcessorJob)
def run_processor(
    executable, body: ProcessorArgs = ...
) -> ProcessorJob:
    pass


@app.get('/processor/{executable}/{job_id}', response_model=ProcessorJob)
def get_processor_job(
    executable, job_id: str = Path(..., alias='job-id')
) -> ProcessorJob:
    pass


@app.get('/processor/{executable}/{job_id}/log', response_model=None)
def get_processor_job_log(
    executable, job_id: str = Path(..., alias='job-id')
) -> None:
    pass


@app.post('/processor/{executable}/{job_id}/log', response_model=None)
def post_processor_job_log_entry(
    executable, job_id: str = Path(..., alias='job-id')
) -> None:
    pass


@app.post('/workflow', response_model=Workflow)
def post_workflow() -> Workflow:
    pass


@app.put('/workflow/{workflow_id}', response_model=Workflow)
def put_workflow(workflow_id: str = Path(..., alias='workflow-id')) -> Workflow:
    pass


@app.get('/workflow/{workflow_id}', response_model=Workflow)
def get_workflow(workflow_id: str = Path(..., alias='workflow-id')) -> Workflow:
    pass


@app.post('/workflow/{workflow_id}', response_model=WorkflowJob)
def run_workflow(workflow_id: str = Path(..., alias='workflow-id')) -> WorkflowJob:
    pass


@app.get('/workflow/{workflow_id}/{job_id}', response_model=WorkflowJob)
def get_workflow_job(
    workflow_id: str = Path(..., alias='workflow-id'),
    job_id: str = Path(..., alias='job-id'),
) -> WorkflowJob:
    pass


@app.get('/workspace', response_model=List[Workspace])
def get_workspaces() -> List[Workspace]:
    pass


@app.post('/workspace', response_model=None, responses={'201': {'model': Workspace}})
def create_workspace() -> Union[None, Workspace]:
    """
    Post a new workspace
    """
    pass


@app.put('/workspace/{workspace_id}', response_model=Workspace)
def replace_workspace(workspace_id: str = Path(..., alias='workspace-id')) -> Workspace:
    """
    Replace an existing workspace
    """
    pass


@app.get('/workspace/{workspace_id}', response_model=Workspace)
def get_workspace(workspace_id: str = Path(..., alias='workspace-id')) -> Workspace:
    pass


@app.delete('/workspace/{workspace_id}', response_model=Workspace)
def delete_workspace(workspace_id: str = Path(..., alias='workspace-id')) -> Workspace:
    pass
