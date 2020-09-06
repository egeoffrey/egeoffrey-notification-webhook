# egeoffrey-notification-webhook

This is an eGeoffrey notification package.

## Description

forward notifications via a POST to a webhook URL, useful for integrating with IFTTT or Zapier.

## Install

To install this package, run the following command from within your eGeoffrey installation directory:
```
egeoffrey-cli install egeoffrey-notification-webhook
```
After the installation, remember to run also `egeoffrey-cli start` to ensure the Docker image of the package is effectively downloaded and started.
To validate the installation, go and visit the *'eGeoffrey Admin'* / *'Packages'* page of your eGeoffrey instance. All the modules, default configuration files and out-of-the-box contents if any will be automatically deployed and made available.
## Content

The following modules are included in this package.

For each module, if requiring a configuration file to start, its settings will be listed under *'Module configuration'*. Additionally, if the module is a service, the configuration expected to be provided by each registered sensor associated to the service is listed under *'Service configuration'*.

To configure each module included in this package, once started, click on the *'Edit Configuration'* button on the *'eGeoffrey Admin'* / *'Modules'* page of your eGeoffrey instance.
- **notification/webhook**: forward notifications to a webhook
  - Module configuration:
    - *url**: the URL of the webhook (e.g. https://maker.ifttt.com/trigger/event/asdasdasdqwdq789712ueikjhaskjf7as9)
    - *house_name_key*: the name of the JSON key the House Name will be passed along (e.g. house_name)
    - *severity_key*: the name of the JSON key the severity of the notification will be passed along (e.g. severity)
    - *message_key*: the name of the JSON key the message of the notification will be passed along (e.g. message)

## Contribute

If you are the author of this package, simply clone the repository, apply any change you would need and run the following command from within this package's directory to commit your changes and automatically push them to Github:
```
egeoffrey-cli commit "<comment>"
```
After taking this action, remember you still need to build (see below) the package (e.g. the Docker image) to make it available for installation.

If you are a user willing to contribute to somebody's else package, submit your PR (Pull Request); the author will take care of validating your contributation, merging the new content and building a new version.

## Build

Building is required only if you are the author of the package. To build a Docker image and automatically push it to [Docker Hub](https://hub.docker.com/r/egeoffrey/egeoffrey-notification-webhook), run the following command from within this package's directory:
```
egeoffrey-cli build egeoffrey-notification-webhook
```

## Uninstall

To uninstall this package, run the following command from within your eGeoffrey installation directory:
```
egeoffrey-cli uninstall egeoffrey-notification-webhook
```
Remember to run also `egeoffrey-cli start` to ensure the changes are correctly applied.
## Tags

The following tags are associated to this package:
```
notification webhook ifttt zapier
```

## Version

The version of this egeoffrey-notification-webhook is 1.0-1 on the master branch.
