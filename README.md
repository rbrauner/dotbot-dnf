# Dotbot ```yum``` Plugin

Plugin for [Dotbot](https://github.com/anishathalye/dotbot), that adds ```yum``` directive, which allows you to install and upgrade packages and groups using ```yum```.

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
--plugin-dir /path/to/plugin/folder
```

 **WARNING!**

 Dotbot (or install script) needs to be executed with root permissions (as sudo) in order to install/upgrade packages. It is strongly recommended to place ```yum``` tasks in a separate config!

## Options
`options` - Command line options to be passed to yum. See `man yum` for possible command line options.

`group`   - If the package(s) listed are yum groups, set this to `True`. Default is `False`. This changes the command from `yum install` to `yum groupinstall`

`sudo`    - To execute the yum command with sudo, set this to `True`. *Use with caution! This option is normally not needed or suggested.* If you are choosing to use the ```yum``` directive in your main dotbot config and your user account is a sudoer you may use this to run only your ```yum``` directives under sudo privileges instead of having to run your entire config with root privileges.

`stdin`   - Set to `True` this enables stdin.  Default is `False`

`stdout`  - Set to `True` this enables stdout. Default is `False`

`stderr`  - Set to `True` this enables stderr. Default is `False`

&nbsp;

## Defaults
Default options are applied to all ```yum``` tasks, but can be overridden per task.

### Example
```yaml
- defaults:
    yum:
        options: "-q -y"
        stdout: False
        stderr: True
```

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
        group: True
    package_four:
```
_Notes:_ The last format will do individual yum install calls for each package listed. It is the only supported format for specifying a groupinstall. If you are installing local rpms and there are dependencies between your listed packages it will fail.

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

To see a list of yum groups that are available:
```
yum grouplist -v
```

## Usage

### Example ```packages.conf.yaml```
The suggested format is to group as many packages as possible in lists and set the default options.

```yaml
- defaults:
    yum:
        options: "-q -y"
        stdout: False
        stderr: True

- yum:
    dev-yumgroup:
      options: '-q -y --disablerepo=* --enablerepo=mainline --enablerepo=mainline-extra'
      group: True

- yum: [gdb, valgrind]

```

### Execution
```bash
./install -p dotbot-yum/yum.py -c packages.conf.yaml
```

### Output
Here is the output from a sample config showing all possible formats. It is an unrealistic config, but shows all supported formats and output.

![cli_out](https://i.imgur.com/fBrEBT6.png)
