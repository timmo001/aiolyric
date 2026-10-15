---
name: diagnose
description: Investigate bugs using source, observed failures, and proportionate verification. Use for regressions, intermittent failures, incorrect behaviour, or performance problems whose cause needs investigation.
license: MIT
---

# Diagnose

Use this skill for debugging work where ad-hoc inspection is likely to miss the cause.

## Redaction

- Redact secrets from commands, output, logs, traces, and captured artefacts shown to the agent.
- Prefer passing credentials through environment variables rather than command arguments.
- Quote only the signal-bearing lines from authenticated artefacts.
- If redaction removes evidence needed to diagnose the bug, ask the user for a safe way to inspect it.

## When to Use

- Bug reports and behavioural regressions
- Failing or flaky tests
- Intermittent errors or wrong output
- Performance regressions that need measurement before a fix

## When NOT to Use

- Broad codebase exploration with no concrete failure mode
- Pure refactors or cleanup work
- Type, lint, or formatting errors that already have a direct fix path

## Workflow

1. Establish the failure from available evidence.
   - Read the reported symptom, relevant code, logs, and existing checks. Code inspection can establish a useful hypothesis before a runnable reproducer exists.
   - Choose the smallest practical verification: an existing test, CLI invocation, HTTP request, captured trace, or authorised UI check. No particular tool is the default.
   - Build a temporary reproducer only when it resolves uncertainty that existing evidence cannot. Do not add a permanent test or a new harness just to begin diagnosis.
   - For intermittent failures, use targeted instrumentation or bounded repeated attempts when they are likely to distinguish causes. Avoid arbitrary repetition counts.
   - If reproduction is unavailable, state the limitation and continue with source and recorded evidence where useful. Ask for access or a human-only action only when it blocks progress; [hitl-loop.template.sh](scripts/hitl-loop.template.sh) is available for repeatable human-driven checks.
2. Reproduce and minimise the reported problem when practical.
    - Confirm any reproducer matches the user's actual failure, not a nearby symptom.
    - If the issue is flaky, use the evidence to choose which condition to probe next.
    - Shrink the repro one input, caller, config value, data item, or step at a time. Keep only elements that are load-bearing for the failure.
3. Rank hypotheses.
    - Name the plausible causes supported by the evidence when the cause is not obvious; do not fill a quota.
    - Use this shape: "If <X> is the cause, then <changing Y> will make the bug disappear or <changing Z> will make it worse."
    - Share the ranked list when user or domain context is likely to change the order materially.
4. Instrument narrowly.
    - Prefer debuggers, targeted logs, or focused measurements over broad logging.
    - Map each probe to one hypothesis prediction and change one variable at a time.
    - For performance regressions, establish a baseline measurement first. Prefer profilers, timing harnesses, query plans, and bisection over logs.
    - Tag temporary debug logs with a unique prefix so they are easy to remove.
5. Fix with lightweight verification.
    - Prefer the smallest verification that proves the real failure path is fixed.
    - If you deliberately mutate code or a fixture to check that verification detects the failure, compare it with a pristine copy before trusting the failing result.
    - Apply `testing`: add regression coverage when it catches a meaningful failure that existing checks miss. Explain the benefit; an ordinary case can qualify without being a rare edge case.
    - If no good test seam exists, use another practical verification rather than forcing one or proposing architecture changes for an optional test.
6. Verify the fix and clean up.
    - Re-run the original check when available. Otherwise state what source or recorded evidence supports the fix and what remains unverified.
    - Remove temporary instrumentation and throwaway harnesses unless they remain intentionally useful.
    - State the hypothesis that turned out to be correct in the final explanation, commit message, or PR text where relevant.
    - If the failure was a failing systemd unit, crash, out-of-memory kill, or logged error on a machine triage collects from, apply `triage-resolve` to close its triage issues.

## Tool Guidance

- Start with narrow local reads and searches before broad exploration.
- For browser-specific bugs, apply `browser-access` before using Chrome DevTools or any other browser tool.
- Use tests, CLI commands, curl, small repro scripts, or harnesses to create deterministic loops.
- Do not trim normal command output with `head` or `tail`. If a repro command is genuinely huge, capture output to a file and inspect targeted sections with `Grep` or `Read` offsets instead of re-running.
- If project glossary, ADRs, or local architecture docs exist, use them to avoid misreading terms or constraints.
- Ask one targeted question only when a missing detail blocks diagnosis.

## Done Checklist

- The original failure is reproduced or the missing repro constraint is stated clearly.
- The fix is checked against the original failure where possible, with any verification limits stated.
- Any added regression coverage meets `testing` and names the meaningful failure or important behaviour it protects, or the explicit requirement.
- Temporary debug instrumentation is removed.
- Any remaining uncertainty or follow-up risk is called out explicitly.
