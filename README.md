### Find video ID:

`alert((new RegExp("key=([0-9a-z]+)")).exec(document.getElementsByClassName("iframeLoaded")[0].getAttribute("src"))[1])`

### As bookmarklet
`javascript:(function()%7Balert((new%20RegExp(%22key%3D(%5B0-9a-z%5D%2B)%22)).exec(document.getElementsByClassName(%22iframeLoaded%22)%5B0%5D.getAttribute(%22src%22))%5B1%5D)%7D)()`

### Build EXE
`pyinstaller --onefile videocampus-sachsen-dl.py`