## Design Philosophy

Trinity Engine deliberately treats an LLM as a semantic planning component—not as an autonomous executor.

Where deterministic algorithms exist, they should be preferred.

Authority increases only after validation.

Capability knowledge remains localized to each capability.

The goal is not to maximize AI autonomy.
The goal is to maximize system reliability.

### Why deterministic execution?
Execution should be separated from the LLM. Having determinisitc code handle execution makes the system reliable and testable.
### Why capabilities?
Capabilities act as a contract to let users plug and play different modules into the Trinity Engine and keeps these capabilities self contained.
### Why JSON as the planning contract?
JSON allows for schema validation, easy parsing for value validation, and easy logging of the LLM output.
### Why keep domain knowledge inside capabilities?
The execution engine does not need to own the rules, validation schemas, and execution handling of capabilities. The capabilities should own those and be the arbiters of the information.

## Threat model

Trinity Engine treats all LLM-generated output as untrusted. The engine is designed to constrain model behavior by requiring generated plans and commands to pass deterministic structural and domain validation before they can reach execution.

Trinity does not claim to defend against compromise of the host system, runtime, dependencies, credentials, capability implementations, or other conventional cybersecurity threats. Its security architecture specifically addresses the trust boundary between probabilistic model output and deterministic application behavior.
