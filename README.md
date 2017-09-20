# Dotbot ```yum``` Plugin

Plugin for [Dotbot](https://github.com/anishathalye/dotbot), that adds ```yum``` directive, which allows you to install and upgrade packages using ```yum```.

&nbsp;

## Installation

1. Simply add this repo as a submodule of your dotfiles repository:

  `git submodule add https://gitlab.com/flyingchipmunk/dotbot-yum.git`

2. Pass this folder (or directly yum.py file) path with corresponding flag to your [Dotbot](https://github.com/anishathalye/dotbot) script:

 `-p /path/to/file/yum.py`

  or

 `--plugin-dir /pato/to/plugin/folder`


 **WARNING!**

 Dotbot (or install script) needs to be executed with root permissions (as sudo) in order to install/upgrade packages. It is strongly recommended to place ```yum``` tasks in a separate config!

&nbsp;

## Options
`assumeyes` - will pass the flag `--assumeyes` to yum

`quiet` - will pass the flag `--quiet` to yum


## Defaults
Default options are applied to all ```yum``` tasks, but can be overridden per task.

&nbsp;

### Example
```yaml
- defaults:
    yum:
        quiet: true
        assumeyes: true
```

&nbsp;

## Supported task variants
The various formats supported are shown below. If you want to bundle a group of packages in the same ```yum``` call use the list format. This is important if you have cross dependencies on the yum packages in your list. i.e. package_one depends on package_two, use this format `- yum: [package_one, package_two]`. It also speeds up the process as the dependency scan only happens once instead of for each package individually.

&nbsp;

### Formats Supported
```yaml
- yum: package_one
```
```yaml
- yum: [package_one, package_two, package_three]
```
```yaml
- yum:
    package_one:
        quiet: false
        assumeyes: true
    package_two:
    package_three:
```
_Note:_ This last format will do individual yum calls for each package. If there are dependencies between your listed packages it will fail.

&nbsp;

## Usage

### Example ```packages.conf.yaml```
The suggested format is to group as many packages as possible in lists and set the default options.

```yaml
- defaults:
    yum:
        quiet: true
        assumeyes: true

- yum: [gcc, poco-devel, libjson-devel]
```

&nbsp;

### Execution
```bash
./install -p dotbot-yum/yum.py -c packages.conf.yaml
```

### Output
![cli_out]
