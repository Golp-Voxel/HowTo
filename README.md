# How To Install Tango

Pre-install [Java](https://www.java.com/en/download/) in all machines that are going to use Tango and [MySQL](https://dev.mysql.com/downloads/mysql/5.7.html) on the main machine or on the machines that you want to have their own database.

You can find the latest versions of Tango in [here](https://gitlab.com/tango-controls/TangoSourceDistribution/-/releases).

Following the documentation of [Tango](https://tango-controls.readthedocs.io/en/latest/How-To/installation/tango-on-windows.html), you should easily install Tango. If this link is nolonger avaible you can find the documentation of the 9.3.7 pdf in the `Doc_Tango` folder. This documentation is close to the one use to install the version **9.5.0 in Voxel** (at the time I used the documentation of the version 9.3.4 you can also find that pdf on the folder, the instalation process for the Windows should be the same).  

Also if the link and the version of Tango you want to install is deferent I suggest to go to the main page of [Tango Controll](https://www.tango-controls.org/).

If you find a erro on the criation of the DataBase `'create_db_tables.sql': Specified key was too long; max key length is 1000 bytes` you can find the solution [here](https://www.tango-controls.org/community/forum/c/general/installation/tango-9-windows-demo-installation-problem/?page=1#post-3999).


# How To Install a Device Server

The Documention presented on the Doc_Tango also provied a good base on: How to start a device server, How to PyTango, ...

[How to start a device server](https://tango-controls.readthedocs.io/en/9.3.7/tutorials-and-howtos/how-tos/how-to-start-device-server.html)