from typing import Annotated, Any, Literal

from pydantic import Field
from tracecat import identifiers

from tracecat_registry import RegistryActionError, registry


@registry.register(
    namespace="core.workflow",
    description="Execute a child workflow. The child workflow inherits the parent's execution context.",
    default_title="Execute Child Workflow",
    display_group="Workflows",
)
async def execute(
    workflow_id: Annotated[
        identifiers.WorkflowID,
        Field(
            ...,
            description=("The title of the child workflow. "),
        ),
    ],
    trigger_inputs: Annotated[
        dict[str, Any],
        Field(
            ...,
            description="The inputs to pass to the child workflow.",
        ),
    ],
    environment: Annotated[
        str | None,
        Field(
            description=(
                "The child workflow's target execution environment. "
                "This is used to isolate secrets across different environments."
                "If not provided, the child workflow's default environment is used. "
            ),
        ),
    ] = None,
    version: Annotated[
        int | None,
        Field(..., description="The version of the child workflow definition, if any."),
    ] = None,
    loop_strategy: Annotated[
        Literal["parallel", "batch", "sequential"],
        Field(
            ...,
            description="The execution strategy to use for the child workflow.",
        ),
    ] = "parallel",
    batch_size: Annotated[
        int,
        Field(
            ...,
            description="The number of child workflows to execute in parallel.",
        ),
    ] = 16,
    fail_strategy: Annotated[
        Literal["isolated", "all"],
        Field(
            ...,
            description="Fail strategy to use when a child workflow fails.",
        ),
    ] = "isolated",
) -> Any:
    raise RegistryActionError(
        "This UDF only defines a controller interface and cannot be invoked directly."
        "If you are seeing this error, please contact your administrator."
    )