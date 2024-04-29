# 💬 Intranet Python Chat 
This project works with only two Python third-party modules:

- 📨 [Paho.MQTT](https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html) for communication protocol;
- 📪 [GetMac](https://pypi.org/project/getmac/) to gather the address.

Also, this project uses built-in modules:
- 🗂️ [JSON](https://python.readthedocs.io/en/v2.7.2/library/json.html) to storage the messages from the MQTT retained topic;
- ⏰ [DateTime](https://docs.python.org/3/library/datetime.html) to gather the specific time that the user sends the message or when the user registers;
- 🧑‍💻 [SYS](https://docs.python.org/3/library/sys.html) to leave the code when we are at some specific conditions;
- 🗄️ [AST](https://docs.python.org/3/library/ast.html) to convert string list into lists with ast.literal_eval();

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MQTT](https://img.shields.io/badge/mqtt-5e5086?style=for-the-badge&logo=MQTT&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-F7DF1E?style=for-the-badge&logo=JSON&logoColor=black)

## ❓ Which Purpose Does This Project Have?
This project is meant to be an "internal network chat" like the ones we have inside some companies around the world. The only purpose to use something like that is the supervising capacity the company will have.

## 🔄 Possible Future Updates
- DJango Framework (GUI); OR
- Flet (GUI).

I've created a Flet base program, but when the code reach the "display log" part, the Flet Aplication just crashes. I'll try to solve this error, probably this will take some time, but i'll manage to do reach a solution.

## 🛠️ This Code Works With
I've created a Module named "CleanTerminarModule", this module is a simple way to explain, just cleans the terminal depending in which OS the User are at the moment.

![Windows](https://img.shields.io/badge/Windows-000?style=for-the-badge&logo=windows&logoColor=2CA5E0)
![Ubuntu](https://img.shields.io/badge/Ubuntu-35495E?style=for-the-badge&logo=ubuntu&logoColor=2CA5E0)
![Linux](https://img.shields.io/badge/Linux-000?style=for-the-badge&logo=linux&logoColor=FCC624)
![MAC](https://img.shields.io/badge/MAC-FFFFFF?style=for-the-badge&logo=APPLE&logoColor=black)
![Vscode](https://img.shields.io/badge/Vscode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## 🔗 Links
[![github](https://img.shields.io/badge/github-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/VicourtBitt)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vicourtbitt)

# 🙋 How The Code Works
These are some fluxograms that I've made for us all.

![](https://github.com/VicourtBitt/Intranet_Python_Chat/blob/main/img_starter_page_before_main.png)

![](https://github.com/VicourtBitt/Intranet_Python_Chat/blob/main/img_main_loop.png)
