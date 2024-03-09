# hiiii again

[<img src="https://github.com/cakeGit/random-additional/blob/e41af287944c9187aeb5a8e946b367f063e6c89e/download-free-.png"/>](https://github.com/cakeGit/super-marked-dash/archive/refs/heads/main.zip)<br/>

so i changed alot of stuff<br/>
i did the module split thing i talked about in the last one<br/>
so that each file will generally be about like a page and a bit on my screen<br/>
<br/>
i reccomend you spend some time figuring out the new structure, ive added comments at the top of each file for whats up<br/>
<br/>
i will try oto put usage comments on sutff<br/>
<br/>
ask me anything else (cakeistasty_ on disc)

# big notes

## new things to know

### Game class
this is a class made to hold like game options, and user position, and level<br/>
basically everything about the game itself<br/>
this lets it get passed through classes such as menus for changing options, since importing main.py anywhere will make python have a stroke ig<br/>

### menus.py / menushandler.py
these files hold well, the menus, menusHandler is used to keep track of the history, and where the menus are opened in the first place, but menus holds the actual menus themselves, alongside their drawing functions and click handling functions

also sry for ruining your code im a massachist im enjoying this too much

theres alot of stuff everywhere btw

## debug renderers
theres a few debug renderers, they are controlled in constants.py, and draw boxes around objects in the world

[![](https://mermaid.ink/img/pako:eNptVE1v2zAM_SuCTi1Qu9g1h10arD20wLBs2EEOBsViHW2ObEhygaDofx9JWf5ImoMiUXzkI_msd1l3BuRGNl73R_FzW7nKheGQjkZHLdQW1z3ZhwCeTOqmvM_7-9u9KIpChLrzcOi0N2Ud3tTN-nzLeHCGQ65yhObPCTC0esFVHLUzrXUN-gv8oWfk27I_i6J8wOsGgqgH78FF0esGyuKrEEcbYufPCUQAjgOeYcUjxCBi1xfoOnoq9ZQ2e2IWRyv6bm3oW32echAmM8g1ZMpXdWjrFC3oy2GZfjpj6B3RyNRbeINWWEfxG30CpR5xTWwImPMgOrdimYrhQT1zlEXTUk6-XbXgG8T6CIGyJejkFmiaaZdnyacvqeDYHf5CHccBcCeTRRh4tc5G27lQ5rAZtKhgSrfiTz0Gr77z3_XUaaWujBlTs-quba0Bz-lSgLnGhLm0IuVfPUoONZOuRN8xnIInSEo4kk1Ol2RnLavdtGVFE3i-fVp2_EG3Lfcb5b-LHjDhzHNtQ5Y_IA7eBUHfGvH7LOhCfvM1c_2cwSRl-ubWOr4SyEQAWY8KIRqjeCs3q3geyKym5RhyEtR71D6S09zsyl1WXvz2NkKxKplejGVVdGaK2pRXDZV3EjfIz-Ar9k5pKhmPgBnlBrdG-3-VrNwH-ukhdruzq-Um-gHu5MDS2FqNkz7JzatuA1rBWHwLXtKzyK_jx3_nT9i4?type=png)](https://mermaid.live/edit#pako:eNptVE1v2zAM_SuCTi1Qu9g1h10arD20wLBs2EEOBsViHW2ObEhygaDofx9JWf5ImoMiUXzkI_msd1l3BuRGNl73R_FzW7nKheGQjkZHLdQW1z3ZhwCeTOqmvM_7-9u9KIpChLrzcOi0N2Ud3tTN-nzLeHCGQ65yhObPCTC0esFVHLUzrXUN-gv8oWfk27I_i6J8wOsGgqgH78FF0esGyuKrEEcbYufPCUQAjgOeYcUjxCBi1xfoOnoq9ZQ2e2IWRyv6bm3oW32echAmM8g1ZMpXdWjrFC3oy2GZfjpj6B3RyNRbeINWWEfxG30CpR5xTWwImPMgOrdimYrhQT1zlEXTUk6-XbXgG8T6CIGyJejkFmiaaZdnyacvqeDYHf5CHccBcCeTRRh4tc5G27lQ5rAZtKhgSrfiTz0Gr77z3_XUaaWujBlTs-quba0Bz-lSgLnGhLm0IuVfPUoONZOuRN8xnIInSEo4kk1Ol2RnLavdtGVFE3i-fVp2_EG3Lfcb5b-LHjDhzHNtQ5Y_IA7eBUHfGvH7LOhCfvM1c_2cwSRl-ubWOr4SyEQAWY8KIRqjeCs3q3geyKym5RhyEtR71D6S09zsyl1WXvz2NkKxKplejGVVdGaK2pRXDZV3EjfIz-Ar9k5pKhmPgBnlBrdG-3-VrNwH-ukhdruzq-Um-gHu5MDS2FqNkz7JzatuA1rBWHwLXtKzyK_jx3_nT9i4)
