
[app]

title = MONU Scientific Calculator
package.name = monuscientificcalculator
package.domain = org.monu

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = 
android.archs = arm64-v8a

android.api = 35
android.minapi = 24
android.ndk = 27c

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1

