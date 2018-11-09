const APP_NAME			= "Corrector ortogr�fico de Galego";
const APP_PACKAGE		= "gl-es@dictionaries.addons.mozilla.org";
const APP_VERSION		= "18.07.0";

var err = initInstall(APP_NAME, APP_PACKAGE, APP_VERSION);
if (err != SUCCESS)
    cancelInstall();

var fProgram = getFolder("Program");
err = addDirectory("", "gl-es@dictionaries.addons.mozilla.org",
		   "dictionaries", fProgram, "dictionaries", true);
if (err != SUCCESS)
    cancelInstall();

performInstall();
