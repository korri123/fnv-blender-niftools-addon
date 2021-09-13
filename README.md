# Blender Niftools Add-on adapted for Fallout New Vegas
 
This is a fork of the [Blender Niftools Addon](https://github.com/niftools/blender_niftools_addon) with some slight tweaks to make animation export for Fallout New Vegas possible. This is released here until the official add-on is updated with the features and appropriate bug fixes so that it can work with FNV natively. The code changes are not ideal/generalized enough for other games or in some cases just hacky which is why I haven't opened PRs to the official repo.

This add-on is developed and tested for **Blender 2.92**.

# Changes

- KF file export: it is required that you export to a location containing the `skeleton.nif` file of the animation you are working on.
- .blend files saved in 2.49b are not supported for export due to correction matrices in old niftools add-on which are no longer used in the current version.
- Bones can be excluded from export, so that they do not need to be deleted in SNIFF or after baking.
- Multiple bones can be selected and it's priorities or bone exclusion state can be edited.
- In import under armature settings, you can check `NV Weapon Skeleton Fix` to fix bones facing the wrong axis due to a bug in the orientation guessing algorithm in the blender add-on.

# Installation
- Download the .zip source code of this repository and select the .zip in the install add-on panel in Blender.