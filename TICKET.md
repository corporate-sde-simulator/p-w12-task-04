# OPS-402: Fix Broken Alerting Rules

**Status:** In Progress · **Priority:** High
**Sprint:** Sprint 33 · **Story Points:** 5
**Reporter:** On-Call Team · **Assignee:** You (Intern)
**Labels:** `alerts`, `monitoring`, `python`, `bug-fix`
**Task Type:** Bug Fix

---

## Description

The alerting system is firing wrong alerts: critical alerts for minor issues,
and missing alerts for actual problems. Three alert rules have broken conditions.

## Acceptance Criteria

- [ ] CPU alert triggers at > 90%, not > 9%
- [ ] Memory alert checks USED percentage, not FREE
- [ ] Error rate alert uses per-minute rate, not total count
- [ ] All tests pass
