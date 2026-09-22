# Ice Cream Cabinet Object Detection

## Project Goal

Build a computer vision system that can detect and count ice cream cartons inside a cabinet.

---

## Problem Statement

Manual inventory checking is time consuming.

The goal is to:

1. Capture cabinet images/video
2. Extract frames
3. Annotate cartons
4. Train YOLO
5. Detect cartons automatically
6. Count inventory

---

## Current Phase

✅ Video Collection

✅ Frame Extraction

✅ Cabinet Cropping

🔄 Annotation

⬜ YOLO Training

⬜ Object Detection

⬜ Inventory Counting

---

## Project Pipeline

Video
↓
Frame Extraction
↓
Cabinet Cropping
↓
Annotation
↓
YOLO Training
↓
Object Detection
↓
Inventory Count

---

## Dataset Structure

Data/

raw/
videos/

interim/
extracted_frames/
cropped_frames/

dataset/
images/
labels/

---

## Annotation Rules

Class Name:

box

Annotate:

✅ Ice cream cartons

✅ Partially visible cartons

Do NOT annotate:

❌ Shelf

❌ Cabinet frame

❌ Glass reflections

❌ Empty spaces

❌ Brand banners

---

## Annotation Tool

LabelImg

Format:

YOLO

Annotation Class:

box

---

## Team Workflow

1. Extract frames
2. Crop cabinet area
3. Annotate images
4. Commit annotation files
5. Train YOLO

---

## Future Scope

- SKU Detection
- Inventory Tracking
- Cabinet Monitoring
- Real-time Detection



## Git Workflow

Main Branch

main

Feature Branch Example

feature/annotation

feature/yolo-training

feature/dataset-cleanup

Commit Format

feat: add frame extraction script

docs: update annotation guide

fix: correct ROI cropping