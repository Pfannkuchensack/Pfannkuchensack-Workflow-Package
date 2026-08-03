from invokeai.app.invocations.baseinvocation import BaseInvocation, invocation
from invokeai.app.invocations.fields import InputField
from invokeai.app.invocations.primitives import StringOutput
from invokeai.app.services.shared.invocation_context import InvocationContext


@invocation(
    "pfannis_dummy_node",
    title="Pfannis Dummy Node",
    tags=["dummy", "passthrough", "utility"],
    category="util",
    version="1.0.0",
)
class PfannisDummyNode(BaseInvocation):
    """Passes a string through unchanged.

    This pack exists to ship the workflows in `workflows/`. InvokeAI only installs a node
    pack that contains at least one importable `__init__.py`, so this node is what makes
    the pack installable — it is deliberately trivial and has no side effects.

    It is not entirely useless: dropped into a graph it works as a labelled reroute for
    strings, which is handy for keeping a long prompt chain readable.
    """

    value: str = InputField(default="", description="The string to pass through.")

    def invoke(self, context: InvocationContext) -> StringOutput:
        return StringOutput(value=self.value)
