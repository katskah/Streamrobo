[     UTC     ] Logs for streamrobo.streamlit.app/

────────────────────────────────────────────────────────────────────────────────────────

[10:56:41] 🖥 Provisioning machine...

[10:56:41] 🎛 Preparing system...

[10:56:41] ⛓ Spinning up manager process...

[10:56:41] 🚀 Starting up repository: 'streamrobo', branch: 'main', main module: 'streamrob.py'

[10:56:41] 🐙 Cloning repository...

[10:56:42] 🐙 Cloning into '/mount/src/streamrobo'...

[10:56:42] 🐙 Cloned repository!

[10:56:42] 🐙 Pulling code changes from Github...

[10:56:42] 📦 Processing dependencies...


──────────────────────────────────────── uv ───────────────────────────────────────────


Using uv pip install.

Using Python 3.10.19 environment at /home/adminuser/venv

Resolved 69 packages in 1.07s

Prepared [2025-11-21 10:56:49.911403] 69 packages[2025-11-21 10:56:49.911718]  [2025-11-21 10:56:49.912031] in 5.61s[2025-11-21 10:56:49.912436] 

Installed 69 packages in 199ms

 + aiohappyeyeballs==2.6.1

 + aiohttp==3.13.2

 + aioresponses==0.7.8

 + aiosignal==1.4.0

 + altair==5.5.0

 + async-timeout==5.0.1

 + attrs==25.4.0

 + backoff==2.2.1

 + blinker==1.9.0

 + cachetools==5.5.2

 + certifi==2025.11.12

 + charset-normalizer==3.4.4

 + click==8.3.1

 + contourpy==1.3.2

 + cycler==0.12.1

 + dataclasses-json==0.6.7

 + defusedxml==0.7.1

 + fonttools==4.60.1

 + frozenlist==1.8.0

 + gitdb==4.0.12

 + gitpython==3.1.45

 + idna==3.11

 + inference-sdk==0.16.3

 + jinja2==3.1.6

 + jsonschema==4.25.1

 + jsonschema-specifications==2025.9.1

 + kiwisolver==1.4.9

 + markdown-it-py==4.0.0

 + markupsafe==3.0.3

 + marshmallow==3.26.1

 + matplotlib==3.10.7

 + mdurl==0.1.2

 + multidict==6.7.0

 + mypy-extensions==1.1.0

 + narwhals==2.12.0

 + numpy==1.26.4

 + opencv-python==4.11.0.86

 + packaging==24.2

 + pandas==2.3.3

 + pillow==10.4.0

 + propcache==0.4.1

 + protobuf==5.29.5

 + py-cpuinfo==9.0.0

 + pyarrow==22.0.0

 + pydeck==0.9.1

 + pygments==2.19.2

 + pyparsing==3.2.5

 + python-dateutil==2.9.0.post0

 + pytz==2025.2

 + pyyaml==6.0.3

 + referencing==0.37.0

 + requests==2.32.5

 + rich==13.9.4

 + rpds-py==0.29.0

 + scipy==1.15.3

 + six==1.17.0

 + smmap==5.0.2

 + streamlit==1.39.0

 + supervision==0.27.0

 + tenacity==9.1.2

 + toml==0.10.2

 + tornado==6.5.2

 + tqdm==4.67.1

 + typing-extensions==4.15.0

 + typing-inspect==0.9.0

 + tzdata==2025.2

 + urllib3==2.5.0

 + watchdog==5.0.3

 + yarl==1.22.0

Checking if Streamlit is installed

Found Streamlit version 1.39.0 in the environment

Installing rich for an improved exception logging

Using uv pip install.

Using Python 3.10.19 environment at /home/adminuser/venv

Audited 1 package in 7ms


────────────────────────────────────────────────────────────────────────────────────────


[10:56:52] 🐍 Python dependencies were installed from /mount/src/streamrobo/requirements.txt using uv.

Check if streamlit is installed

Streamlit is already installed

[10:56:53] 📦 Processed dependencies!




2025-11-21 10:56:59.534 Uncaught exception GET /_stcore/stream (127.0.0.1)

