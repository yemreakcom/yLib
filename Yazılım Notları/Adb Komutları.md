# ADB Komutları <!-- omit in toc -->

Android telefonları için komutları barındırır.

## İçerikler <!-- omit in toc -->

> `HOME` tuşu ile yukarı yönlenebilrsiniz.

- [Adb Server](#adb-server)
- [Adb Reboot](#adb-reboot)
- [Shell](#shell)
- [Devices](#devices)
- [Get device android version](#get-device-android-version)
- [LogCat](#logcat)
- [Files](#files)
- [App install](#app-install)
- [Uninstalling app from device](#uninstalling-app-from-device)
- [Update app](#update-app)
- [Home button](#home-button)
- [Activity Manager](#activity-manager)
- [Print text](#print-text)
- [Screenshot](#screenshot)
- [Key event](#key-event)
- [ShPref](#shpref)
- [replace org.example.app with your application id](#replace-orgexampleapp-with-your-application-id)
- [Add a value to default shared preferences](#add-a-value-to-default-shared-preferences)
- [Remove a value to default shared preferences](#remove-a-value-to-default-shared-preferences)
- [Clear all default shared preferences](#clear-all-default-shared-preferences)
- [It's also possible to specify shared preferences file](#its-also-possible-to-specify-shared-preferences-file)
- [Data types](#data-types)
- [Restart application process after making changes](#restart-application-process-after-making-changes)
- [Monkey](#monkey)
- [Other](#other)
- [Shared Preferences](#shared-preferences)
  - [Add a value to default broadcast shared preferences](#add-a-value-to-default-broadcast-shared-preferences)
  - [Remove a value to default broadcast shared preferences](#remove-a-value-to-default-broadcast-shared-preferences)
  - [Clear all default broadcast shared preferences](#clear-all-default-broadcast-shared-preferences)
  - [It's also possible to specify shared broadcast preferences file](#its-also-possible-to-specify-shared-broadcast-preferences-file)
  - [Broadcast Data types](#broadcast-data-types)
  - [Restart broadcast application process after making changes](#restart-broadcast-application-process-after-making-changes)
- [Few bash snippets](#few-bash-snippets)
- [Using tail -n](#using-tail--n)
- [Using cut -sf](#using-cut--sf)
- [Using xargs -I](#using-xargs--i)
- [Three options below together](#three-options-below-together)
- [Using alias](#using-alias)

## Adb Server

- adb kill-server
- adb start-server

## Adb Reboot

- adb reboot
- adb reboot recovery
- adb reboot-bootloader

## Shell

adb shell    > Open or run commands in a terminal on the host Android device.

## Devices

- adb usb
- adb devices   >show devices attached
- adb connect ip_address_of_device

## Get device android version

adb shell getprop ro.build.version.release

## LogCat

- adb logcat
- adb logcat -c > clear > The parameter -c will clear the current logs on the - device.
- adb logcat -d > [path_to_file] > Save the logcat output to a file on the local - system.
- adb bugreport > [path_to_file] > Will dump the whole device information like dumpstate, dumpsys and logcat output.

## Files

- adb push [source] [destination]    > Copy files from your computer to your phone.
- adb pull [device file location] [local file location] > Copy files from your phone to your computer.

## App install

- adb -e install path/to/app.apk

  - `-d`                        - directs command to the only connected USB device...
  - `-e`                       - directs command to the only running emulator...
  - `-s <serial number>`        ...
  - `-p <product name or path>` ...

The flag you decide to use has to come before the actual adb command:

- adb devices | tail -n +2 | cut -sf 1 | xargs -IX adb -s X install -r com.myAppPackage > Install the given app on all connected devices.

## Uninstalling app from device

- db uninstall com.myAppPackage
- db uninstall <app .apk name>
- db uninstall -k <app .apk name> -> "Uninstall .apk withour deleting data"
- db shell pm uninstall com.example.MyApp
- db shell pm clear [package] > Deletes all data associated with a package.
- db devices | tail -n +2 | cut -sf 1 | xargs -IX adb -s X uninstall com.myAppPackage >Uninstall the given app from all connected devices

## Update app

- adb install -r yourApp.apk  >  -r means re-install the app and keep its data on the device.
- adb install –k <.apk file path on computer>

## Home button

- adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN

## Activity Manager

- adb shell am start -a android.intent.action.VIEW
- adb shell am broadcast -a 'my_action'

- adb shell am start -a android.intent.action.CALL -d tel:+972527300294 > Make a call

> Open send sms screen with phone number and the message:

- adb shell am start -a android.intent.action.SENDTO -d sms:+972527300294   --es  sms_body "Test --ez exit_on_sent false

> Reset permissions

- adb shell pm reset-permissions -p your.app.package
- adb shell pm grant [packageName] [ Permission]  > Grant a permission to an app.
- adb shell pm revoke [packageName] [ Permission]   > Revoke a permission from an app.

> Emulate device

- adb shell wm size 2048x1536
- adb shell wm density 288

> And reset to default

- adb shell wm size reset
- adb shell wm density reset

## Print text

- adb shell input text 'Wow, it so cool feature'

## Screenshot

- adb shell screencap -p /sdcard/screenshot.png

- $ adb shell
- shell@ $ screencap /sdcard/screen.png
- shell@ $ exit
- $ adb pull /sdcard/screen.png
- adb shell screenrecord /sdcard/NotAbleToLogin.mp4
- $ adb shell
- shell@ $ screenrecord --verbose /sdcard/demo.mp4
- (press Control + C to stop)
- shell@ $ exit
- $ adb pull /sdcard/demo.mp4

## Key event

- adb shell input keyevent 3 > Home btn
- adb shell input keyevent 4 > Back btn
- adb shell input keyevent 5 > Call
- adb shell input keyevent 6 > End call
- adb shell input keyevent 26  > Turn Android device ON and OFF. It will toggle - device to on/off status.
- adb shell input keyevent 27 > Camera
- adb shell input keyevent 64 > Open browser
- adb shell input keyevent 66 > Enter
- adb shell input keyevent 67 > Delete (backspace)
- adb shell input keyevent 207 > Contacts
- adb shell input keyevent 220 / 221 > Brightness down/up
- adb shell input keyevent 277 / 278 /279 > Cut/Copy/Paste

> https:>developer.android.com/reference/android/view/KeyEvent.html

## ShPref

## replace org.example.app with your application id

## Add a value to default shared preferences

- adb shell 'am broadcast -a org.example.app.sp.PUT --es key key_name --es value "hello world!"'

## Remove a value to default shared preferences

- adb shell 'am broadcast -a org.example.app.sp.REMOVE --es key key_name'

## Clear all default shared preferences

- adb shell 'am broadcast -a org.example.app.sp.CLEAR --es key key_name'

## It's also possible to specify shared preferences file

- adb shell 'am broadcast -a org.example.app.sp.PUT --es name Game --es key level --ei value 10'

## Data types

- adb shell 'am broadcast -a org.example.app.sp.PUT --es key string --es value "hello world!"'
- adb shell 'am broadcast -a org.example.app.sp.PUT --es key boolean --ez value true'
- adb shell 'am broadcast -a org.example.app.sp.PUT --es key float --ef value 3.14159'
- adb shell 'am broadcast -a org.example.app.sp.PUT --es key int --ei value 2015'
- adb shell 'am broadcast -a org.example.app.sp.PUT --es key long --el value 9223372036854775807'

## Restart application process after making changes

- adb shell 'am broadcast -a org.example.app.sp.CLEAR --ez restart true'

## Monkey

- adb shell monkey -p com.myAppPackage -v 10000 -s 100

> monkey tool is generating 10.000 random events on the real device

## Other

- adb backup > Create a full backup of your phone and save to the computer.
- adb restore > Restore a backup to your phone.
- adb sideload >  Push and flash custom ROMs and zips from your computer.
- fastboot devices

> Check connection and get basic information about devices connected to the - computer.
>
> This is essentially the same command as adb devices from earlier.
>
> However, it works in the bootloader, which ADB does not. Handy for ensuring - that you have properly established a connection.

--------------------------------------------------------------------------------

## Shared Preferences

> replace org.example.app with your application id

### Add a value to default broadcast shared preferences

- adb shell 'am broadcast -a org.example.app.sp.PUT --es key key_name --es value "hello world!"'

### Remove a value to default broadcast shared preferences

- adb shell 'am broadcast -a org.example.app.sp.REMOVE --es key key_name'

### Clear all default broadcast shared preferences

- adb shell 'am broadcast -a org.example.app.sp.CLEAR --es key key_name'

### It's also possible to specify shared broadcast preferences file

- adb shell 'am broadcast -a org.example.app.sp.PUT --es name Game --es key level --ei value 10'

### Broadcast Data types

- adb shell 'am broadcast -a org.example.app.sp.PUT --es key string --es value - "hello world!"'
- adb shell 'am broadcast -a org.example.app.sp.PUT --es key boolean --ez value - true'
- adb shell 'am broadcast -a org.example.app.sp.PUT --es key float --ef value - 3.14159'
- adb shell 'am broadcast -a org.example.app.sp.PUT --es key int --ei value 2015'
- adb shell 'am broadcast -a org.example.app.sp.PUT --es key long --el value 9223372036854775807'

### Restart broadcast application process after making changes

- adb shell 'am broadcast -a org.example.app.sp.CLEAR --ez restart true'

--------------------------------------------------------------------------------

## Few bash snippets

@Source (https:>jonfhancock.com/bash-your-way-to-better-android-development-1169bc3e0424)

## Using tail -n

>Use tail to remove the first line. Actually two lines. The first one is just a newline. The second is “List of devices attached.”
$ adb devices | tail -n +2

## Using cut -sf

> Cut the last word and any white space off the end of each line.
$ adb devices | tail -n +2 | cut -sf -1

## Using xargs -I

> Given the -I option, xargs will perform an action for each line of text that we feed into it.
> We can give the line a variable name to use in commands that xargs can execute.
$ adb devices | tail -n +2 | cut -sf -1 | xargs -I X echo X aw yiss

## Three options below together

> Will print android version of all connected devices
adb devices | tail -n +2 | cut -sf -1 | xargs -I X adb -s X shell getprop ro.build.version.release  

## Using alias

- -- Example 1
- alias tellMeMore=echo
- tellMeMore "hi there"
- Output => hi there
- -- Example 2
- > Define alias
- alias apkinstall="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X - install -r $1"
- > And you can use it later
- apkinstall ~/Downloads/MyAppRelease.apk  > Install an apk on all devices
- -- Example 3
- alias rmapp="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X uninstall - $1"
- rmapp com.example.myapp > Uninstall a package from all devices
- -- Example 4
- alias clearapp="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X shell - pm clear $1"
- clearapp com.example.myapp  > Clear data on all devices (leave installed)
- -- Example 5
- alias startintent="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X - shell am start $1"
- startintent https:>twitter.com/JonFHancock > Launch a deep link on all devices

Setting up your .bash_profile
Finally, to make this all reusable even after rebooting your computer (aliases only last through the current session), we have to add these to your .bash_profile. You might or might not already have a .bash_profile, so let’s make sure we append to it rather than overwriting it. Just open a terminal, and run the following command

touch .bash_profile && open .bash_profile

This will create it if it doesn’t already exist, and open it in a text editor either way. Now just copy and paste all of the aliases into it, save, and close.

- alias startintent="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X - shell am start $1"
- alias apkinstall="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X - install -r $1"
- alias rmapp="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X uninstall - $1"
- alias clearapp="adb devices | tail -n +2 | cut -sf 1 | xargs -I X adb -s X shell - pm clear $1"
