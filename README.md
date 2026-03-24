# mmWave Visualization Demo

This repo is a small reconstruction of the kind of workflow I used in a past project involving mmWave data.

The original project work cannot be shared because of NDA restrictions, so this example focuses on the visualization side and the general processing flow rather than the original implementation.

## Background

In that work, I was involved in handling sensor output, processing it into a usable format, and building visualization components so the data could be interpreted in real time.

This repo is not meant to represent a full production sensor pipeline. It is a simple example that shows the general direction of how point cloud style data can be visualized.

## Simplified Processing Flow

ADC data -> FFT -> Range / Doppler processing -> Detection -> Point Cloud -> Visualization

## What This Demo Includes

- simple simulated point cloud generation
- color mapping based on velocity values
- basic visualization with matplotlib

## Why This Repo Exists

I put this together as a practical example of how I think about the visualization side of sensor data.

A lot of the real work in these systems is not just collecting data, but turning it into something that can actually be interpreted and used. That was a big part of the work I did.

## Files

### `mmwave_demo.py`
A small Python example that generates sample point cloud style data and plots it.

### `notes.txt`
A short note explaining the context of the demo.

## Running the Demo

Install the dependencies first:

```bash
pip install numpy matplotlib
