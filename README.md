# Discord-Auto-Messenger     
This is a Python script that allows you to send automated messages to a Discord channel. Randomly sends messages from chat dataset to appear more human-like.      

## Installation    

  ### Local Machine or Repl

 1. Clone the repository or download the code as a zip file and extract it to a folder:  
 
     ```
     git clone https://github.com/xRiddin/Discord-Auto-message.git
     ```
     
     If you do not have Git, you may also press the Download button (GitHub) and unzip the code.  


 2. Navigate to the project directory in your terminal:  
 
     ```
     cd /Downloads/Discord-Auto-message/
     ```
 
 3. Install the required packages using pip:  
 
    ```
    pip install -r requirements.txt
    ```
 
 4. (Optional) In **messages.txt** add the messages you want to send, each on a new line. By default there are lines of text to randomly print the texts.

    ### (Optional) for 100% uptime host it on uptimerobot.com

1. sign up at uptimerobot.com

2. Add new monitor and select Http(s)
   ![alt text](https://github.com/xRiddin/Discord-Auto-message/blob/main/image.png?raw=true)

3. Run the program in replit, copy the url
   ![alt text](https://github.com/xRiddin/Discord-Auto-message/blob/main/image1.png?raw=true)

4. Paste the url in the uptimerobot:
   ![alt text](https://github.com/xRiddin/Discord-Auto-message/blob/main/image2.png?raw=true)

5. Save the changes and have fun!

   
 
## Usage
 
   The script can be run using the following command:  

    python auto.py
    
 When running the script, you will be prompted to enter the number of seconds to wait between each message.  
 
 
## Options
   The following options are available:

`--config` : Configures the user information by prompting for **user ID, Discord token, Discord channel URL, and Discord channel ID**:    

```
  python auto.py --config
```

 `--setC` : Sets the channel to send messages to by prompting for the Discord channel URL and channel ID.    
 
 ```
  python auto.py --setC
 ```
 
 `--help` : Shows help for the script and its available options.
 
 ```
  python auto.py --help
```
 
## Contributing
  If you find a bug or have a feature request, please create an issue on GitHub. Pull requests are also welcome.  
  **Please do star this project if you like my work.**


