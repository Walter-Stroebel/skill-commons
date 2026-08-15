@echo off
mkdir skills 2>nul
powershell Compress-Archive -Force -Path mindmap\SKILL.md,mindmap\layout.py,mindmap\references -DestinationPath skills\mindmap.skill
powershell Compress-Archive -Force -Path session-json\SKILL.md -DestinationPath skills\session-json.skill
powershell Compress-Archive -Force -Path enshittification-detector\SKILL.md -DestinationPath skills\enshittification-detector.skill
powershell Compress-Archive -Force -Path false-binary\SKILL.md -DestinationPath skills\false-binary.skill
powershell Compress-Archive -Force -Path struggle\SKILL.md -DestinationPath skills\struggle.skill
powershell Compress-Archive -Force -Path multilingual-search\SKILL.md -DestinationPath skills\multilingual-search.skill
powershell Compress-Archive -Force -Path numeracy-triage\SKILL.md -DestinationPath skills\numeracy-triage.skill
powershell Compress-Archive -Force -Path controlled-cot\SKILL.md -DestinationPath skills\controlled-cot.skill
powershell Compress-Archive -Force -Path java-style\SKILL.md -DestinationPath skills\java-style.skill
echo Built: skills\*.skill
