#!/bin/bash
mkdir -p skills
cd mindmap && zip -r ../skills/mindmap.skill SKILL.md layout.py references/ && cd ..
cd session-json && zip -r ../skills/session-json.skill SKILL.md && cd ..
cd enshittification-detector && zip -r ../skills/enshittification-detector.skill SKILL.md && cd ..
cd false-binary && zip -r ../skills/false-binary.skill SKILL.md && cd ..
echo "Built: skills/*.skill"
