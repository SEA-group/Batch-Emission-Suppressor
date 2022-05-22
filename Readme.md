# Batch texture compressor

![GitHub last commit](https://img.shields.io/github/last-commit/SEA-group/Batch-Emission-Suppressor)
![GitHub issues](https://img.shields.io/github/issues-raw/SEA-group/Batch-Emission-Suppressor)

A script that decreases the max Blue value of all *_mg.dds, in order to reduce the power of glowing effect.

This project is derived from [my previous "Compressed Texture Mod" generator](https://github.com/SEA-group/Batch-Texture-Compressor); written and tested in Anaconda Python 3.8.5 64-bit.

## How it works
Pillow (PIL) is able to read .dds files up to BC7, but it can't save image in .dds; Wand(ImageMagick) is capable to load and write .dds but it doesn't support BC7/DXT10. So I have to use both libraries, which can't share image data between them. Finally the idea is to use Pillow to read dds and save modified image in png, then use Wand to convert png to dds.

## Requirement and preparation
Although the tool is supposed to do all the job by just one click, it does require some additional works before the first use. 
1. Install pillow library: in cmd or powershell, type `pip install pillow`
2. Install wand library: in cmd or powershell, type `pip install wand`
3. Install ImageMagick **and set envionment variable** for it: please follow [this page](https://docs.wand-py.org/en/0.6.6/guide/install.html#install-imagemagick-on-windows). 

**Attention:** The choice between ImageMagick x86 and x64 depends on your Python, not your OS. For example I have 32-bit Python on 64-bit Windows, so I must install 32-bit ImageMagick
![Screenshot](https://raw.githubusercontent.com/SEA-group/Batch-Emission-Suppressor/main/Installation%20instructions/ImageMagick_Installation_1.png)

## How to use
1. Put *EmissionSuppressor.py* in `res_mods/content/`, beside `gameplay/`
2. Open *EmissionSuppressor.py* with a certain text editor
3. Assign the max Blue value (i.e. the B in RGBA color) in line 19
4. Save and run *Texture_Compressor.py*. I suggest to run it by double click or in cmd/powershell, in order to avoid path problems.
