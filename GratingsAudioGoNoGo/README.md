# Audio Go-NoGo Task

## Description

The task is a closed-loop go-nogo behavioral task in which, on each trial, the subject is presented with either an audio or gratings stimulis. For the entire task, one stimuli will be labeled as go and the rest are labeled as nogo. If a subject responds within the expected time period when the go stimulus is presented, the subject will receive a water reward.

## Trial Information
- A trial is presented every 3 seconds
- A stimuli is displayed at the start for 2 seconds
- If the subject responds within 100 milliseconds of stimulus presentation onset, a response is registered
	- For the "go" stimulus, a reward is issued

## Parameterizing Stimuli

### Gratings
All files in the `stimuli\gratings` with the suffix `.csv` will be parsed as parameters for individual gratings stimuli. The format of these files is expected to be:
- “,” delineated
- first row should be parameter names
	- supported parameters:
		- Angle: Angle of the stimulus in degrees
- second row should be values to associate with the aforementioned variable names
	

### Audio
All files in the `stimuli\audio` with the suffix `.wav` will be parsed as parameters for individual gratings stimuli. The expected sample rate is 44.1kHz.

### Choosing a go stimulus
By default the go stimulus is `stimuli\gratings\0.csv`, to change which stimulus is labeled as the “go” stimulus, edit the externalized workflow parameter `Value` in the Bonsai workflow editor. Other stimuli with file paths not matching this value will be labeled as “nogo”.  

## Current Status
Hardware interaction outside of audio playback is not yet enabled. Gamma correction is disabled by default but can be enabled by enabling it within the Bonsai workflow editor.

## Requirements
Bonsai 0.7.0 (other versions may work but have not been tested)
The following Bonsai packages are also required:
- BonVision (community package)
- Bonsai - Windows Input Library
- Bonsai - Vision Library

## Workflow overview

### Main
![Main](main.svg)

### Trial Selection
![Trial Selection](trial-selection.svg)

### Go Audio Trial
![Go Audio Trial](go-audio-trial.svg)

### NoGo Audio Trial
![NoGo Audio Trial](nogo-audio-trial.svg)

### Go Gratings Trial
![Go Gratings Trial](go-gratings-trial.svg)

### NoGo Gratings Trial
![NoGo Gratings Trial](nogo-gratings-trial.svg)

## Issues

This was developed with the intent to be open loop however there were difficulties driving the task without a timer. Since it is driven by a timer, the task is closed-loop because the timer cannot be dynamically parameterized to allow for variable duration trials.