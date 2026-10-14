[app]
title = MaCalculatrice
package.name = calculatrice
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy

orientation = all
fullscreen = 0

android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.permissions = 

[buildozer]
log_level = 2
warn_on_root = 1
