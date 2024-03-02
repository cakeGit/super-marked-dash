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

## new modules

### Game class
this is a class made to hold like game options, and user position, and level<br/>
basically everything about the game itself<br/>
this lets it get passed through classes such as menus for changing options, since importing main.py anywhere will make python have a stroke ig<br/>

### menus.py / menushandler.py
these files hold well, the menus, menusHandler is used to keep track of the history, and where the menus are opened in the first place, but menus holds the actual menus themselves, alongside their drawing functions and click handling functions

also sry for ruining your code im a massachist im enjoying this too much

## debug renderers
theres a few renderes to help with development, first is in menus.py<br/>
`RENDER_DEBUG_BUTTON_COLLIDERS = True`<br/>
this makes the menu's buttons have a red outline of what can be clicked<br/>
as well as the one in playerhandler.py for seeing colliders
