# Copyright (C) 2015 Kevin Ross
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature


class SunbeltDetectFiles(Signature):
    name = "antisandbox_sunbelt_files"
    description = "Detects Sunbelt Sandbox through the presence of a file"
    severity = 3
    categories = ["anti-sandbox"]
    authors = ["Kevin Ross"]
    minimum = "0.5"
    ttps = ["T1083", "T1057"]
    mbcs = ["B0007"]

    def run(self):
        indicators = [
            ".*\\\\SandboxStarter\.exe$",
            "^C\:\\\\analysis\\\\.*",
        ]

        for indicator in indicators:
            if self.check_file(pattern=indicator, regex=True):
                return True

        return False
