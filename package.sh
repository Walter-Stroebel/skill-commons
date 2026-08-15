#!/bin/bash
mkdir -p skills
cd mindmap && zip -r ../skills/mindmap.skill SKILL.md layout.py references/ && cd ..
cd session-json && zip -r ../skills/session-json.skill SKILL.md && cd ..
cd enshittification-detector && zip -r ../skills/enshittification-detector.skill SKILL.md && cd ..
cd false-binary && zip -r ../skills/false-binary.skill SKILL.md && cd ..
cd struggle && zip -r ../skills/struggle.skill SKILL.md && cd ..
cd multilingual-search && zip -r ../skills/multilingual-search.skill SKILL.md && cd ..
cd numeracy-triage && zip -r ../skills/numeracy-triage.skill SKILL.md && cd ..
cd controlled-cot && zip -r ../skills/controlled-cot.skill SKILL.md && cd ..
cd java-style && zip -r ../skills/java-style.skill SKILL.md && cd ..
echo "Built: skills/*.skill"
