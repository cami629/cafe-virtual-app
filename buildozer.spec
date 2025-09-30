[app]
title = Cafe Virtual
package.name = cafevirtual
package.domain = org.cafe
source.dir = .
version = 1.0
requirements = python3,kivy
presplash.filename = %(source.dir)s/logo.png
icon.filename = %(source.dir)s/logo.png
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[android]
api = 33
minapi = 21
ndk_version = 25b
android.accept_sdk_license = True

[python]
version = 3.10.0
