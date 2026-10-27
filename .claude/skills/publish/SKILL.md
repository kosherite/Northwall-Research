---
name: publish
description: Take a finished Northwall draft through supervisory review and publication (for example "/publish AGI OnePager").
---

# Publish: $ARGUMENTS

1. Run `python tools/build_model.py <T>` and `python tools/check_report.py <T>`; stop on failure and route it to the owner.
2. **supervisory-analyst**: full checklist review; writes the signed checklist.
3. If approved, **publishing-desk**: final PDF, logs, tracker, library index, git commit.
4. Report the published file, the decision record and the commit.
