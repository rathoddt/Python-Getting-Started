## Anaconda installation
installation finished.

Do you wish to update your shell profile to automatically initialize conda?

This will activate conda on startup and change the command prompt when activated.

If you'd prefer that conda's base environment not be activated on startup,

   run the following command when conda is activated:


``
conda config --set auto_activate_base false
``


You can undo this by running `conda init --reverse $SHELL`? [yes|no]

[no] >>> 

To activate this environment, use                                             
``                                                                               
$ conda activate quant                                                    
``
To deactivate an active environment, use
``
$ conda deactivate
``



``
 458  export PATH="/home/dilip/anaconda3/bin:$PATH"

  459  PATH
  460  echo $PATH
  461  cd
  462  conda activate
  463  conda --version
  464  conda create --name quant python=3.11

  conda update --all

``


   


``
conda update --all
conda activate quant
conda install spyder
``


List all installed packer with their versions  
``
pip freeze
``