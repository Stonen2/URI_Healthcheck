# URI_Healthcheck
Did you know that there are modern webservers that do not have built in outage reports? I had no idea, and a friends website absolutely-specatacularly crashed every web page. I think it was a DNS change issue, but the hotfix had nothing to do with redeploying web pages to a new IP address. My solution? Build my own watchdog script. 


Virtually all of my production applications use some sort of similar technique and its trivial. We are sending a simple GET request to a URL embedded within a website that we know (when web app is functioning properly) repsonds with a HTTP status code of 200. This does the same thing with a list of urls... So you can use this for as many URLS as you'd like. In production, each individual app monitors itself which I am not sure that is the most efficient? Distibuted systems are wild, so individual watch dogs might make sense. IE a single app running this can fail, so we add built in redundancy. All of this information aside, I am running this script to emulate 'best practices' that I employ wihtin a professional setting for friends web apps (that I have source code running on, so I feel responsible to put my best foot forward). 

Source code is attrocious, but I wanted to get something deployed as fast a humanly possible to ensure web app monitoring is established immediately. Feel free to use this source code and modify it to your individual needs. As I have said, it is seriously trivial. Non-200 response codes transmit an email to 'hard coded' email accounts you can provide. I use this script to monitor mulitple clients/personal websites. So the source code is manually chopped up to deviate between friends, I always email myself which is why there is a second line. 

If you are curious where improvements could be made here you go. 

* Properties files with encryption on passwords instead of embedding hardcoded values for passwords on email authentication (ConfigParser) {Java is better}
* Correlating URLs with necessary contact information (arguably class obects, but python classes leave a lot to be desired on performance and readbility) 
* Requirements.txt file generation 
* Web UI To visually show error messages/response codes. I do not include or differentiate between 404, 403, 301, etc. script only cares for 200 status code 


" I'm watching you, Wazowski. Always watching. Always. " -Roz Monsters Inc. 
