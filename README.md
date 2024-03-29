# IOT-Project: Smart travel system (36h Hackathon)

As part of the **BCG Platinion Hackathon 2019**, our team developed a **"Smart Travel System"** for NextGenConsultants.



**BUSINESS PROBLEM**
--------

As a consultant, you want to be sure that you have everything you need for the upcoming workweek, and don't worry about forgetting your tie for the CEO meeting or the key card for the Copenhagen office, or even realising when you're packing that certain clothes aren't available. 



**SOLUTION**
--------

Our product solution consisted of a **smart suitcase, a sensor for your wardrobe** and an **IOS-application** that provides  
* *recommendation* on what to put in the suitcase regarding the consultant's upcoming travel plans, the weather at the destinations, the type of meetings and the cloakroom status and 
* *realtime feedback* about the packing activities to ensure the completion of the packing process. 

For the working MVP we made use of *AWS services* for the Full Stack: 
* AWS IOT core service, 
* AWS Lambda service and 
* AWS DynamoDB 

which we connected to 
* two Rasberry Pi 3B+ devices linked with 
* RFID-Card reader
in order to collect the RFID tags data to track the real-time location of the clothes in the wardrobe and suitcase. 

To visualize the information for the consultant, we developed an IOS app and linked it to the developed technology system.



**CREDITS** 
_______________________________

* Johannes Hoerst (IT Architect)
* Fazeel Akthar (iOS development) https://github.com/FazeelAkhtar
* Gaurav Joshi (Edge & cloud development team mate) https://github.com/Gauravjsh127
* Rafael Pina (Database architect) https://github.com/rafaalb
