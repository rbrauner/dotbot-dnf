import os, platform, subprocess, dotbot

class Yum(dotbot.Plugin):
    _directive = "yum"

    def can_handle(self, directive):
        return directive == self._directive

    def handle(self, directive, data):
        if directive != self._directive:
            raise ValueError('yum cannot handle directive {0}'.format(directive))
        success = self._process_packages(data)
        if success:
            self._log.info('All packages have been installed')
        else:
            self._log.error('Some packages were not installed')

        return success


    def _process_packages(self, packages):
        if os.geteuid() != 0:
            msg = 'Need root permissions to install packages'
            self._log.error(msg)
            raise YumError(msg)

        defaults = self._context.defaults().get('yum', {})
        yum_opts = defaults.get('options', '')

        if isinstance(packages, str):
            # single package
            return self._install(packages, yum_opts)
        elif isinstance(packages, list):
            # multiple packages in list, one install for all
            pkg_list = ' '.join(packages)
            return self._install(pkg_list, yum_opts)
        elif isinstance(packages, dict):
            # multiple packages in dict with possible otions, one install per package
            for pkg_name, pkg_opts in packages.items():
                if isinstance(pkg_opts, dict):
                    yum_opts = pkg_opts.get('options', yum_opts)
                elif pkg_opts:
                    yum_opts = pkg_opts
                else:
                    yum_opts = defaults.get('options', '')

                if not self._install(pkg_name, yum_opts):
                    return False

            return True


    def _install(self, packages, opts):
        if not packages:
            return True

        cwd = self._context.base_directory()

        with open(os.devnull, 'w') as devnull:
            stdin = stdout = stderr = devnull

            self._log.info("Installing [{0}] with options [{1}]".format(packages, opts))

            cmd = "yum install {0} {1}".format(opts, packages)
            ret_code = subprocess.call(cmd, shell=True, stdin=stdin, stdout=None, stderr=None, cwd=cwd)

            if ret_code != 0:
                self._log.error("Failed to install [{0}]".format(packages))
                return False
            return True


class YumError(Exception):
    pass
