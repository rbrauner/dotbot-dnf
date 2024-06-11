# Dotbot ```dnf``` Plugin

Plugin for [Dotbot](https://github.com/anishathalye/dotbot), that adds ```dnf``` directive, which allows you to install and upgrade packages and groups using ```dnf```.

## Installation

1) Simply add this repo as a submodule of your dotfiles repository:

```
git submodule add https://gitlab.com/flyingchipmunk/dotbot-dnf.git
```

2) Pass this folder (or directly dnf.py file) path with corresponding flag to your [Dotbot](https://github.com/anishathalye/dotbot) script:

```
-p /path/to/file/dnf.py
```
  or

```
--plugin-dir /path/to/plugin/folder
```

 **WARNING!**

 Dotbot (or install script) needs to be executed with root permissions (as sudo) in order to install/upgrade packages. It is strongly recommended to place ```dnf``` tasks in a separate config!

## Options
`options` - Command line options to be passed to dnf. See `man dnf` for possible command line options.

`group`   - If the package(s) listed are dnf groups, set this to `True`. Default is `False`. This changes the command from `dnf install` to `dnf groupinstall`

`sudo`    - To execute the dnf command with sudo, set this to `True`. *Use with caution! This option is normally not needed or suggested.* If you are choosing to use the ```dnf``` directive in your main dotbot config and your user account is a sudoer you may use this to run only your ```dnf``` directives under sudo privileges instead of having to run your entire config with root privileges. Default is `False`

`stdin`   - Set to `True` this enables stdin.  Default is `False`

`stdout`  - Set to `True` this enables stdout. Default is `False`

`stderr`  - Set to `True` this enables stderr. Default is `False`

&nbsp;

## Defaults
Default options are applied to all ```dnf``` tasks, but can be overridden per task.

### Example
```yaml
- defaults:
    dnf:
        options: "-q -y"
        stdout: False
        stderr: True
```

## Supported task variants
The various formats supported are shown below. If you want to bundle a group of packages in the same ```dnf``` call use the list format. This speeds up the process as the dependency scan only happens once instead of for each package individually.


### Formats Supported
```yaml
- dnf: package_one
```
```yaml
- dnf: [package_one, package_two, package_three]
```
```yaml
- dnf:
    package_one:
        options: "-v -y"
    package_two: "-q -y"
    package_three:
        group: True
    package_four:
```
_Notes:_ The last format will do individual dnf install calls for each package listed. It is the only supported format for specifying a groupinstall. If you are installing local rpms and there are dependencies between your listed packages it will fail.

### Specifying package names
Again see `man dnf` for more details, but in general these formats are supported by dnf.
```
name
name.arch
name-ver
name-ver-rel
name-ver-rel.arch
name-epoch:ver-rel.arch
epoch:name-ver-rel.arch
```

To see a list of dnf groups that are available:
```
dnf grouplist -v
```

## Usage

### Example ```packages.conf.yaml```
The suggested format is to group as many packages as possible in lists and set the default options.

```yaml
- defaults:
    dnf:
        options: "-q -y"
        stdout: False
        stderr: True

- dnf:
    dev-dnfgroup:
      options: '-q -y --disablerepo=* --enablerepo=mainline --enablerepo=mainline-extra'
      group: True

- dnf: [gdb, valgrind]

```

### Execution
```bash
./install -p dotbot-dnf/dnf.py -c packages.conf.yaml
```

### Output
Here is the output from a sample config showing all possible formats. It is an unrealistic config, but shows all supported formats and output.

![cli_out](https://i.imgur.com/fBrEBT6.png)

## Original repository

- https://gitlab.com/flyingchipmunk/dotbot-yum
