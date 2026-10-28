---
name: multimodal-workflows
description: "Handle user-provided images, audio or video and explicitly requested visual creation or edits with the native capabilities actually available."
---

# Multimodal Workflows

Apply the [shared workflow rules](../using-minhas-skills/references/workflow-rules.md) once.

## Identify the requested operation

Separate **interpretation** (describe, compare, extract or explain attached media), **transformation** (edit a supplied image or media), and **generation** (make a new image or other supported media). Words such as 'design', 'show' or 'visualize' do not by themselves authorize generation. Do not add an illustration merely because the topic is visual.

Check which source media are really available in this conversation and what the host can actually process. If the essential media or modality is unavailable, explain the limitation without inventing frames, transcripts, observations or tool results.

## Respect modality and user intent

- For provided images, analyze what is visible and separate observations from interpretation. Never infer that a real person is a particular named individual from an image.
- For image editing, preserve requested subject matter and honor precise additions, removals and stylistic changes; use the native image-editing tool when available.
- For new images, use image generation only when the user actually requests an image output and an image tool is available.
- For audio or video, rely on accessible recordings, transcriptions or frames. Do not claim live camera, screen, continuous microphone or video access without that capability.
- When creating a report from media, use [file-workflows](../file-workflows/SKILL.md) only if a reusable file is requested.

Do not publish personal media, extract hidden identifiers or upload private material to unrelated services without appropriate authorization.

## Completion check

Give the requested explanation or media result, not a description of imagined work. Name any uncertainty caused by missing angles, unreadable details, poor audio, incomplete frames or lack of an editing tool. Avoid claiming an asset is complete before the actual output is available.
