#!/bin/bash

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# © Enrique Estévez Fernández <keko.gl[fix@]gmail[fix.]com>
# © Proxecto Trasno <proxecto[fix@]trasno[fix.]net>
# novembro 2018

## -

# execute « [bash |./]genPackages TASK [version edition] »

## Script para xerar correctores ortográficos para o galego baseados
## en Hunspell para diferentes aplicativos


# Path to the folder where the projects are placed
root_path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/.."

path_templates="templates"

## Change the variables or pass it as arguments
version="18.07"
edition="Francisco Mirás"

## Name that will take the package of the spellchecker followed of the version.
## Example: Corrector_de_galego-18.07.oxt for LibreOffice
filename="Corrector_de_galego-"

zip=$(which zip 2>/dev/null)

## Código reutilizado dun script de Francesco Flodolo (Membro do equipo l10n de Mozilla)
## https://github.com/flodolo/scripts/blob/master/mozilla_l10n/update_central.sh
#############################################################################################
function interrupt_code()
# This code runs if user hits control-c
{
  echored "*** Setup interrupted ***"
  exit $?
}

# Trap keyboard interrupt (control-c)
trap interrupt_code SIGINT

# Pretty printing functions
NORMAL=$(tput sgr0)
GREEN=$(tput setaf 2; tput bold)
YELLOW=$(tput setaf 3)
RED=$(tput setaf 1)

function echored() {
    echo -e "$RED$*$NORMAL"
}

function echogreen() {
    echo -e "$GREEN$*$NORMAL"
}

function echoyellow() {
    echo -e "$YELLOW$*$NORMAL"
}
#############################################################################################


function generate_oxt(){
	cd $root_path
	if [ $1 != "" ]; then
		version=$2
	fi
	if [ $2 != "" ]; then
		edition=$3
	fi

	if [ -f build/gl.aff ] && [ -f build/gl.dic ]
		then
			mkdir -p $path_templates/temp
			## Files of hunspell-gl project
			cp changelog.txt $path_templates/temp/
			cp license.txt $path_templates/temp/
			cp license-gl.txt $path_templates/temp/
			cp build/gl.aff $path_templates/temp/
			cp build/gl.dic $path_templates/temp/
			## Commons files for the .xpi and .oxt packages
			cp $path_templates/readme.txt $path_templates/temp/
			cp $path_templates/readme-gl.txt $path_templates/temp/
			## Especific files for the .oxt package
			cp -r $path_templates/libo/* $path_templates/temp/
			sed -n -e "
				/__/! { p; };
				/__EDITION__/ { s//$edition/g; p; }" \
 			./$path_templates/libo/package-description.txt > ./$path_templates/temp/package-description.txt
			sed -n -e "
				/__/! { p; };
				/__VERSION__/ { s//$version/g; p; }" \
 			./$path_templates/libo/description.xml > ./$path_templates/temp/description.xml

			if [ "$zip" != "" ]
			then
				cd $path_templates/temp
				$zip -r -q $root_path/build/"$filename$version.oxt" ./*
				echogreen "It has created the $filename$version.oxt package.Edición «$edition»."
				echoyellow "The package is localized in the build folder."
				cd $root_path
			else
				echored "The zip application is nos installed. Could not generate the .oxt package."
				echored "Try to installing the zip application."
			fi
			rm -r $path_templates/temp
		else
			echored "Before it executes this script it must generate the .aff and .dic files."
		fi
}

function generate_xpi(){
	cd $root_path/templates
	mkdir -p temp
	echo "Not implemented yet."
	rm -r temp
}

function usage(){
	echogreen "Usage: ./genPackages.sh TASK [version edition]"
	echo ""
	echo "For more information, execute ./genPackages.sh --help"
}

function simple_help(){
	echogreen "Usage: ./genPackages.sh TASK [version edition]"
	echo ""
	echo "The script can execute the following tasks:"
	echo "	oxt	It generates the spellchecker for LibreOffice. It needs two parameters:"
	echo "		- The version in format yy.mm (year.month)."
	echo "		- The edition, the name of a personality between quotes."
	echo "		Example of usage: ./genPackages.sh oxt 18.07 \"Francisco Mirás\"."
	echo ""
	echo "	xpi	Not implemented yet."
	echo "		Example of usage: ./genPackages.sh xpi"
}

if [ $# -eq 0 ]
	then
		usage
	else
		param=$1
		[ $param = --help ] && simple_help
		[ $param = oxt ] && generate_oxt "$@"
		[ $param = xpi ] && generate_xpi 
	fi

#.EOF
