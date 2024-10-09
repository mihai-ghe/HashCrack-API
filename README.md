An API made to make storing, cracking and accessing your hashes easier at a distance. This app was made for people working in the field with a CrackStation at home. The gui was made using tkinter-designer by Parth Jadhav https://github.com/ParthJadhav/Tkinter-Designer. Go ahead and take a look at his amazing project. This app is by no means finished, lacking advanced options for the JTR commands that are run server-side and probably more features that I haven't thought about. If you have any suggestions I'd love to hear them! 

As this is just a Proof Of Concept project I have not made a release version, packaged into an app. If there is any demand for something like that please let me know!

Usage:

"python3 HashCrackAPI server" to launch the server. ( No GUI ). The server assumes it is running on a linux machine and that JohnTheRipper is installed.

"python3 HashCrackAPI client" to launch the client.

At this moment, the server runs on port 5000. This must be modified manually at the moment.
