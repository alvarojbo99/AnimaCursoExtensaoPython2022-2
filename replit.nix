# The command that runs the program. If the interpreter field is set, it will have priority and this run command will do nothing
run = "python3 aula3-2022-11-09.py"

# The primary language of the repl. There can be others, though!
language = "python3"
entrypoint = "aula3-2022-11-09.py"
{ pkgs }: {
  deps = [
    pkgs.python38Full
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Needed for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for matplotlib
      pkgs.xorg.libX11
    ];
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
  };
}