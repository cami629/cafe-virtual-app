# Crear archivo buildozer.spec
spec_content = """
[app]
title = Cafe Virtual
package.name = cafevirtual
package.domain = org.example
source.dir = .
version = 0.1
requirements = python3,kivy,android
presplash.filename = %(source.dir)s/logo.png
icon.filename = %(source.dir)s/logo.png
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
api = 33
minapi = 21
ndk = 25b
p4a.branch = develop
android.accept_sdk_license = True
android.allow_backup = True
android.ndk_path = /content/android/ndk
android.sdk_path = /content/android

[android:meta-data]
android.enable_metrics = 0

[android:permission]
android.permission.INTERNET

[android:activity]
android.theme = @android:style/Theme.NoTitleBar

[python]
version = 3.10.0

[clean]
source.dir = %(source.dir)s
""".strip()

with open('buildozer.spec', 'w') as f:
    f.write(spec_content)