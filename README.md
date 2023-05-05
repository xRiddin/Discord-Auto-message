# Discord-Auto-Messenger     
This is a Python script that allows you to send automated messages to a Discord channel. Randomly sends messages from chat dataset to appear more human-like.      

## Installation    

  ### Local Machine or Online IDE(with cmd/shell)  

 1. Clone the repository or download the code as a zip file and extract it to a folder:  
 
     ```
     git clone https://github.com/Jeevaraz/Discord-Auto-msg.git
     ```
     
     If you do not have Git, you may also press the Download button (GitHub) and unzip the code.  


 2. Navigate to the project directory in your terminal:  
 
     ```
     cd /Downloads/Discord-Auto-msg/
     ```
 
 3. Install the required packages using pip:  
 
    ```
    pip install -r requirements.txt
    ```
 
 4. (Optional) In **messages.txt** add the messages you want to send, each on a new line. By default there are lines of text to randomly print the texts.    
 
## Usage
 
   The script can be run using the following command:  

    python3 auto.py
    
 When running the script, you will be prompted to enter the number of seconds to wait between each message.  
 
 
## Options
   The following options are available:

`--config` : Configures the user information by prompting for **user ID, Discord token, Discord channel URL, and Discord channel ID**:    

```
  python3 auto.py --config
```

 `--setC` : Sets the channel to send messages to by prompting for the Discord channel URL and channel ID.    
 
 ```
  python3 auto.py --setC
 ```
 
 `--help` : Shows help for the script and its available options.
 
 ```
  python3 auto.py --help
```
 
## Contributing
  If you find a bug or have a feature request, please create an issue on GitHub. Pull requests are also welcome.  
  **Please do star this project if you like my work.**