HTTPServerRequest(protocol='http', host='streamrobo.streamlit.app', method='GET', uri='/_stcore/stream', version='HTTP/1.1', remote_ip='127.0.0.1')

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.10/site-packages/tornado/websocket.py", line 965, in _accept_connection

    open_result = handler.open(*handler.open_args, **handler.open_kwargs)

  File "/home/adminuser/venv/lib/python3.10/site-packages/streamlit/web/server/browser_websocket_handler.py", line 126, in open

    self._session_id = self._runtime.connect_session(

  File "/home/adminuser/venv/lib/python3.10/site-packages/streamlit/runtime/runtime.py", line 384, in connect_session

    session_id = self._session_mgr.connect_session(

  File "/home/adminuser/venv/lib/python3.10/site-packages/streamlit/runtime/websocket_session_manager.py", line 99, in connect_session

    session = AppSession(

  File "/home/adminuser/venv/lib/python3.10/site-packages/streamlit/runtime/app_session.py", line 133, in __init__

    self._pages_manager = PagesManager(

  File "/home/adminuser/venv/lib/python3.10/site-packages/streamlit/runtime/pages_manager.py", line 236, in __init__

    self.pages_strategy = PagesManager.DefaultStrategy(self, **kwargs)

  File "/home/adminuser/venv/lib/python3.10/site-packages/streamlit/runtime/pages_manager.py", line 74, in __init__

    PagesStrategyV1.watch_pages_dir(pages_manager)

  File "/home/adminuser/venv/lib/python3.10/site-packages/streamlit/runtime/pages_manager.py", line 62, in watch_pages_dir

    watch_dir(

  File "/home/adminuser/venv/lib/python3.10/site-packages/streamlit/watcher/path_watcher.py", line 155, in watch_dir

    return _watch_path(

  File "/home/adminuser/venv/lib/python3.10/site-packages/streamlit/watcher/path_watcher.py", line 126, in _watch_path

    watcher_class(

  File "/home/adminuser/venv/lib/python3.10/site-packages/streamlit/watcher/event_based_path_watcher.py", line 107, in __init__

    path_watcher.watch_path(

  File "/home/adminuser/venv/lib/python3.10/site-packages/streamlit/watcher/event_based_path_watcher.py", line 185, in watch_path

    folder_handler.watch = self._observer.schedule(

  File "/home/adminuser/venv/lib/python3.10/site-packages/watchdog/observers/api.py", line 312, in schedule

    emitter.start()

  File "/home/adminuser/venv/lib/python3.10/site-packages/watchdog/utils/__init__.py", line 75, in start

    self.on_thread_start()

  File "/home/adminuser/venv/lib/python3.10/site-packages/watchdog/observers/inotify.py", line 119, in on_thread_start

    self._inotify = InotifyBuffer(path, recursive=self.watch.is_recursive, event_mask=event_mask)

  File "/home/adminuser/venv/lib/python3.10/site-packages/watchdog/observers/inotify_buffer.py", line 30, in __init__

    self._inotify = Inotify(path, recursive=recursive, event_mask=event_mask)

  File "/home/adminuser/venv/lib/python3.10/site-packages/watchdog/observers/inotify_c.py", line 167, in __init__

    self._add_dir_watch(path, event_mask, recursive=recursive)

  File "/home/adminuser/venv/lib/python3.10/site-packages/watchdog/observers/inotify_c.py", line 387, in _add_dir_watch

    self._add_watch(path, mask)

  File "/home/adminuser/venv/lib/python3.10/site-packages/watchdog/observers/inotify_c.py", line 407, in _add_watch

    Inotify._raise_error()

  File "/home/adminuser/venv/lib/python3.10/site-packages/watchdog/observers/inotify_c.py", line 418, in _raise_error

    raise OSError(errno.ENOSPC, "inotify watch limit reached")

OSError: [Errno 28] inotify watch limit reached

Exception ignored in: <function AppSession.__del__ at 0x79ceb26cfeb0>

Traceback (most recent call last):

  File "/home/adminuser/venv/lib/python3.10/site-packages/streamlit/runtime/app_session.py", line 174, in __del__

    self.shutdown()

  File "/home/adminuser/venv/lib/python3.10/site-packages/streamlit/runtime/app_session.py", line 240, in shutdown

    if self._state != AppSessionState.SHUTDOWN_REQUESTED:

AttributeError: 'AppSession' object has no attribute '_state'

────────────────────── Traceback (most recent call last) ───────────────────────

  /home/adminuser/venv/lib/python3.10/site-packages/streamlit/runtime/scriptru  

  nner/exec_code.py:88 in exec_func_with_error_handling                         

                                                                                

  /home/adminuser/venv/lib/python3.10/site-packages/streamlit/runtime/scriptru  

  nner/script_runner.py:579 in code_to_exec                                     

                                                                                

  /mount/src/streamrobo/streamrob.py:2 in <module>                              

                                                                                

     1 import streamlit as st                                                   

  ❱  2 from inference_sdk import InferenceHTTPClient                            

     3 from PIL import Image                                                    

     4 import numpy as np                                                       

     5 import io                                                                

                                                                                

  /home/adminuser/venv/lib/python3.10/site-packages/inference_sdk/__init__.py:  

  5 in <module>                                                                 

                                                                                

     2 import warnings                                                          

     3                                                                          

     4 from inference_sdk.config import InferenceSDKDeprecationWarning          

  ❱  5 from inference_sdk.http.client import InferenceHTTPClient                

     6 from inference_sdk.http.entities import (                                

     7 │   InferenceConfiguration,                                              

     8 │   VisualisationResponseFormat,                                         

                                                                                

  /home/adminuser/venv/lib/python3.10/site-packages/inference_sdk/http/client.  

  py:41 in <module>                                                             

                                                                                

      38 │   execute_requests_packages_async,                                   

      39 )                                                                      

      40 from inference_sdk.http.utils.iterables import unwrap_single_element_  

  ❱   41 from inference_sdk.http.utils.loaders import (                         

      42 │   load_static_inference_input,                                       

      43 │   load_static_inference_input_async,                                 

      44 │   load_stream_inference_input,                                       

                                                                                

  /home/adminuser/venv/lib/python3.10/site-packages/inference_sdk/http/utils/l  

  oaders.py:6 in <module>                                                       

                                                                                

      3 from typing import Generator, List, Optional, Tuple, Union              

      4                                                                         

      5 import aiohttp                                                          

  ❱   6 import cv2                                                              

      7 import numpy as np                                                      

      8 import requests                                                         

      9 import supervision as sv                                                

                                                                                

  /home/adminuser/venv/lib/python3.10/site-packages/cv2/__init__.py:181 in      

  <module>                                                                      

                                                                                

    178 │   if DEBUG: print('OpenCV loader: DONE')                              

    179                                                                         

    180                                                                         

  ❱ 181 bootstrap()                                                             

    182                                                                         

                                                                                

  /home/adminuser/venv/lib/python3.10/site-packages/cv2/__init__.py:153 in      

  bootstrap                                                                     

                                                                                

    150 │                                                                       

    151 │   py_module = sys.modules.pop("cv2")                                  

    152 │                                                                       

  ❱ 153 │   native_module = importlib.import_module("cv2")                      

    154 │                                                                       

    155 │   sys.modules["cv2"] = py_module                                      

    156 │   setattr(py_module, "_native", native_module)                        

                                                                                

  /usr/local/lib/python3.10/importlib/__init__.py:126 in import_module          

                                                                                

    123 │   │   │   if character != '.':                                        

    124 │   │   │   │   break                                                   

    125 │   │   │   level += 1                                                  

  ❱ 126 │   return _bootstrap._gcd_import(name[level:], package, level)         

    127                                                                         

    128                                                                         

    129 _RELOADING = {}                                                         

────────────────────────────────────────────────────────────────────────────────

ImportError: libGL.so.1: cannot open shared object file: No such file or 

directory

main
katskah/streamrobo/main/streamrob.py
