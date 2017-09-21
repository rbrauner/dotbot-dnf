# Dotbot ```yum``` Plugin

Plugin for [Dotbot](https://github.com/anishathalye/dotbot), that adds ```yum``` directive, which allows you to install and upgrade packages using ```yum```.

## Installation

1) Simply add this repo as a submodule of your dotfiles repository:

```
git submodule add https://gitlab.com/flyingchipmunk/dotbot-yum.git
```

2) Pass this folder (or directly yum.py file) path with corresponding flag to your [Dotbot](https://github.com/anishathalye/dotbot) script:

```
-p /path/to/file/yum.py
```
  or

```
--plugin-dir /pato/to/plugin/folder`
```

 **WARNING!**

 Dotbot (or install script) needs to be executed with root permissions (as sudo) in order to install/upgrade packages. It is strongly recommended to place ```yum``` tasks in a separate config!

## Options
`options` - specify any command line options to be passed to yum

## Defaults
Default options are applied to all ```yum``` tasks, but can be overridden per task.

### Example
```yaml
- defaults:
    yum:
        options: "-q -y"
```

See `man yum` for possible command line options.

## Supported task variants
The various formats supported are shown below. If you want to bundle a group of packages in the same ```yum``` call use the list format. This speeds up the process as the dependency scan only happens once instead of for each package individually.


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
        options: "-v -y"
    package_two: "-q -y"
    package_three:
```
_Note:_ This last format will do individual yum calls for each package. If there are dependencies between your listed packages it will fail.

### Specifying package names
Again see `man yum` for more details, but in general these formats are supported by yum.
```
name
name.arch
name-ver
name-ver-rel
name-ver-rel.arch
name-epoch:ver-rel.arch
epoch:name-ver-rel.arch
```

## Usage

### Example ```packages.conf.yaml```
The suggested format is to group as many packages as possible in lists and set the default options.

```yaml
- defaults:
    yum:
        options: "-q -y"

- yum: [gcc, poco-devel, libjson-devel]
```

### Execution
```bash
./install -p dotbot-yum/yum.py -c packages.conf.yaml
```

### Output
Here is the output from a sample config showing all possible formats. It is an unrealistic config, but shows all supported formats and output.

![cli_out](https://i.imgur.com/OhoeL4f.png)
